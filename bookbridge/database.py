"""
BookBridge - Database Module
Developed by Sanya (Enrollment No: 10517704426, MCA 1-B)
Project Mentor: Dr. Cosmena
Course: Master of Computer Applications
"""

import sqlite3
import os
from werkzeug.security import generate_password_hash

DB_PATH = os.path.join(os.path.dirname(__file__), 'bookbridge.db')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'schema.sql')

def get_db():
    """Returns a sqlite3 connection with Row factory enabled for dictionary-like access."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

def init_db(seed=True):
    """Initializes the database using schema.sql and optionally seeds sample data."""
    conn = get_db()
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        conn.executescript(f.read())
    conn.commit()
    
    if seed:
        seed_sample_data(conn)
    
    conn.close()
    print("Database initialized and sample records seeded successfully.")

def seed_sample_data(conn):
    """Populates realistic demo accounts, approved campus meeting points, and MCA textbooks."""
    cursor = conn.cursor()

    # 1. Seed Approved Campus Meeting Points (Vivekananda Institute of Professional Studies)
    meeting_points = [
        ("Central Library Foyer (A-Block)", "Ground Floor near Library Issue Desk. Well-lit, high visibility & CCTV monitored on VIPS campus.", "8:30 AM - 6:00 PM (Mon-Sat)", "Meet during daytime university library operating hours."),
        ("Student Activity Centre (SAC) Atrium", "C-Block Ground Floor atrium near student council notice board, VIPS.", "9:00 AM - 5:30 PM", "Well-lit common gathering zone with ample seating on campus."),
        ("VSIT Computer Lab 102 Corridor", "1st Floor, IT & Computer Applications Block B, VIPS.", "9:30 AM - 5:00 PM", "Ideal for MCA and CS branch peers during academic lab intervals."),
        ("Campus Cafeteria Courtyard", "Outdoor shaded seating area next to main VIPS canteen.", "10:00 AM - 4:30 PM", "Open public area with constant student presence."),
        ("VIPS Main Gate Reception Desk", "Visitors desk inside the main campus gate archway, VIPS Pitampura.", "8:00 AM - 7:00 PM", "Campus security personnel present at all times.")
    ]
    cursor.executemany("""
        INSERT INTO meeting_points (name, location_desc, operating_hours, safety_notes)
        VALUES (?, ?, ?, ?)
    """, meeting_points)

    # 2. Seed Verified VIPS Students
    # Password for all accounts is 'student123'
    default_pw_hash = generate_password_hash("student123")
    
    users = [
        ("10517704426", "Sanya Gupta", "sanya.mca@vips.edu", default_pw_hash, "Computer Applications", "MCA 1-B", "9876543210"),
        ("10517704412", "Rahul Sharma", "rahul.sharma@vips.edu", default_pw_hash, "Computer Applications", "MCA 1-A", "9811223344"),
        ("10517704435", "Priya Nair", "priya.nair@vips.edu", default_pw_hash, "Information Technology", "MCA 2nd Year", "9822334455"),
        ("10517704448", "Amit Verma", "amit.verma@vips.edu", default_pw_hash, "Computer Science & Engg", "B.Tech CS 3rd Year", "9833445566")
    ]
    cursor.executemany("""
        INSERT INTO users (enrollment_no, full_name, email, password_hash, department, course_year, contact_phone)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, users)

    # 3. Seed Realistic Learning Material Listings
    # user_ids will be 1 (Sanya), 2 (Rahul), 3 (Priya), 4 (Amit)
    listings = [
        (
            2, # Rahul
            "Database System Concepts (6th Edition)",
            "Abraham Silberschatz, Henry F. Korth, S. Sudarshan",
            "Database Management Systems",
            "MCA",
            "Semester 1",
            "Lend",
            "Good",
            "Available",
            "Core textbook for DBMS course. Covers ER modeling, Relational Algebra, SQL, Normalization (1NF to BCNF) and Transaction Processing. Light pencil marks in chapters 3 and 7.",
            1, # Central Library
            "bi-database"
        ),
        (
            1, # Sanya
            "Computer Networks (5th Edition)",
            "Andrew S. Tanenbaum, David J. Wetherall",
            "Computer Networks & Data Comm",
            "MCA",
            "Semester 1",
            "Exchange",
            "Like New",
            "Available",
            "Prescribed text for MCA 1st semester. Great reference for OSI 7-Layer model, TCP/IP, IP addressing, and routing algorithms. Looking to exchange with Discrete Mathematics by Rosen.",
            3, # MCA Lab 102
            "bi-diagram-3"
        ),
        (
            3, # Priya
            "Core Java: An Integrated Approach (Black Book)",
            "R. Nageswara Rao",
            "Object-Oriented Programming with Java",
            "MCA",
            "Semester 1",
            "Donate",
            "Good",
            "Available",
            "Passed MCA 1st year and donating this book to any incoming junior who needs it for Java lab practicals and OOP concepts. Contains solved programs.",
            2, # SAC
            "bi-code-slash"
        ),
        (
            4, # Amit
            "Introduction to Algorithms (CLRS 3rd Ed)",
            "Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, Clifford Stein",
            "Data Structures & Algorithms",
            "MCA",
            "Semester 1",
            "Lend",
            "Fair / Marked",
            "Available",
            "Standard reference for asymptotic notation, Divide & Conquer, Dynamic Programming, and Graph Algorithms (Dijkstra, Kruskal). Lending for 3-4 weeks until semester mid-terms.",
            1, # Central Library
            "bi-cpu"
        ),
        (
            1, # Sanya
            "Python Programming & MCA Lab Practical Manual (Printed)",
            "MCA Department Faculty & Sanya",
            "Programming in Python Lab",
            "MCA",
            "Semester 1",
            "Donate",
            "Annotated / Notes",
            "Available",
            "Spiral-bound clean printout of MCA Sem-1 Python lab syllabus exercises, flowcharts, solved code outputs, and exam practice questions. Free to any junior student.",
            3, # MCA Lab 102
            "bi-journal-code"
        ),
        (
            2, # Rahul
            "Operating System Concepts (9th Edition)",
            "Silberschatz, Galvin, Gagne",
            "Operating Systems",
            "MCA",
            "Semester 1",
            "Exchange",
            "Good",
            "Available",
            "Covers Process Synchronization, Semaphores, Deadlocks, Paging, and Virtual Memory. Would like to exchange for Software Engineering Pressman book.",
            4, # Cafeteria
            "bi-terminal"
        ),
        (
            3, # Priya
            "Discrete Mathematics and Its Applications (7th Edition)",
            "Kenneth H. Rosen",
            "Discrete Mathematical Structures",
            "MCA",
            "Semester 1",
            "Lend",
            "Like New",
            "Pending Handover",
            "Indispensable for Propositional Logic, Set Theory, Combinatorics, and Graph Theory. Lending for 2 weeks. Handover requested by Amit.",
            1, # Central Library
            "bi-calculator"
        ),
        (
            4, # Amit
            "Software Engineering: A Practitioner's Approach",
            "Roger S. Pressman",
            "Software Engineering & Agile Methodologies",
            "MCA",
            "Semester 2",
            "Donate",
            "Good",
            "Available",
            "Covers Waterfall, Agile, Scrum, SRS documentation, UML diagrams, and Black/White box testing. Donating to students starting their MCA 2nd semester.",
            2, # SAC
            "bi-layers"
        )
    ]

    cursor.executemany("""
        INSERT INTO listings (
            user_id, title, author, subject, course, semester,
            listing_type, condition, availability_status, description,
            preferred_meeting_point_id, cover_image
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, listings)

    # 4. Seed A Sample Request-Interest record to demonstrate the workflow
    # Amit (user 4) requested Discrete Math (listing 7 owned by Priya, user 3)
    cursor.execute("""
        INSERT INTO exchange_requests (
            listing_id, requester_id, meeting_point_id, message,
            offered_exchange_item, proposed_duration, status, owner_remarks
        ) VALUES (
            7, 4, 1,
            'Hi Priya, I need Rosen for Discrete Mathematics test preparation this upcoming Monday. Can I borrow it for 10 days?',
            NULL, '10 Days', 'Accepted',
            'Accepted! Let us meet tomorrow at 1:30 PM outside Central Library issue counter.'
        )
    """)

    conn.commit()

if __name__ == '__main__':
    init_db(seed=True)
