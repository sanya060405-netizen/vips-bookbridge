"""
BookBridge: A Campus Book and Learning-Material Exchange Board
MCA 1st Year Mini-Project
Student: Sanya | Enrollment No: 10517704426 | Section: MCA 1-B
Project Mentor: Dr. Cosmena
"""

from flask import Flask, render_template, request, redirect, url_for, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
import os
import re
import sqlite3
from database import get_db, init_db, DB_PATH

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'bookbridge_mca_secret_key_2026_sanya')

# Ensure database exists when application starts
def ensure_db():
    """Ensure database schema exists and initial records are seeded."""
    if not os.path.exists(DB_PATH) or os.path.getsize(DB_PATH) == 0:
        init_db(seed=True)

ensure_db()

# -------------------------------------------------------------
# Authentication & Request Helpers
# -------------------------------------------------------------
@app.before_request
def load_logged_in_user():
    """Populates g.user with the currently logged-in student's details."""
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None
    else:
        conn = get_db()
        g.user = conn.execute(
            "SELECT id, enrollment_no, full_name, email, department, course_year, contact_phone FROM users WHERE id = ?",
            (user_id,)
        ).fetchone()
        conn.close()

def login_required(view):
    """Decorator to enforce login on protected routes."""
    @wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            flash("Please sign in with your campus account to access this feature.", "warning")
            return redirect(url_for('login', next=request.url))
        return view(**kwargs)
    return wrapped_view

@app.context_processor
def inject_global_data():
    """Provides unread request count and VIPS college info across all templates."""
    pending_count = 0
    if g.user:
        conn = get_db()
        row = conn.execute("""
            SELECT COUNT(*) AS count
            FROM exchange_requests er
            JOIN listings l ON er.listing_id = l.id
            WHERE l.user_id = ? AND er.status = 'Pending'
        """, (g.user['id'],)).fetchone()
        if row:
            pending_count = row['count']
        conn.close()
    return {
        'pending_requests_count': pending_count,
        'college_name': 'VIVEKANANDA INSTITUTE OF PROFESSIONAL STUDIES',
        'college_short': 'VIPS-TC',
        'college_full': 'Vivekananda Institute of Professional Studies – Technical Campus',
        'college_address': 'AU Block, Outer Ring Road, Pitampura, New Delhi - 110034',
        'college_affiliation': 'Affiliated to Guru Gobind Singh Indraprastha University (GGSIPU), Delhi'
    }

# -------------------------------------------------------------
# Main Public & Catalog Routes
# -------------------------------------------------------------
@app.route('/')
def index():
    """Homepage: Searchable catalog of books and learning materials."""
    conn = get_db()
    
    query = request.args.get('q', '').strip()
    listing_type = request.args.get('type', '').strip()
    course = request.args.get('course', '').strip()
    status = request.args.get('status', '').strip()
    meeting_point = request.args.get('meeting_point', '').strip()
    
    sql = """
        SELECT l.*, u.full_name AS owner_name, u.department AS owner_dept, u.course_year AS owner_year,
               mp.name AS meeting_point_name
        FROM listings l
        JOIN users u ON l.user_id = u.id
        LEFT JOIN meeting_points mp ON l.preferred_meeting_point_id = mp.id
        WHERE 1=1
    """
    params = []
    
    if query:
        sql += " AND (l.title LIKE ? OR l.author LIKE ? OR l.subject LIKE ? OR l.description LIKE ?)"
        wildcard = f"%{query}%"
        params.extend([wildcard, wildcard, wildcard, wildcard])
    
    if listing_type and listing_type != 'All':
        sql += " AND l.listing_type = ?"
        params.append(listing_type)
        
    if course and course != 'All':
        sql += " AND l.course = ?"
        params.append(course)
        
    if status and status != 'All':
        sql += " AND l.availability_status = ?"
        params.append(status)
        
    if meeting_point and meeting_point != 'All':
        sql += " AND l.preferred_meeting_point_id = ?"
        params.append(meeting_point)
        
    sql += " ORDER BY l.created_at DESC"
    
    listings = conn.execute(sql, params).fetchall()
    
    # Statistics for the dashboard banner
    stats = {
        'total': conn.execute("SELECT COUNT(*) FROM listings").fetchone()[0],
        'available': conn.execute("SELECT COUNT(*) FROM listings WHERE availability_status = 'Available'").fetchone()[0],
        'lending': conn.execute("SELECT COUNT(*) FROM listings WHERE listing_type = 'Lend'").fetchone()[0],
        'donations': conn.execute("SELECT COUNT(*) FROM listings WHERE listing_type = 'Donate'").fetchone()[0],
        'exchanges': conn.execute("SELECT COUNT(*) FROM listings WHERE listing_type = 'Exchange'").fetchone()[0]
    }
    
    meeting_points = conn.execute("SELECT * FROM meeting_points ORDER BY name").fetchall()
    courses = conn.execute("SELECT DISTINCT course FROM listings ORDER BY course").fetchall()
    
    conn.close()
    
    return render_template(
        'index.html',
        listings=listings,
        stats=stats,
        meeting_points=meeting_points,
        courses=courses,
        selected_q=query,
        selected_type=listing_type,
        selected_course=course,
        selected_status=status,
        selected_mp=meeting_point
    )

