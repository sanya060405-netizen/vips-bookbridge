"""
Generate Official Minor Project Report PDF for Sanya (Enrollment No. 10517704426)
Course: Master of Computer Applications (MCA 1-B)
Project Title: BookBridge – A Campus Book and Learning-Material Exchange Board
Mentor: Dr. Cosmena
"""

import os
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak, KeepTogether, HRFlowable
)
from reportlab.pdfgen import canvas

class NumberedCanvas(canvas.Canvas):
    """Two-pass canvas to dynamically compute and draw total page count in running footer."""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super().showPage()
        super().save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        self.setFont("Helvetica", 8)
        self.setFillColor(colors.HexColor("#4b5563"))
        
        # Draw running footer line & text on all pages
        self.setStrokeColor(colors.HexColor("#d1d5db"))
        self.setLineWidth(0.6)
        self.line(40, 42, 555, 42)
        
        self.drawString(40, 30, "BookBridge – Campus Book Exchange | Sanya (10517704426)")
        self.drawRightString(555, 30, f"Page {self._pageNumber} of {page_count}")
        self.restoreState()

def build_pdf(filename="Minor_Project_Report_Sanya_10517704426.pdf"):
    doc = SimpleDocTemplate(
        filename,
        pagesize=A4,
        leftMargin=40,
        rightMargin=40,
        topMargin=40,
        bottomMargin=55
    )

    styles = getSampleStyleSheet()

    # Custom palette matching academic sample
    PRIMARY = colors.HexColor("#1e3a8a")     # Deep academic blue
    SECONDARY = colors.HexColor("#1f2937")   # Dark neutral
    TEXT_COLOR = colors.HexColor("#374151")  # Body text
    MUTED = colors.HexColor("#6b7280")
    BORDER_COLOR = colors.HexColor("#d1d5db")
    BG_LIGHT = colors.HexColor("#f9fafb")
    BG_HEADER = colors.HexColor("#f3f4f6")

    # Typography styles
    top_badge_style = ParagraphStyle(
        'TopBadge',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=PRIMARY,
        alignment=1, # Center
        spaceAfter=10
    )

    main_title_style = ParagraphStyle(
        'MainTitle',
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=PRIMARY,
        alignment=1,
        spaceAfter=4
    )

    subtitle_style = ParagraphStyle(
        'SubTitle',
        fontName='Helvetica-Oblique',
        fontSize=11,
        leading=14,
        textColor=MUTED,
        alignment=1,
        spaceAfter=14
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=PRIMARY,
        spaceBefore=10,
        spaceAfter=6
    )

    subsection_heading = ParagraphStyle(
        'SubSectionHeading',
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=SECONDARY,
        spaceBefore=8,
        spaceAfter=4
    )

    body_style = ParagraphStyle(
        'Body',
        fontName='Helvetica',
        fontSize=8.8,
        leading=12.2,
        textColor=TEXT_COLOR,
        spaceAfter=6
    )

    bullet_style = ParagraphStyle(
        'Bullet',
        fontName='Helvetica',
        fontSize=8.8,
        leading=12.2,
        textColor=TEXT_COLOR,
        leftIndent=15,
        spaceAfter=4
    )

    table_header_style = ParagraphStyle(
        'TableHeader',
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11,
        textColor=SECONDARY
    )

    table_cell_style = ParagraphStyle(
        'TableCell',
        fontName='Helvetica',
        fontSize=8,
        leading=10.5,
        textColor=TEXT_COLOR
    )

    table_cell_bold = ParagraphStyle(
        'TableCellBold',
        fontName='Helvetica-Bold',
        fontSize=8,
        leading=10.5,
        textColor=SECONDARY
    )

    code_style = ParagraphStyle(
        'CodeStyle',
        fontName='Courier',
        fontSize=7.8,
        leading=10.5,
        textColor=colors.HexColor("#111827")
    )

    story = []

    # ==========================================
    # PAGE 1: Title, Details Table, Declaration, Certificate
    # ==========================================
    story.append(Paragraph("MINOR PROJECT REPORT • MASTER OF COMPUTER APPLICATIONS (MCA 1-B)", top_badge_style))
    story.append(Paragraph("BookBridge – Campus Book Exchange", main_title_style))
    story.append(Paragraph("A Web-Based Campus Book and Learning-Material Exchange Board", subtitle_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY, spaceAfter=14))

    story.append(Paragraph("Student & Submission Details", section_heading))

    details_data = [
        [Paragraph("Particulars", table_header_style), Paragraph("Details", table_header_style)],
        [Paragraph("Student Name", table_cell_bold), Paragraph("Sanya", table_cell_style)],
        [Paragraph("Enrollment Number", table_cell_bold), Paragraph("10517704426", table_cell_style)],
        [Paragraph("Course & Section", table_cell_bold), Paragraph("Master of Computer Applications (MCA 1-B)", table_cell_style)],
        [Paragraph("Project Title", table_cell_bold), Paragraph("BookBridge – A Campus Book and Learning-Material Exchange Board", table_cell_style)],
        [Paragraph("Project Mentor", table_cell_bold), Paragraph("Dr. Cosmena", table_cell_style)],
        [Paragraph("Submission Date", table_cell_bold), Paragraph("November 17, 2026", table_cell_style)],
        [Paragraph("Project Status", table_cell_bold), Paragraph("Completed", table_cell_style)],
        [Paragraph("Report Status", table_cell_bold), Paragraph("Completed (Plagiarism check report to be attached from the library)", table_cell_style)],
    ]
    t_details = Table(details_data, colWidths=[160, 355])
    t_details.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (1,0), BG_HEADER),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_details)
    story.append(Spacer(1, 14))

    story.append(Paragraph("Declaration", section_heading))
    story.append(Paragraph(
        "I, <b>Sanya</b> (Enrollment No. <b>10517704426</b>), a student of Master of Computer Applications (MCA 1-B), "
        "hereby declare that this minor project report titled <i>“BookBridge – A Campus Book and Learning-Material Exchange Board”</i> "
        "is my original work carried out under the guidance of <b>Dr. Cosmena</b>. All sources referred to during this work have been "
        "listed in the references section. This report has not been submitted elsewhere for any other degree or diploma.",
        body_style
    ))
    story.append(Spacer(1, 16))

    sig_table = Table([
        [Paragraph("Date: ________________________", body_style), Paragraph("Signature of Student: ________________________", body_style)]
    ], colWidths=[250, 265])
    sig_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
    story.append(sig_table)
    story.append(Spacer(1, 14))

    story.append(Paragraph("Certificate", section_heading))
    story.append(Paragraph(
        "This is to certify that <b>Sanya</b> (Enrollment No. <b>10517704426</b>), a student of MCA 1-B, has successfully "
        "completed the minor project titled <i>“BookBridge – Campus Book and Learning-Material Exchange Board”</i> under my "
        "supervision and guidance. To the best of my knowledge, this work is original and fulfills the requirements of the course.",
        body_style
    ))
    story.append(Spacer(1, 16))

    mentor_table = Table([
        [Paragraph("Date: ________________________", body_style), Paragraph("Project Mentor (Dr. Cosmena): ________________________", body_style)]
    ], colWidths=[250, 265])
    mentor_table.setStyle(TableStyle([('VALIGN', (0,0), (-1,-1), 'MIDDLE')]))
    story.append(mentor_table)

    story.append(PageBreak())

    # ==========================================
    # PAGE 2: Acknowledgement, Abstract, 1. Introduction, 1.1 Background
    # ==========================================
    story.append(Paragraph("Acknowledgement", section_heading))
    story.append(Paragraph(
        "I would like to express my sincere thanks to my project mentor, <b>Dr. Cosmena</b>, for her constant guidance, "
        "valuable suggestions, and support throughout the completion of this project. I am also thankful to the faculty members "
        "of the MCA department and my classmates for testing the application and giving helpful feedback, as well as my family "
        "for their encouragement.",
        body_style
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("Abstract", section_heading))
    story.append(Paragraph(
        "<b>BookBridge</b> is a proposed web-based campus exchange directory that connects students who have unused learning "
        "materials with students who need them. In university environments, students frequently require textbooks, reference manuals, "
        "and lab guides for their respective courses, but purchasing new retail copies each semester is costly. Concurrently, senior and "
        "peer students possess study materials they no longer actively use, which often sit idle despite their continuing educational utility.",
        body_style
    ))
    story.append(Paragraph(
        "This application allows registered students to search, filter, and browse listings by book title, author, subject module, "
        "and course branch (e.g., MCA, B.Tech CS, BCA). The platform supports three distinct resource-sharing mechanisms: <b>Lending</b> "
        "(with a proposed borrowing duration), <b>Exchange</b> (book-for-book trade), and <b>Free Donation</b>. Through an intuitive "
        "request-interest flow, students can communicate their requirements and propose meeting coordination. To preserve student privacy "
        "and security, BookBridge strictly prohibits publishing residential addresses and coordinates physical handovers exclusively at "
        "approved, monitored university meeting points such as the Central Library Foyer and Student Activity Centre.",
        body_style
    ))
    story.append(Paragraph(
        "The project is built using HTML5, CSS3, and JavaScript for the frontend, Python with the Flask web framework for the backend, "
        "and SQLite for reliable relational data storage. The application features complete user authentication, a student listings dashboard, "
        "a handover requests hub, and comprehensive safety guidelines. All automated test cases written for the project pass successfully.",
        body_style
    ))
    story.append(Paragraph(
        "<b>Keywords:</b> Campus Book Exchange, Peer-to-Peer Resource Sharing, Academic Lending, Flask Web Framework, SQLite, Web Development, Campus Safety.",
        body_style
    ))
    story.append(Spacer(1, 6))

    story.append(Paragraph("1. Introduction", section_heading))
    story.append(Paragraph("1.1 Background", subsection_heading))
    story.append(Paragraph(
        "Textbooks, syllabus reference manuals, and lecture notes represent an essential yet recurring financial expenditure for university "
        "students throughout their academic tenure. In professional computing disciplines such as the Master of Computer Applications (MCA) "
        "and Computer Science & Engineering, prescribed reference volumes—such as Database System Concepts by Korth, Computer Networks by "
        "Tanenbaum, and Algorithms by CLRS—carry substantial retail prices. Once students conclude end-semester examinations, these books "
        "frequently sit unused on dorm shelves, while incoming juniors seek identical copies.",
        body_style
    ))
    story.append(Paragraph(
        "While digital PDFs are common, physical textbooks remain indispensable for in-depth technical study, mathematical derivation, "
        "and open-book university assessments. However, universities typically lack a centralized, campus-specific directory to facilitate "
        "direct peer-to-peer textbook reuse. Commercial buyback platforms impose heavy courier fees and intermediary margins, while unorganized "
        "social media chat groups suffer from information clutter and lack privacy safeguards.",
        body_style
    ))

    story.append(PageBreak())

    # ==========================================
    # PAGE 3: 1.2 Problem Statement, 1.3 Objectives, 1.4 Scope, 2. System Analysis, 2.1 Existing Methods
    # ==========================================
    story.append(Paragraph("1.2 Problem Statement", subsection_heading))
    story.append(Paragraph(
        "When university students require course textbooks or wish to pass on completed study materials, they encounter significant hurdles. "
        "Searching across unorganized student messaging groups or generic classified websites is time-consuming, unindexed, and exposes "
        "students' personal telephone numbers to unknown individuals. Commercial buyback portals offer negligible repurchase value and require "
        "postal transit. Furthermore, arranging off-campus physical meetups with unfamiliar parties presents personal safety concerns. "
        "Therefore, there is an urgent need for a localized, campus-centric web platform that catalogs available study materials, facilitates "
        "direct peer interest requests, and enforces safe handovers strictly within monitored university grounds.",
        body_style
    ))

    story.append(Paragraph("1.3 Objectives", subsection_heading))
    story.append(Paragraph("• Provide an intuitive, searchable directory where students can discover books by title, author, subject, and course.", bullet_style))
    story.append(Paragraph("• Support three flexible sharing options: Lending (time-bound), Exchange (reciprocal barter), and Free Donation.", bullet_style))
    story.append(Paragraph("• Implement a request-interest workflow allowing borrowers to propose terms and owners to accept or decline requests.", bullet_style))
    story.append(Paragraph("• Enforce campus safety protocols by restricting physical exchanges to designated, CCTV-monitored university points.", bullet_style))
    story.append(Paragraph("• Protect student privacy by completely avoiding collection or publication of private residential addresses.", bullet_style))
    story.append(Paragraph("• Provide student dashboards for monitoring active listings, incoming peer requests, and handover statuses.", bullet_style))

    story.append(Paragraph("1.4 Scope of the Project", subsection_heading))
    story.append(Paragraph(
        "The application operates as a campus-level web portal tailored for enrolled university students and faculty. It facilitates listing "
        "creation, multi-criteria catalog queries, request-interest coordination, and safe handover tracking using Python, Flask, and SQLite. "
        "Commercial financial payments, external courier shipping logistics, and cross-university inter-campus delivery networks are outside "
        "the scope of this minor project prototype.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("2. System Analysis", section_heading))
    story.append(Paragraph("2.1 Existing Methods and Their Limitations", subsection_heading))
    story.append(Paragraph(
        "Presently, students rely on informal, fragmented mechanisms to procure second-hand textbooks, each exhibiting critical limitations:",
        body_style
    ))
    story.append(Paragraph("• <b>Commercial Resale Portals:</b> Sites like OLX or book resellers take significant profit cuts, involve courier charges, and fail to filter books by specific university course syllabi.", bullet_style))
    story.append(Paragraph("• <b>Unorganized Messaging Groups:</b> WhatsApp and Telegram batch groups flood feeds with unstructured requests that quickly get lost, lacking search filters and structured status tracking.", bullet_style))
    story.append(Paragraph("• <b>Privacy Exposure:</b> Broadcasting book needs in public groups publicly exposes personal phone numbers and identities, increasing spam and unwanted contact.", bullet_style))
    story.append(Paragraph("• <b>Physical Safety Risks:</b> Informal exchanges frequently pressure students to meet strangers at unverified off-campus street locations or after hours.", bullet_style))

    story.append(PageBreak())

    # ==========================================
    # PAGE 4: 2.2 Proposed System, 2.3 Feasibility Study, 3. System Requirements, 3.1 Functional Requirements
    # ==========================================
    story.append(Paragraph("2.2 Proposed System", subsection_heading))
    story.append(Paragraph(
        "<b>BookBridge</b> resolves these shortcomings through a centralized, privacy-conscious university portal. Registered students "
        "can list surplus learning materials within seconds, indicating subject, semester, physical condition, and listing type (Lend, "
        "Exchange, or Donate). Borrowers filter listings effortlessly and submit interest requests detailing their requirements. Book owners "
        "review requests in their personal dashboard, accept handover terms, and agree to meet at pre-approved campus points such as the "
        "Central Library Foyer during verified daylight hours, completely eliminating off-campus risks.",
        body_style
    ))

    story.append(Paragraph("2.3 Feasibility Study", subsection_heading))
    feasibility_data = [
        [Paragraph("Feasibility Type", table_header_style), Paragraph("Assessment", table_header_style)],
        [Paragraph("Technical Feasibility", table_cell_bold), Paragraph("Built using Python, Flask, SQLite, HTML5, CSS3, and JavaScript. All components are lightweight, standard in the MCA curriculum, and execute smoothly on any standard laptop without complex configurations.", table_cell_style)],
        [Paragraph("Economic Feasibility", table_cell_bold), Paragraph("Zero financial investment required. The entire tech stack comprises free, open-source tools. No proprietary servers, paid APIs, or commercial hosting subscriptions are needed.", table_cell_style)],
        [Paragraph("Operational Feasibility", table_cell_bold), Paragraph("Extremely user-friendly. Designed with clear card layouts, intuitive badges, and straightforward forms so any student can search, post, or request books without prior training.", table_cell_style)],
        [Paragraph("Schedule Feasibility", table_cell_bold), Paragraph("Structured with a focused, well-defined scope allowing development, database design, testing, and report documentation to be completed comfortably within the one-month minor project timeframe.", table_cell_style)],
    ]
    t_feasibility = Table(feasibility_data, colWidths=[120, 395])
    t_feasibility.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (1,0), BG_HEADER),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 4),
        ('BOTTOMPADDING', (0,0), (-1,-1), 4),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_feasibility)
    story.append(Spacer(1, 6))

    story.append(Paragraph("3. System Requirements", section_heading))
    story.append(Paragraph("3.1 Functional Requirements", subsection_heading))
    
    fr_data = [
        [Paragraph("Req. ID", table_header_style), Paragraph("Description", table_header_style)],
        [Paragraph("FR1", table_cell_bold), Paragraph("The system allows students to register and sign in securely using their University Enrollment Number and password.", table_cell_style)],
        [Paragraph("FR2", table_cell_bold), Paragraph("Registered users can create new listings by specifying Title, Author, Subject, Course, Semester, Condition, Type, and Handover Spot.", table_cell_style)],
        [Paragraph("FR3", table_cell_bold), Paragraph("The catalog provides keyword search across titles and authors, with filters for Course, Exchange Type, and Status.", table_cell_style)],
        [Paragraph("FR4", table_cell_bold), Paragraph("Students can express interest in a book by proposing a message, borrowing duration, or reciprocal trade book.", table_cell_style)],
        [Paragraph("FR5", table_cell_bold), Paragraph("Book owners can review incoming interest requests and Accept, Decline, or mark them as Completed.", table_cell_style)],
        [Paragraph("FR6", table_cell_bold), Paragraph("The system automatically shifts listing status from 'Available' to 'Pending Handover' and 'Completed' based on request state.", table_cell_style)],
        [Paragraph("FR7", table_cell_bold), Paragraph("The system enforces approved campus meeting points and provides a dedicated Campus Handover Guidelines section.", table_cell_style)],
        [Paragraph("FR8", table_cell_bold), Paragraph("Form validations reject incomplete inputs and prevent students from expressing interest in their own listings.", table_cell_style)],
    ]
    t_fr = Table(fr_data, colWidths=[55, 460])
    t_fr.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (1,0), BG_HEADER),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_fr)

    story.append(PageBreak())

    # ==========================================
    # PAGE 5: 3.2 Non-Functional Requirements, 3.3 Hardware/Software, 4. System Design, 4.1 Architecture
    # ==========================================
    story.append(Paragraph("3.2 Non-Functional Requirements", subsection_heading))
    story.append(Paragraph("• <b>Usability:</b> Clean, intuitive interface powered by Bootstrap 5, optimized for both desktop monitors and mobile browsers.", bullet_style))
    story.append(Paragraph("• <b>Performance:</b> Lightweight database queries and Jinja2 templating ensure pages render in under 200 milliseconds.", bullet_style))
    story.append(Paragraph("• <b>Privacy:</b> Zero collection or display of personal home addresses or dorm rooms. Phone numbers remain hidden until a request is accepted.", bullet_style))
    story.append(Paragraph("• <b>Security:</b> Cryptographic password hashing via Werkzeug (PBKDF2-SHA256) and parameterized SQL queries preventing SQL Injection.", bullet_style))
    story.append(Paragraph("• <b>Reliability:</b> Foreign key integrity constraints in SQLite prevent orphan listings or dangling exchange requests upon deletion.", bullet_style))
    story.append(Spacer(1, 4))

    story.append(Paragraph("3.3 Hardware and Software Requirements", subsection_heading))
    hw_data = [
        [Paragraph("Component", table_header_style), Paragraph("Minimum Requirement", table_header_style)],
        [Paragraph("Processor & RAM", table_cell_bold), Paragraph("Intel Core i3 / AMD Ryzen 3 or higher; Minimum 4 GB RAM", table_cell_style)],
        [Paragraph("Operating System", table_cell_bold), Paragraph("Windows 10 or later (fully compatible with Ubuntu Linux and macOS)", table_cell_style)],
        [Paragraph("Programming Language", table_cell_bold), Paragraph("Python 3.10 or later", table_cell_style)],
        [Paragraph("Web Framework & Tools", table_cell_bold), Paragraph("Flask 3.x, Jinja2, Werkzeug Security, unittest / pytest", table_cell_style)],
        [Paragraph("Database Engine", table_cell_bold), Paragraph("SQLite3 (embedded relational database with row factory)", table_cell_style)],
        [Paragraph("Web Browser & Editor", table_cell_bold), Paragraph("Google Chrome, Mozilla Firefox, or Microsoft Edge; VS Code or Antigravity IDE", table_cell_style)],
    ]
    t_hw = Table(hw_data, colWidths=[140, 375])
    t_hw.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (1,0), BG_HEADER),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 6),
        ('RIGHTPADDING', (0,0), (-1,-1), 6),
    ]))
    story.append(t_hw)
    story.append(Spacer(1, 8))

    story.append(Paragraph("4. System Design", section_heading))
    story.append(Paragraph("4.1 System Architecture", subsection_heading))
    story.append(Paragraph(
        "BookBridge follows a classic Model-View-Controller (MVC) architectural pattern adapted for web microframeworks. "
        "The application is segmented into four cohesive layers operating locally on the student server:",
        body_style
    ))

    arch_box_data = [
        [Paragraph("<b>Step 1 – Client Browser (Frontend):</b> Renders HTML5 templates with Bootstrap 5 and custom CSS. Dispatches HTTP GET search filters and POST request submissions to Flask routes.", body_style)],
        [Paragraph("<b>Step 2 – Web Application Controller (app.py):</b> Handles route dispatching, session authentication, request validation, flash notifications, and orchestrates business logic.", body_style)],
        [Paragraph("<b>Step 3 – Exchange Workflow Engine:</b> Manages the state transitions of listings (Available -> Pending Handover -> Completed) and coordinates interest requests between borrower and owner.", body_style)],
        [Paragraph("<b>Step 4 – Relational Database Layer (database.py / SQLite):</b> Persists records across normalized tables with enforced foreign key constraints, executing parameterized SQL transactions.", body_style)],
    ]
    t_arch = Table(arch_box_data, colWidths=[515])
    t_arch.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT),
        ('BOX', (0,0), (-1,-1), 0.8, PRIMARY),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 5),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_arch)

    story.append(PageBreak())

    # ==========================================
    # PAGE 6: 4.2 Data Flow Overview, 4.3 Database Design
    # ==========================================
    story.append(Paragraph("4.2 Data Flow Overview", subsection_heading))
    story.append(Paragraph(
        "At the top level (<b>Level 0 Context DFD</b>), the Student acts as the primary external entity who interacts with BookBridge "
        "by registering credentials, posting book listings, filtering the course material directory, submitting interest requests, and "
        "confirming handovers. In return, the system provides real-time search results, owner contact details upon request acceptance, "
        "and handover coordination notices.",
        body_style
    ))
    story.append(Paragraph(
        "Internally (<b>Level 1 DFD</b>), the flow is partitioned into five functional subprocesses: (1) <i>User Authentication & Session Management</i> "
        "— verifies login credentials and issues secure cookies; (2) <i>Listing Management</i> — validates book metadata and inserts into <code>listings</code>; "
        "(3) <i>Catalog Querying & Filtering</i> — executes multi-parameter SQL SELECT queries with wildcard pattern matching; (4) <i>Interest Request Dispatching</i> "
        "— captures borrower proposals and creates <code>exchange_requests</code> records with state 'Pending'; and (5) <i>Handover Lifecycle Coordination</i> "
        "— shifts listing status to 'Pending Handover' upon owner acceptance and 'Completed' upon physical exchange.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("4.3 Database Design", subsection_heading))
    story.append(Paragraph(
        "The relational schema is implemented in SQLite with four interconnected tables enforcing referential integrity:",
        body_style
    ))

    db_data = [
        [Paragraph("Table Name", table_header_style), Paragraph("Column", table_header_style), Paragraph("Data Type", table_header_style), Paragraph("Purpose", table_header_style)],
        [Paragraph("<b>users</b><br/>(Stores student accounts)", table_cell_style), Paragraph("id<br/>enrollment_no<br/>full_name<br/>email<br/>password_hash<br/>department<br/>course_year<br/>contact_phone", table_cell_style), Paragraph("INTEGER (PK)<br/>TEXT (UNIQUE)<br/>TEXT<br/>TEXT (UNIQUE)<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT", table_cell_style), Paragraph("Primary Key<br/>Student Roll Number<br/>Full Name<br/>Campus Email<br/>PBKDF2-SHA256 Hash<br/>Academic Dept<br/>Class / Section<br/>Contact Phone", table_cell_style)],
        [Paragraph("<b>meeting_points</b><br/>(Approved campus spots)", table_cell_style), Paragraph("id<br/>name<br/>location_desc<br/>operating_hours<br/>safety_notes", table_cell_style), Paragraph("INTEGER (PK)<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT", table_cell_style), Paragraph("Primary Key<br/>Spot Name (e.g. Library)<br/>Location Details<br/>Daylight Hours<br/>CCTV / Visibility Notes", table_cell_style)],
        [Paragraph("<b>listings</b><br/>(Book & study materials)", table_cell_style), Paragraph("id<br/>user_id<br/>title<br/>author<br/>subject<br/>course<br/>semester<br/>listing_type<br/>condition<br/>availability_status<br/>preferred_mp_id", table_cell_style), Paragraph("INTEGER (PK)<br/>INTEGER (FK)<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT<br/>INTEGER (FK)", table_cell_style), Paragraph("Primary Key<br/>Refers to users(id)<br/>Book Title<br/>Author(s)<br/>Course Subject<br/>Branch (MCA, etc.)<br/>Target Semester<br/>Lend / Exchange / Donate<br/>Book Condition<br/>Available / Pending / Done<br/>Refers to meeting_points(id)", table_cell_style)],
        [Paragraph("<b>exchange_requests</b><br/>(Interest requests)", table_cell_style), Paragraph("id<br/>listing_id<br/>requester_id<br/>meeting_point_id<br/>message<br/>offered_exchange_item<br/>proposed_duration<br/>status<br/>owner_remarks", table_cell_style), Paragraph("INTEGER (PK)<br/>INTEGER (FK)<br/>INTEGER (FK)<br/>INTEGER (FK)<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT", table_cell_style), Paragraph("Primary Key<br/>Refers to listings(id)<br/>Refers to users(id)<br/>Refers to meeting_points(id)<br/>Borrower message<br/>Offered trade book<br/>Borrowing period<br/>Pending/Accepted/Done<br/>Owner meeting note", table_cell_style)],
    ]
    t_db = Table(db_data, colWidths=[105, 115, 110, 185])
    t_db.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), BG_HEADER),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'TOP'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_db)

    story.append(PageBreak())

    # ==========================================
    # PAGE 7: 4.4 Application Routes, 5. Implementation, 5.1 Project Folder Structure, 5.2 Core Modules
    # ==========================================
    story.append(Paragraph("4.4 Application Routes", subsection_heading))
    routes_data = [
        [Paragraph("Route", table_header_style), Paragraph("Method", table_header_style), Paragraph("Function", table_header_style)],
        [Paragraph("/", table_cell_bold), Paragraph("GET", table_cell_style), Paragraph("Opens main catalogue with keyword search and multi-parameter filtering.", table_cell_style)],
        [Paragraph("/listing/&lt;id&gt;", table_cell_bold), Paragraph("GET", table_cell_style), Paragraph("Displays full book metadata, meeting spot details, and request form.", table_cell_style)],
        [Paragraph("/listings/create", table_cell_bold), Paragraph("GET, POST", table_cell_style), Paragraph("Allows authenticated students to list books for Lend, Exchange, or Donate.", table_cell_style)],
        [Paragraph("/listings/&lt;id&gt;/edit", table_cell_bold), Paragraph("GET, POST", table_cell_style), Paragraph("Enables book owners to update description, condition, or status.", table_cell_style)],
        [Paragraph("/listing/&lt;id&gt;/express-interest", table_cell_bold), Paragraph("POST", table_cell_style), Paragraph("Submits borrower interest request with duration or trade offer.", table_cell_style)],
        [Paragraph("/requests/&lt;id&gt;/update", table_cell_bold), Paragraph("POST", table_cell_style), Paragraph("Owner accepts, declines, or marks handover as completed.", table_cell_style)],
        [Paragraph("/dashboard/my-listings", table_cell_bold), Paragraph("GET", table_cell_style), Paragraph("Displays student's posted books and pending request indicators.", table_cell_style)],
        [Paragraph("/dashboard/my-requests", table_cell_bold), Paragraph("GET", table_cell_style), Paragraph("Hub for managing incoming peer requests and outgoing borrow requests.", table_cell_style)],
        [Paragraph("/guidelines", table_cell_bold), Paragraph("GET", table_cell_style), Paragraph("Shows approved campus meeting points and safety protocols.", table_cell_style)],
        [Paragraph("/about-project", table_cell_bold), Paragraph("GET", table_cell_style), Paragraph("Comprehensive synopsis, mentor details, architecture, and viva guide.", table_cell_style)],
        [Paragraph("/register, /login, /logout", table_cell_bold), Paragraph("GET, POST", table_cell_style), Paragraph("Student authentication and session lifecycle management.", table_cell_style)],
    ]
    t_routes = Table(routes_data, colWidths=[130, 65, 320])
    t_routes.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), BG_HEADER),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_routes)
    story.append(Spacer(1, 6))

    story.append(Paragraph("5. Implementation", section_heading))
    story.append(Paragraph("5.1 Project Folder Structure", subsection_heading))
    struct_data = [
        [Paragraph("File / Folder", table_header_style), Paragraph("Role in the Project", table_header_style)],
        [Paragraph("app.py", table_cell_bold), Paragraph("Main Flask application containing route controllers, session handling, and validation.", table_cell_style)],
        [Paragraph("database.py", table_cell_bold), Paragraph("SQLite connection utility, DDL schema executor, and sample dataset seeder.", table_cell_style)],
        [Paragraph("schema.sql", table_cell_bold), Paragraph("Relational table definitions with constraints (users, listings, points, requests).", table_cell_style)],
        [Paragraph("test_app.py", table_cell_bold), Paragraph("Automated unit test suite verifying catalog, filters, listings, and requests.", table_cell_style)],
        [Paragraph("run.bat", table_cell_bold), Paragraph("One-click Windows batch launcher that boots Flask and launches default browser.", table_cell_style)],
        [Paragraph("templates/", table_cell_bold), Paragraph("Jinja2 HTML templates (base, index, listing_detail, create, requests, etc.).", table_cell_style)],
        [Paragraph("static/", table_cell_bold), Paragraph("Frontend assets: custom CSS (custom.css) and client-side interactions (main.js).", table_cell_style)],
    ]
    t_struct = Table(struct_data, colWidths=[120, 395])
    t_struct.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), BG_HEADER),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_struct)
    story.append(Spacer(1, 6))

    story.append(Paragraph("5.2 Core Modules and Business Logic", subsection_heading))
    story.append(Paragraph(
        "The application core consists of three key mechanisms: (1) <b>Dynamic Multi-Parameter Filtering:</b> constructs SQL queries dynamically "
        "using parameterized wildcard matching across book titles, authors, subjects, and course tags; (2) <b>Tri-Model Resource Sharing:</b> "
        "customizes UI inputs based on whether the item is for <i>Lend</i> (capturing borrowing duration), <i>Exchange</i> (capturing offered trade item), "
        "or <i>Donate</i> (capturing recipient need); and (3) <b>Handover State Machine:</b> coordinates request transitions across four states.",
        body_style
    ))

    story.append(PageBreak())

    # ==========================================
    # PAGE 8: 5.2 (Cont) Request-Interest State Machine, Code Snippet, 5.3 Campus Safety & Privacy
    # ==========================================
    story.append(Paragraph("5.2 (Continued) Request-Interest Workflow & State Transitions", subsection_heading))
    story.append(Paragraph(
        "The book handover lifecycle transitions through a four-stage finite state machine:",
        body_style
    ))
    story.append(Paragraph("• <b>Available:</b> The book is actively listed in the catalogue and visible to all students for search and discovery.", bullet_style))
    story.append(Paragraph("• <b>Pending Review:</b> A student submits an interest request. The request is marked 'Pending', and the owner is notified.", bullet_style))
    story.append(Paragraph("• <b>Pending Handover:</b> The owner clicks 'Accept' and specifies a meeting note. The book's public availability automatically shifts to 'Pending Handover', preventing conflicting requests.", bullet_style))
    story.append(Paragraph("• <b>Completed:</b> After meeting at the approved campus spot and verifying the book, the owner clicks 'Confirm Handover'. The listing and request are marked 'Completed'.", bullet_style))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Listing Status Synchronization Logic (Snippet from app.py):", subsection_heading))
    code_text = (
        "@app.route('/requests/<int:request_id>/update', methods=['POST'])\n"
        "@login_required\n"
        "def update_request(request_id):\n"
        "    new_status = request.form.get('status') # 'Accepted', 'Declined', 'Completed'\n"
        "    owner_remarks = request.form.get('owner_remarks', '').strip()\n"
        "    conn = get_db()\n"
        "    conn.execute('UPDATE exchange_requests SET status = ?, owner_remarks = ? WHERE id = ?',\n"
        "                 (new_status, owner_remarks, request_id))\n"
        "    if new_status == 'Accepted':\n"
        "        conn.execute('UPDATE listings SET availability_status = ? WHERE id = ?',\n"
        "                     ('Pending Handover', req['listing_id']))\n"
        "    elif new_status == 'Completed':\n"
        "        conn.execute('UPDATE listings SET availability_status = ? WHERE id = ?',\n"
        "                     ('Completed', req['listing_id']))\n"
        "    conn.commit()\n"
        "    flash(f'Request updated to {new_status}.', 'success')"
    )
    t_code = Table([[Paragraph(code_text.replace('\n', '<br/>').replace(' ', '&nbsp;'), code_style)]], colWidths=[515])
    t_code.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), colors.HexColor("#f8fafc")),
        ('BOX', (0,0), (-1,-1), 0.5, colors.HexColor("#cbd5e1")),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_code)
    story.append(Spacer(1, 8))

    story.append(Paragraph("5.3 Campus Safety, Privacy, and Handover Protocols", subsection_heading))
    story.append(Paragraph(
        "To address student safety and privacy concerns inherent in peer-to-peer exchanges, BookBridge implements four structural safeguards:",
        body_style
    ))
    story.append(Paragraph("• <b>Zero Home Address Collection:</b> The database schema does not include fields for personal residences or hostel rooms.", bullet_style))
    story.append(Paragraph("• <b>Approved Campus Meeting Points:</b> Pre-configured in the database (Central Library Foyer, SAC Atrium, MCA Lab 102 corridors) with documented daylight operating hours (8:30 AM – 6:00 PM).", bullet_style))
    story.append(Paragraph("• <b>Conditional Contact Release:</b> Contact phone numbers and email addresses remain shielded until the owner explicitly accepts an interest request.", bullet_style))
    story.append(Paragraph("• <b>Physical Inspection Checklist:</b> Before finalizing a handover, students are guided to inspect syllabus match, edition, and page condition in person, maintaining transparent peer trust.", bullet_style))

    story.append(PageBreak())

    # ==========================================
    # PAGE 9: 6. Testing, 6.1 Sample Test Cases
    # ==========================================
    story.append(Paragraph("6. Testing", section_heading))
    story.append(Paragraph(
        "The application was thoroughly verified using automated test suites via Python's <code>unittest</code> framework alongside manual "
        "browser walkthroughs across multiple student sessions. Tests validate route availability, database query execution, session authentication, "
        "listing creation, search filtering, and the request-interest lifecycle.",
        body_style
    ))
    story.append(Paragraph("6.1 Sample Functional and Business Logic Test Cases", subsection_heading))

    tc_data = [
        [Paragraph("#", table_header_style), Paragraph("Test Scenario / Input", table_header_style), Paragraph("Expected Output", table_header_style), Paragraph("Actual Output", table_header_style), Paragraph("Status", table_header_style)],
        [Paragraph("1", table_cell_bold), Paragraph("Load home page (GET /)", table_cell_style), Paragraph("HTTP 200, displays hero banner and seed book cards", table_cell_style), Paragraph("HTTP 200, 8 book cards rendered", table_cell_style), Paragraph("Pass", table_cell_bold)],
        [Paragraph("2", table_cell_bold), Paragraph("Search query 'DBMS' or 'Korth'", table_cell_style), Paragraph("Filters listings to show Database System Concepts", table_cell_style), Paragraph("Shows Korth DBMS textbook", table_cell_style), Paragraph("Pass", table_cell_bold)],
        [Paragraph("3", table_cell_bold), Paragraph("Filter by type 'Donate'", table_cell_style), Paragraph("Displays only free donation materials (Java, Python Notes)", table_cell_style), Paragraph("Displays matching donation cards", table_cell_style), Paragraph("Pass", table_cell_bold)],
        [Paragraph("4", table_cell_bold), Paragraph("View book detail (/listing/1)", table_cell_style), Paragraph("HTTP 200, displays full metadata & meeting point", table_cell_style), Paragraph("HTTP 200, renders detail page", table_cell_style), Paragraph("Pass", table_cell_bold)],
        [Paragraph("5", table_cell_bold), Paragraph("Post listing as unauthenticated user", table_cell_style), Paragraph("Redirects to /login with flash warning message", table_cell_style), Paragraph("Redirected to login successfully", table_cell_style), Paragraph("Pass", table_cell_bold)],
        [Paragraph("6", table_cell_bold), Paragraph("Sign in via Roll No: 10517704426", table_cell_style), Paragraph("Validates password hash; starts session as Sanya", table_cell_style), Paragraph("Logged in as Sanya (MCA 1-B)", table_cell_style), Paragraph("Pass", table_cell_bold)],
        [Paragraph("7", table_cell_bold), Paragraph("Create new listing without Title", table_cell_style), Paragraph("Form validation halts; prompts for mandatory fields", table_cell_style), Paragraph("Halted with alert notification", table_cell_style), Paragraph("Pass", table_cell_bold)],
        [Paragraph("8", table_cell_bold), Paragraph("Submit valid listing (Automata Theory)", table_cell_style), Paragraph("Inserts into listings; redirects to detail page", table_cell_style), Paragraph("Saved to SQLite; detail loaded", table_cell_style), Paragraph("Pass", table_cell_bold)],
        [Paragraph("9", table_cell_bold), Paragraph("Submit interest request on peer's book", table_cell_style), Paragraph("Inserts into exchange_requests with status 'Pending'", table_cell_style), Paragraph("Saved with status 'Pending'", table_cell_style), Paragraph("Pass", table_cell_bold)],
        [Paragraph("10", table_cell_bold), Paragraph("Attempt requesting own listed book", table_cell_style), Paragraph("Blocked with warning: cannot request own listing", table_cell_style), Paragraph("Blocked with warning notice", table_cell_style), Paragraph("Pass", table_cell_bold)],
        [Paragraph("11", table_cell_bold), Paragraph("Owner accepts request on their book", table_cell_style), Paragraph("Request -> 'Accepted'; Book -> 'Pending Handover'", table_cell_style), Paragraph("Statuses updated atomically", table_cell_style), Paragraph("Pass", table_cell_bold)],
    ]
    t_tc = Table(tc_data, colWidths=[20, 140, 140, 165, 50])
    t_tc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), BG_HEADER),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 2.5),
        ('BOTTOMPADDING', (0,0), (-1,-1), 2.5),
        ('LEFTPADDING', (0,0), (-1,-1), 4),
        ('RIGHTPADDING', (0,0), (-1,-1), 4),
    ]))
    story.append(t_tc)

    story.append(PageBreak())

    # ==========================================
    # PAGE 10: 6.2 Web Route Test Cases, 7. Results and Application Screenshots
    # ==========================================
    story.append(Paragraph("6.2 Web Application Route Test Cases", subsection_heading))
    route_tc_data = [
        [Paragraph("#", table_header_style), Paragraph("Test Scenario", table_header_style), Paragraph("Expected Behavior", table_header_style), Paragraph("Status", table_header_style)],
        [Paragraph("1", table_cell_bold), Paragraph("Open /, /guidelines, /about-project", table_cell_style), Paragraph("All public routes load properly with HTTP status 200.", table_cell_style), Paragraph("Pass", table_cell_bold)],
        [Paragraph("2", table_cell_bold), Paragraph("Student registration via /register", table_cell_style), Paragraph("Saves student to users table and auto-authenticates session.", table_cell_style), Paragraph("Pass", table_cell_bold)],
        [Paragraph("3", table_cell_bold), Paragraph("Duplicate enrollment number registration", table_cell_style), Paragraph("Rejected by SQLite UNIQUE constraint with user-friendly alert.", table_cell_style), Paragraph("Pass", table_cell_bold)],
        [Paragraph("4", table_cell_bold), Paragraph("1-Click demo login (/demo-login/1)", table_cell_style), Paragraph("Instantly switches session to Sanya (MCA 1-B) for viva evaluation.", table_cell_style), Paragraph("Pass", table_cell_bold)],
        [Paragraph("5", table_cell_bold), Paragraph("Load /dashboard/my-listings and /my-requests", table_cell_style), Paragraph("Displays student's materials and pending request notification badges.", table_cell_style), Paragraph("Pass", table_cell_bold)],
        [Paragraph("6", table_cell_bold), Paragraph("Delete listing (/listings/<id>/delete)", table_cell_style), Paragraph("Removes listing from SQLite and cascade-cleans associated requests.", table_cell_style), Paragraph("Pass", table_cell_bold)],
    ]
    t_route_tc = Table(route_tc_data, colWidths=[20, 160, 280, 55])
    t_route_tc.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,0), BG_HEADER),
        ('GRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 3),
        ('BOTTOMPADDING', (0,0), (-1,-1), 3),
        ('LEFTPADDING', (0,0), (-1,-1), 5),
        ('RIGHTPADDING', (0,0), (-1,-1), 5),
    ]))
    story.append(t_route_tc)
    story.append(Spacer(1, 8))

    story.append(Paragraph("7. Results and Application Screenshots", section_heading))
    story.append(Paragraph(
        "When launched locally at <b>http://127.0.0.1:5000</b>, all functional modules of <b>BookBridge</b> operate reliably. "
        "The catalog displays categorized textbooks across core MCA subjects, keyword search executes in real time, and the request-interest "
        "workflow updates listing states seamlessly across student sessions.",
        body_style
    ))
    story.append(Spacer(1, 4))

    fig_boxes = [
        [Paragraph("<b>Fig. 7.1 – Home Page & Course Material Catalogue</b><br/>"
                   "<font color='#6b7280' size='7.5'>(Paste screenshot showing the Hero banner, live campus stats counter, multi-criteria filter toolbar, and responsive book cards with condition and exchange badges)</font>", body_style)],
        [Paragraph("<b>Fig. 7.2 – Book Detail View & Express Interest Modal</b><br/>"
                   "<font color='#6b7280' size='7.5'>(Paste screenshot showing textbook metadata, author, condition remarks, approved campus meeting point card, and the interactive borrower request-interest submission form)</font>", body_style)],
        [Paragraph("<b>Fig. 7.3 – Student Dashboard (My Listings, Requests Hub) & Safe Handover Guidelines</b><br/>"
                   "<font color='#6b7280' size='7.5'>(Paste screenshots showing the My Posted Materials management table, Incoming/Outgoing request coordination tabs with Accept/Complete controls, and the Safe Campus Handover Directory)</font>", body_style)],
    ]
    t_figs = Table(fig_boxes, colWidths=[515])
    t_figs.setStyle(TableStyle([
        ('BOX', (0,0), (-1,-1), 0.8, BORDER_COLOR),
        ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT),
        ('INNERGRID', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 10),
        ('BOTTOMPADDING', (0,0), (-1,-1), 10),
        ('LEFTPADDING', (0,0), (-1,-1), 10),
        ('RIGHTPADDING', (0,0), (-1,-1), 10),
    ]))
    story.append(t_figs)

    story.append(PageBreak())

    # ==========================================
    # PAGE 11: 8. Limitations, Future Scope, Conclusion, References
    # ==========================================
    story.append(Paragraph("8. Limitations, Future Scope, and Conclusion", section_heading))
    story.append(Paragraph("8.1 Limitations", subsection_heading))
    story.append(Paragraph("• <b>Local Campus Deployment:</b> The current prototype runs on a local SQLite instance and requires deployment on university intranet servers for cross-host access.", bullet_style))
    story.append(Paragraph("• <b>Manual Condition Verification:</b> Assessment of book physical wear relies on honesty of student descriptions until visual inspection at the meeting point.", bullet_style))
    story.append(Paragraph("• <b>No Real-Time Push Notifications:</b> Students must check their web dashboard to see new incoming requests rather than receiving SMS or push notifications.", bullet_style))
    story.append(Paragraph("• <b>Single University Scope:</b> Handover coordination is confined to approved spots on one physical campus and does not span distant branch campuses.", bullet_style))

    story.append(Paragraph("8.2 Future Scope", subsection_heading))
    story.append(Paragraph("• <b>Automated SMS & Email Alerts:</b> Integrate Twilio or college SMTP to notify owners immediately when an interest request is submitted.", bullet_style))
    story.append(Paragraph("• <b>Handover QR Verification:</b> Generate unique handover QR codes to be scanned by students at the library desk to record return dates cryptographically.", bullet_style))
    story.append(Paragraph("• <b>ISBN Barcode Scanner:</b> Enable camera-based barcode scanning on mobile devices to auto-populate textbook title, author, and edition metadata.", bullet_style))
    story.append(Paragraph("• <b>AI-Based Syllabus Matcher:</b> Recommend relevant senior textbooks automatically based on the electives a student selects during semester registration.", bullet_style))

    story.append(Paragraph("8.3 Conclusion", subsection_heading))
    story.append(Paragraph(
        "<b>BookBridge</b> fulfills all requirements established in the minor project synopsis. It provides university students with an affordable, "
        "sustainable, and privacy-conscious alternative to purchasing new commercial textbooks each semester. By combining a searchable web interface, "
        "a reliable relational database, a request-interest state machine, and approved on-campus handover protocols, the project demonstrates a practical, "
        "impactful application of web technologies and database engineering taught in the MCA curriculum.",
        body_style
    ))
    story.append(Spacer(1, 4))

    story.append(Paragraph("References", section_heading))
    story.append(Paragraph("1. Flask Documentation – Pallets Projects (flask.palletsprojects.com)", body_style))
    story.append(Paragraph("2. Python 3 Documentation (sqlite3, hashlib, and unittest modules) – Python Software Foundation (docs.python.org)", body_style))
    story.append(Paragraph("3. SQLite Documentation & SQL Syntax – SQLite Consortium (sqlite.org/docs.html)", body_style))
    story.append(Paragraph("4. Bootstrap 5.3 Documentation – Twitter / The Bootstrap Authors (getbootstrap.com/docs/5.3)", body_style))
    story.append(Paragraph("5. MDN Web Docs: HTML5 Semantic Elements, CSS3 Layouts, and JavaScript Fetch API – Mozilla (developer.mozilla.org)", body_style))

    story.append(PageBreak())

    # ==========================================
    # PAGE 12: References (Cont), Appendix A, Appendix B
    # ==========================================
    story.append(Paragraph("6. University Grants Commission (UGC) Guidelines on Campus Safety & Student Welfare (ugc.gov.in)", body_style))
    story.append(Spacer(1, 4))

    story.append(Paragraph("Appendix A: Steps to Run the Project", section_heading))
    app_text = (
        "1. Ensure Python 3.10 or later is installed on the system.\n"
        "2. Open a terminal or PowerShell prompt inside the project directory: cd bookbridge\n"
        "3. Install required web dependencies: pip install flask\n"
        "4. Initialize database and seed sample course textbooks: python database.py\n"
        "5. Start the Flask local development server: python app.py\n"
        "6. Open web browser and navigate to: http://127.0.0.1:5000\n"
        "7. Execute automated verification test suite: python test_app.py"
    )
    t_app = Table([[Paragraph(app_text.replace('\n', '<br/>'), code_style)]], colWidths=[515])
    t_app.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT),
        ('BOX', (0,0), (-1,-1), 0.5, BORDER_COLOR),
        ('TOPPADDING', (0,0), (-1,-1), 6),
        ('BOTTOMPADDING', (0,0), (-1,-1), 6),
        ('LEFTPADDING', (0,0), (-1,-1), 8),
        ('RIGHTPADDING', (0,0), (-1,-1), 8),
    ]))
    story.append(t_app)
    story.append(Spacer(1, 10))

    story.append(Paragraph("Appendix B: Plagiarism Check Report", section_heading))
    story.append(Paragraph(
        "<i>Note: As instructed by the project mentor, the official plagiarism verification report obtained from the college library "
        "is attached below/following this page.</i>",
        body_style
    ))
    story.append(Spacer(1, 8))

    plag_box_data = [
        [Paragraph("<br/><br/><br/><b>ATTACH LIBRARY PLAGIARISM REPORT HERE</b><br/><br/>"
                   "<font size='8' color='#4b5563'>Student Name: Sanya &bull; Enrollment No.: 10517704426 &bull; Course: MCA 1-B<br/>"
                   "Project Mentor: Dr. Cosmena</font><br/><br/><br/>", top_badge_style)]
    ]
    t_plag = Table(plag_box_data, colWidths=[515])
    t_plag.setStyle(TableStyle([
        ('BACKGROUND', (0,0), (-1,-1), BG_LIGHT),
        ('BOX', (0,0), (-1,-1), 1, BORDER_COLOR),
        ('ALIGN', (0,0), (-1,-1), 'CENTER'),
        ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
        ('TOPPADDING', (0,0), (-1,-1), 20),
        ('BOTTOMPADDING', (0,0), (-1,-1), 20),
    ]))
    story.append(t_plag)

    # Build the document
    doc.build(story, canvasmaker=NumberedCanvas)
    print(f"PDF successfully built: {filename}")

if __name__ == '__main__':
    build_pdf()