@app.route('/listing/<int:listing_id>')
def listing_detail(listing_id):
    """Detailed view for an individual learning material."""
    conn = get_db()
    listing = conn.execute("""
        SELECT l.*, u.full_name AS owner_name, u.email AS owner_email, u.contact_phone AS owner_phone,
               u.department AS owner_dept, u.course_year AS owner_year, u.enrollment_no AS owner_enrollment,
               mp.name AS meeting_point_name, mp.location_desc AS meeting_point_desc, mp.operating_hours AS meeting_point_hours
        FROM listings l
        JOIN users u ON l.user_id = u.id
        LEFT JOIN meeting_points mp ON l.preferred_meeting_point_id = mp.id
        WHERE l.id = ?
    """, (listing_id,)).fetchone()
    
    if not listing:
        conn.close()
        flash("The requested book listing could not be found.", "danger")
        return redirect(url_for('index'))
    
    # Check if the logged-in student has already requested this book
    existing_request = None
    if g.user:
        existing_request = conn.execute("""
            SELECT * FROM exchange_requests
            WHERE listing_id = ? AND requester_id = ?
            ORDER BY created_at DESC LIMIT 1
        """, (listing_id, g.user['id'])).fetchone()
        
    meeting_points = conn.execute("SELECT * FROM meeting_points ORDER BY name").fetchall()
    
    # Related books in the same subject or course
    related_books = conn.execute("""
        SELECT * FROM listings
        WHERE id != ? AND (subject = ? OR course = ?)
        LIMIT 3
    """, (listing_id, listing['subject'], listing['course'])).fetchall()
    
    conn.close()
    return render_template(
        'listing_detail.html',
        listing=listing,
        existing_request=existing_request,
        meeting_points=meeting_points,
        related_books=related_books
    )

# -------------------------------------------------------------
# Listing Management Routes (Create, Edit, Delete)
# -------------------------------------------------------------
@app.route('/listings/create', methods=['GET', 'POST'])
@login_required
def create_listing():
    """Allows students to post new books/notes for lending, exchange, or donation."""
    conn = get_db()
    meeting_points = conn.execute("SELECT * FROM meeting_points ORDER BY name").fetchall()
    
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        subject = request.form.get('subject', '').strip()
        course = request.form.get('course', 'MCA').strip()
        semester = request.form.get('semester', 'Semester 1').strip()
        listing_type = request.form.get('listing_type', 'Lend').strip()
        condition = request.form.get('condition', 'Good').strip()
        preferred_mp_id = request.form.get('preferred_meeting_point_id')
        description = request.form.get('description', '').strip()
        cover_image = request.form.get('cover_image', 'bi-book')
        
        # Validation
        if not title or not author or not subject:
            flash("Please fill in all mandatory fields (Title, Author, and Subject).", "danger")
            conn.close()
            return render_template('create_listing.html', meeting_points=meeting_points)
        
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO listings (
                user_id, title, author, subject, course, semester,
                listing_type, condition, availability_status, description,
                preferred_meeting_point_id, cover_image
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'Available', ?, ?, ?)
        """, (
            g.user['id'], title, author, subject, course, semester,
            listing_type, condition, description,
            preferred_mp_id if preferred_mp_id else None,
            cover_image
        ))
        conn.commit()
        new_id = cursor.lastrowid
        conn.close()
        
        flash(f"Success! '{title}' has been listed on the campus board.", "success")
        return redirect(url_for('listing_detail', listing_id=new_id))
        
    conn.close()
    return render_template('create_listing.html', meeting_points=meeting_points)

@app.route('/listings/<int:listing_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_listing(listing_id):
    """Allows owners to update their book's condition, description, and status."""
    conn = get_db()
    listing = conn.execute("SELECT * FROM listings WHERE id = ?", (listing_id,)).fetchone()
    
    if not listing:
        conn.close()
        flash("Listing not found.", "danger")
        return redirect(url_for('my_listings'))
        
    if listing['user_id'] != g.user['id']:
        conn.close()
        flash("Unauthorized: You can only edit your own listings.", "danger")
        return redirect(url_for('index'))
        
    meeting_points = conn.execute("SELECT * FROM meeting_points ORDER BY name").fetchall()
    
    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        author = request.form.get('author', '').strip()
        subject = request.form.get('subject', '').strip()
        course = request.form.get('course', '').strip()
        semester = request.form.get('semester', '').strip()
        listing_type = request.form.get('listing_type', '').strip()
        condition = request.form.get('condition', '').strip()
        availability_status = request.form.get('availability_status', 'Available').strip()
        preferred_mp_id = request.form.get('preferred_meeting_point_id')
        description = request.form.get('description', '').strip()
        
        conn.execute("""
            UPDATE listings
            SET title = ?, author = ?, subject = ?, course = ?, semester = ?,
                listing_type = ?, condition = ?, availability_status = ?,
                preferred_meeting_point_id = ?, description = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (
            title, author, subject, course, semester,
            listing_type, condition, availability_status,
            preferred_mp_id if preferred_mp_id else None,
            description, listing_id
        ))
        conn.commit()
        conn.close()
        
        flash("Listing updated successfully.", "success")
        return redirect(url_for('listing_detail', listing_id=listing_id))
        
    conn.close()
    return render_template('edit_listing.html', listing=listing, meeting_points=meeting_points)

@app.route('/listings/<int:listing_id>/delete', methods=['POST'])
@login_required
def delete_listing(listing_id):
    """Delete a listing owned by the current student."""
    conn = get_db()
    listing = conn.execute("SELECT * FROM listings WHERE id = ?", (listing_id,)).fetchone()
    
    if not listing or listing['user_id'] != g.user['id']:
        conn.close()
        flash("Action not permitted or listing does not exist.", "danger")
        return redirect(url_for('my_listings'))
        
    conn.execute("DELETE FROM listings WHERE id = ?", (listing_id,))
    conn.commit()
    conn.close()
    
    flash("The listing has been removed from BookBridge.", "info")
    return redirect(url_for('my_listings'))

# -------------------------------------------------------------
# Request-Interest Workflow Routes
# -------------------------------------------------------------
@app.route('/listing/<int:listing_id>/express-interest', methods=['POST'])
@login_required
def express_interest(listing_id):
    """Student submits an interest request to borrow, exchange, or receive a book."""
    conn = get_db()
    listing = conn.execute("SELECT * FROM listings WHERE id = ?", (listing_id,)).fetchone()
    
    if not listing:
        conn.close()
        flash("Listing not found.", "danger")
        return redirect(url_for('index'))
        
    if listing['user_id'] == g.user['id']:
        conn.close()
        flash("You cannot express interest in your own listing.", "warning")
        return redirect(url_for('listing_detail', listing_id=listing_id))
        
    message = request.form.get('message', '').strip()
    meeting_point_id = request.form.get('meeting_point_id')
    offered_exchange_item = request.form.get('offered_exchange_item', '').strip()
    proposed_duration = request.form.get('proposed_duration', '').strip()
    
    if not message:
        conn.close()
        flash("Please provide a brief message to the owner stating your requirement.", "danger")
        return redirect(url_for('listing_detail', listing_id=listing_id))
        
    conn.execute("""
        INSERT INTO exchange_requests (
            listing_id, requester_id, meeting_point_id, message,
            offered_exchange_item, proposed_duration, status
        ) VALUES (?, ?, ?, ?, ?, ?, 'Pending')
    """, (
        listing_id, g.user['id'],
        meeting_point_id if meeting_point_id else listing['preferred_meeting_point_id'],
        message,
        offered_exchange_item if offered_exchange_item else None,
        proposed_duration if proposed_duration else None
    ))
    conn.commit()
    conn.close()
    
    flash("Interest request submitted! The book owner will review and respond with handover coordination.", "success")
    return redirect(url_for('my_requests'))

@app.route('/requests/<int:request_id>/update', methods=['POST'])
@login_required
def update_request(request_id):
    """Listing owner accepts, declines, or completes an exchange request."""
    conn = get_db()
    req = conn.execute("""
        SELECT er.*, l.user_id AS owner_id, l.title AS book_title
        FROM exchange_requests er
        JOIN listings l ON er.listing_id = l.id
        WHERE er.id = ?
    """, (request_id,)).fetchone()
    
    if not req or req['owner_id'] != g.user['id']:
        conn.close()
        flash("Unauthorized action.", "danger")
        return redirect(url_for('my_requests'))
        
    new_status = request.form.get('status')
    owner_remarks = request.form.get('owner_remarks', '').strip()
    
    if new_status in ['Accepted', 'Declined', 'Completed']:
        conn.execute("""
            UPDATE exchange_requests
            SET status = ?, owner_remarks = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (new_status, owner_remarks, request_id))
        
        # Update parent listing availability status according to handover stage
        if new_status == 'Accepted':
            conn.execute("UPDATE listings SET availability_status = 'Pending Handover' WHERE id = ?", (req['listing_id'],))
        elif new_status == 'Completed':
            conn.execute("UPDATE listings SET availability_status = 'Completed' WHERE id = ?", (req['listing_id'],))
        elif new_status == 'Declined':
            # Check if there are other accepted requests on this book; if not, revert to Available
            active_accepted = conn.execute("""
                SELECT COUNT(*) FROM exchange_requests
                WHERE listing_id = ? AND status = 'Accepted' AND id != ?
            """, (req['listing_id'], request_id)).fetchone()[0]
            if active_accepted == 0:
                conn.execute("UPDATE listings SET availability_status = 'Available' WHERE id = ?", (req['listing_id'],))
                
        conn.commit()
        flash(f"Request marked as '{new_status}' for '{req['book_title']}'.", "success")
        
    conn.close()
    return redirect(url_for('my_requests'))

# -------------------------------------------------------------
# Student Dashboard Routes (My Listings & My Requests)
# -------------------------------------------------------------
@app.route('/dashboard/my-listings')
@login_required
def my_listings():
    """List of all books and study materials uploaded by the logged-in student."""
    conn = get_db()
    listings = conn.execute("""
        SELECT l.*, mp.name AS meeting_point_name,
               (SELECT COUNT(*) FROM exchange_requests WHERE listing_id = l.id) AS total_requests,
               (SELECT COUNT(*) FROM exchange_requests WHERE listing_id = l.id AND status = 'Pending') AS pending_requests
        FROM listings l
        LEFT JOIN meeting_points mp ON l.preferred_meeting_point_id = mp.id
        WHERE l.user_id = ?
        ORDER BY l.created_at DESC
    """, (g.user['id'],)).fetchall()
    conn.close()
    return render_template('my_listings.html', listings=listings)

@app.route('/dashboard/my-requests')
@login_required
def my_requests():
    """Hub for incoming handover requests (on my books) and outgoing requests (sent by me)."""
    conn = get_db()
    
    # 1. Incoming requests: Other students who want my books
    incoming = conn.execute("""
        SELECT er.*, l.title AS book_title, l.listing_type, l.availability_status,
               u.full_name AS requester_name, u.email AS requester_email, u.enrollment_no AS requester_enrollment,
               u.course_year AS requester_year, u.contact_phone AS requester_phone,
               mp.name AS meeting_point_name, mp.location_desc AS meeting_point_desc
        FROM exchange_requests er
        JOIN listings l ON er.listing_id = l.id
        JOIN users u ON er.requester_id = u.id
        LEFT JOIN meeting_points mp ON er.meeting_point_id = mp.id
        WHERE l.user_id = ?
        ORDER BY er.created_at DESC
    """, (g.user['id'],)).fetchall()
    
    # 2. Outgoing requests: Books I requested from fellow students
    outgoing = conn.execute("""
        SELECT er.*, l.title AS book_title, l.author AS book_author, l.listing_type,
               u.full_name AS owner_name, u.email AS owner_email, u.contact_phone AS owner_phone,
               u.course_year AS owner_year,
               mp.name AS meeting_point_name, mp.location_desc AS meeting_point_desc
        FROM exchange_requests er
        JOIN listings l ON er.listing_id = l.id
        JOIN users u ON l.user_id = u.id
        LEFT JOIN meeting_points mp ON er.meeting_point_id = mp.id
        WHERE er.requester_id = ?
        ORDER BY er.created_at DESC
    """, (g.user['id'],)).fetchall()
    
    conn.close()
    return render_template('my_requests.html', incoming=incoming, outgoing=outgoing)

# -------------------------------------------------------------
# Handover Guidelines & Safety Protocols
# -------------------------------------------------------------
@app.route('/guidelines')
def handover_guidelines():
    """Safe handover rules, daylight hours, approved campus spots, and verification tips."""
    conn = get_db()
    meeting_points = conn.execute("SELECT * FROM meeting_points ORDER BY name").fetchall()
    conn.close()
    return render_template('handover_guidelines.html', meeting_points=meeting_points)

# -------------------------------------------------------------
# Legacy Redirection Route
# -------------------------------------------------------------
@app.route('/about-project')
def about_project():
    """Redirects legacy about/viva route cleanly to the homepage."""
    return redirect(url_for('index'))

# -------------------------------------------------------------
# Authentication Routes (Register, Login, Quick Demo Switcher, Logout)
# -------------------------------------------------------------
@app.route('/register', methods=['GET', 'POST'])
def register():
    """Student registration with MCA Enrollment Number and College Email."""
    if g.user:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        enrollment = request.form.get('enrollment_no', '').strip()
        full_name = request.form.get('full_name', '').strip()
        email = request.form.get('email', '').strip().lower()
        password = request.form.get('password', '')
        department = request.form.get('department', 'Computer Applications').strip()
        course_year = request.form.get('course_year', 'MCA 1st Year').strip()
        phone = request.form.get('contact_phone', '').strip()
        
        if not enrollment or not full_name or not email or not password or not phone:
            flash("All fields marked with * are required.", "danger")
            return render_template('register.html')
            
        # Strict 10-digit Indian mobile number validation
        clean_phone = re.sub(r'\D', '', phone)
        if not re.match(r'^[6-9]\d{9}$', clean_phone):
            flash("Please enter a valid 10-digit mobile number starting with 6, 7, 8, or 9.", "danger")
            return render_template('register.html')
        phone = clean_phone
            
        conn = get_db()
        # Check if enrollment or email is already registered
        existing = conn.execute(
            "SELECT id FROM users WHERE enrollment_no = ? OR email = ?",
            (enrollment, email)
        ).fetchone()
        
        if existing:
            conn.close()
            flash("A student with this Enrollment Number or Email is already registered. Please log in.", "warning")
            return redirect(url_for('login'))
            
        hashed = generate_password_hash(password)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO users (enrollment_no, full_name, email, password_hash, department, course_year, contact_phone)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (enrollment, full_name, email, hashed, department, course_year, phone))
        conn.commit()
        user_id = cursor.lastrowid
        conn.close()
        
        session['user_id'] = user_id
        flash(f"Welcome to BookBridge, {full_name}! Your student account has been created.", "success")
        return redirect(url_for('index'))
        
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Student login via Enrollment Number or Email."""
    if g.user:
        return redirect(url_for('index'))
        
    if request.method == 'POST':
        identifier = request.form.get('identifier', '').strip()
        password = request.form.get('password', '')
        
        conn = get_db()
        user = conn.execute(
            "SELECT * FROM users WHERE enrollment_no = ? OR email = ?",
            (identifier, identifier.lower())
        ).fetchone()
        conn.close()
        
        if user and check_password_hash(user['password_hash'], password):
            session['user_id'] = user['id']
            flash(f"Welcome back, {user['full_name']}!", "success")
            next_url = request.args.get('next')
            return redirect(next_url or url_for('index'))
        else:
            flash("Invalid Enrollment Number / Email or Password. Please try again.", "danger")
            
    return render_template('login.html')

@app.route('/demo-login/<int:user_id>')
def demo_login(user_id):
    """Convenience route for project viva and teacher demonstration to switch student profiles with 1 click."""
    conn = get_db()
    user = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    conn.close()
    
    if user:
        session['user_id'] = user['id']
        flash(f"Switched active demo session to: {user['full_name']} ({user['course_year']})", "info")
    return redirect(request.referrer or url_for('index'))

@app.route('/logout')
def logout():
    """Clear session and log student out."""
    session.clear()
    flash("You have successfully signed out.", "info")
    return redirect(url_for('index'))

# -------------------------------------------------------------
# Main Application Runner (Production & Local Development Ready)
# -------------------------------------------------------------
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '0.0.0.0')
    debug = os.environ.get('FLASK_ENV') != 'production'
    print(f"Starting BookBridge VIPS Portal on http://{host}:{port} (debug={debug})")
    app.run(host=host, port=port, debug=debug)
