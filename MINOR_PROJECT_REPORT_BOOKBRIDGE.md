# MINOR PROJECT REPORT • MASTER OF COMPUTER APPLICATIONS (MCA 1-B)

# BookBridge – Campus Book Exchange
### A Web-Based Campus Book and Learning-Material Exchange Board

---

## Student & Submission Details

| Particulars | Details |
|---|---|
| **Student Name** | Sanya |
| **Enrollment Number** | 10517704426 |
| **Course & Section** | Master of Computer Applications (MCA 1-B) |
| **Project Title** | BookBridge – A Campus Book and Learning-Material Exchange Board |
| **Project Mentor** | Dr. Cosmena |
| **Submission Date** | November 17, 2026 |
| **Project Status** | Completed |
| **Report Status** | Completed (Plagiarism check report to be attached from the library) |

---

## Declaration

I, **Sanya** (Enrollment No. **10517704426**), a student of Master of Computer Applications (MCA 1-B), hereby declare that this minor project report titled *“BookBridge – A Campus Book and Learning-Material Exchange Board”* is my original work carried out under the guidance of **Dr. Cosmena**. All sources referred to during this work have been listed in the references section. This report has not been submitted elsewhere for any other degree or diploma.

**Date:** ________________________  
**Signature of Student:** ________________________

---

## Certificate

This is to certify that **Sanya** (Enrollment No. **10517704426**), a student of MCA 1-B, has successfully completed the minor project titled *“BookBridge – Campus Book and Learning-Material Exchange Board”* under my supervision and guidance. To the best of my knowledge, this work is original and fulfills the requirements of the course.

**Date:** ________________________  
**Project Mentor (Dr. Cosmena):** ________________________

---

## Acknowledgement

I would like to express my sincere thanks to my project mentor, **Dr. Cosmena**, for her constant guidance, valuable suggestions, and support throughout the completion of this project. I am also thankful to the faculty members of the MCA department and my classmates for testing the application and giving helpful feedback, as well as my family for their encouragement.

---

## Abstract

**BookBridge** is a proposed web-based campus exchange directory that connects students who have unused learning materials with students who need them. Today, many university students require textbooks, reference books, and practical manuals for their academic courses, but purchasing brand-new copies each semester is expensive. At the same time, many senior and peer students have books and study materials that they no longer actively use. These materials often sit unused in dormitories and homes, even though other students could benefit from borrowing, exchanging, or receiving them.

This application allows registered students to search, filter, and browse listings by book title, author, subject module, and course (such as MCA, B.Tech CS, BCA). The platform supports three flexible resource-sharing models: **Lending** (with a specified borrowing timeframe), **Exchange** (book-for-book trade), and **Free Donation**. Through an intuitive request-interest flow, students can communicate their requirements and propose handover arrangements. To protect student privacy and physical safety, the system strictly avoids publishing personal residential addresses and coordinates physical handovers exclusively at approved, monitored university meeting points such as the Central Library Foyer and Student Activity Centre (SAC).

The project is built using HTML5, CSS3, and JavaScript for the frontend, Python with the Flask web framework for the backend, and SQLite for relational database management. The web portal includes active search filtering, listing creation/editing, student dashboards for managing requests, and comprehensive campus handover guidelines. All automated test cases written for the project pass successfully.

**Keywords:** Campus Book Exchange, Peer-to-Peer Resource Sharing, Academic Lending, Flask Web Framework, SQLite, Web Development, Campus Safety.

---

## 1. Introduction

### 1.1 Background
Textbooks, reference manuals, and lecture notes represent an essential yet recurring financial expenditure for university students throughout their academic tenure. In professional computing disciplines such as the Master of Computer Applications (MCA) and Computer Science & Engineering, prescribed reference volumes—such as *Database System Concepts* by Korth, *Computer Networks* by Tanenbaum, and *Algorithms* by CLRS—carry substantial retail prices. Once students conclude end-semester examinations, these books frequently sit unused on dorm shelves, while incoming juniors seek identical copies.

While digital PDFs are common, physical textbooks remain indispensable for in-depth technical study, mathematical derivation, and open-book university assessments. However, universities typically lack a centralized, campus-specific directory to facilitate direct peer-to-peer textbook reuse. Commercial buyback platforms impose heavy courier fees and intermediary margins, while unorganized social media chat groups suffer from information clutter and lack privacy safeguards.

### 1.2 Problem Statement
When a university student requires a course textbook or wishes to pass on completed study materials, finding an interested peer is not straightforward. Searching across unorganized student messaging groups or generic classified websites is time-consuming, unindexed, and exposes students' personal telephone numbers to unknown individuals. Commercial buyback portals offer negligible repurchase value and require postal transit. Furthermore, arranging off-campus physical meetups with unfamiliar parties presents personal safety concerns. Therefore, there is an urgent need for a localized, campus-centric web platform that catalogs available study materials, facilitates direct peer interest requests, and enforces safe handovers strictly within monitored university grounds.

### 1.3 Objectives
- Provide an intuitive, searchable directory where students can discover books by title, author, subject, and course.
- Support three flexible sharing options: Lending (time-bound), Exchange (reciprocal barter), and Free Donation.
- Implement an interactive request-interest workflow allowing borrowers to propose terms and owners to review and respond.
- Enforce campus safety protocols by restricting physical exchanges to designated, CCTV-monitored university points.
- Protect student privacy by completely avoiding collection or publication of private residential addresses.
- Provide student dashboards for monitoring active listings, incoming peer requests, and handover statuses.

### 1.4 Scope of the Project
The application operates as a campus-level web portal tailored for enrolled university students and faculty. It facilitates listing creation, multi-criteria catalog queries, request-interest coordination, and safe handover tracking using Python, Flask, and SQLite. Commercial financial payments, external courier shipping logistics, and cross-university inter-campus delivery networks are outside the scope of this minor project prototype.

---

## 2. System Analysis

### 2.1 Existing Methods and Their Limitations
Presently, students rely on informal, fragmented mechanisms to procure second-hand textbooks, each exhibiting critical limitations:
- **Commercial Resale Portals:** Sites like OLX or commercial book resellers take significant profit cuts, involve courier charges, and fail to filter books by specific university course syllabi.
- **Unorganized Messaging Groups:** WhatsApp and Telegram batch groups flood feeds with unstructured requests that quickly get lost, lacking search filters and structured status tracking.
- **Privacy Exposure:** Broadcasting book needs in public groups publicly exposes personal phone numbers and identities, increasing spam and unwanted contact.
- **Physical Safety Risks:** Informal exchanges frequently pressure students to meet strangers at unverified off-campus street locations or after hours.

### 2.2 Proposed System
**BookBridge** resolves these shortcomings through a centralized, privacy-conscious university portal. Registered students can list surplus learning materials within seconds, indicating subject, semester, physical condition, and listing type (Lend, Exchange, or Donate). Borrowers filter listings effortlessly and submit interest requests detailing their requirements. Book owners review requests in their personal dashboard, accept handover terms, and agree to meet at pre-approved campus points such as the Central Library Foyer during verified daylight hours, completely eliminating off-campus risks.

### 2.3 Feasibility Study

| Feasibility Type | Assessment |
|---|---|
| **Technical Feasibility** | Built using Python, Flask, SQLite, HTML5, CSS3, and JavaScript. All components are lightweight, standard in the MCA curriculum, and execute smoothly on any standard laptop without complex configurations. |
| **Economic Feasibility** | Zero financial investment required. The entire tech stack comprises free, open-source tools. No proprietary servers, paid APIs, or commercial hosting subscriptions are needed. |
| **Operational Feasibility** | Extremely user-friendly. Designed with clear card layouts, intuitive badges, and straightforward forms so any student can search, post, or request books without prior training. |
| **Schedule Feasibility** | Structured with a focused, well-defined scope allowing development, database design, testing, and report documentation to be completed comfortably within the one-month minor project timeframe. |

---

## 3. System Requirements

### 3.1 Functional Requirements

| Req. ID | Description |
|---|---|
| **FR1** | The system allows students to register and sign in securely using their University Enrollment Number and password. |
| **FR2** | Registered users can create new listings by specifying Title, Author, Subject, Course, Semester, Condition, Type, and Handover Spot. |
| **FR3** | The catalog provides keyword search across titles and authors, with filters for Course, Exchange Type, and Status. |
| **FR4** | Students can express interest in a book by proposing a message, borrowing duration, or reciprocal trade book. |
| **FR5** | Book owners can review incoming interest requests and Accept, Decline, or mark them as Completed. |
| **FR6** | The system automatically shifts listing status from 'Available' to 'Pending Handover' and 'Completed' based on request state. |
| **FR7** | The system enforces approved campus meeting points and provides a dedicated Campus Handover Guidelines section. |
| **FR8** | Form validations reject incomplete inputs and prevent students from expressing interest in their own listings. |

### 3.2 Non-Functional Requirements
- **Usability:** Clean, intuitive interface powered by Bootstrap 5, optimized for both desktop monitors and mobile browsers.
- **Performance:** Lightweight database queries and Jinja2 templating ensure pages render in under 200 milliseconds.
- **Privacy:** Zero collection or display of personal home addresses or dorm rooms. Phone numbers remain hidden until a request is accepted.
- **Security:** Cryptographic password hashing via Werkzeug (PBKDF2-SHA256) and parameterized SQL queries preventing SQL Injection.
- **Reliability:** Foreign key integrity constraints in SQLite prevent orphan listings or dangling exchange requests upon deletion.

### 3.3 Hardware and Software Requirements

| Component | Minimum Requirement |
|---|---|
| **Processor & RAM** | Intel Core i3 / AMD Ryzen 3 or higher; Minimum 4 GB RAM |
| **Operating System** | Windows 10 or later (fully compatible with Ubuntu Linux and macOS) |
| **Programming Language** | Python 3.10 or later |
| **Web Framework & Tools** | Flask 3.x, Jinja2, Werkzeug Security, unittest / pytest |
| **Database Engine** | SQLite3 (embedded relational database with row factory) |
| **Web Browser & Editor** | Google Chrome, Mozilla Firefox, or Microsoft Edge; VS Code or Antigravity IDE |

---

## 4. System Design

### 4.1 System Architecture
BookBridge follows a classic Model-View-Controller (MVC) architectural pattern adapted for web microframeworks. The application is segmented into four cohesive layers:
- **Step 1 – Client Browser (Frontend):** Renders HTML5 templates with Bootstrap 5 and custom CSS. Dispatches HTTP GET search filters and POST request submissions to Flask routes.
- **Step 2 – Web Application Controller (app.py):** Handles route dispatching, session authentication, request validation, flash notifications, and orchestrates business logic.
- **Step 3 – Exchange Workflow Engine:** Manages the state transitions of listings (`Available` &rarr; `Pending Handover` &rarr; `Completed`) and coordinates interest requests between borrower and owner.
- **Step 4 – Relational Database Layer (database.py / SQLite):** Persists records across normalized tables with enforced foreign key constraints, executing parameterized SQL transactions.

### 4.2 Data Flow Overview
- **Level 0 (Context DFD):** The Student interacts with BookBridge by registering credentials, posting book listings, searching the catalogue, submitting interest requests, and coordinating handovers. The system responds with real-time book availability, filtered results, and handover instructions.
- **Level 1 (Functional DFD):** The system partitions data handling into five stages: (1) *User Authentication & Session Management*, (2) *Listing Management*, (3) *Catalog Querying & Multi-Filter Engine*, (4) *Interest Request Dispatching*, and (5) *Handover Lifecycle Coordination*.

### 4.3 Database Design

| Table Name | Column | Data Type | Purpose |
|---|---|---|---|
| **users**<br/>*(Stores student accounts)* | `id`<br/>`enrollment_no`<br/>`full_name`<br/>`email`<br/>`password_hash`<br/>`department`<br/>`course_year`<br/>`contact_phone` | INTEGER (PK)<br/>TEXT (UNIQUE)<br/>TEXT<br/>TEXT (UNIQUE)<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT | Primary Key<br/>Student Roll Number<br/>Full Name<br/>Campus Email<br/>PBKDF2-SHA256 Hash<br/>Academic Dept<br/>Class / Section<br/>Contact Phone |
| **meeting_points**<br/>*(Approved campus spots)* | `id`<br/>`name`<br/>`location_desc`<br/>`operating_hours`<br/>`safety_notes` | INTEGER (PK)<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT | Primary Key<br/>Spot Name (e.g. Library)<br/>Location Details<br/>Daylight Hours<br/>CCTV / Visibility Notes |
| **listings**<br/>*(Book & study materials)* | `id`<br/>`user_id`<br/>`title`<br/>`author`<br/>`subject`<br/>`course`<br/>`semester`<br/>`listing_type`<br/>`condition`<br/>`availability_status`<br/>`preferred_mp_id` | INTEGER (PK)<br/>INTEGER (FK)<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT<br/>INTEGER (FK) | Primary Key<br/>Refers to users(id)<br/>Book Title<br/>Author(s)<br/>Course Subject<br/>Branch (MCA, etc.)<br/>Target Semester<br/>Lend / Exchange / Donate<br/>Book Condition<br/>Available / Pending / Done<br/>Refers to meeting_points(id) |
| **exchange_requests**<br/>*(Interest requests)* | `id`<br/>`listing_id`<br/>`requester_id`<br/>`meeting_point_id`<br/>`message`<br/>`offered_exchange_item`<br/>`proposed_duration`<br/>`status`<br/>`owner_remarks` | INTEGER (PK)<br/>INTEGER (FK)<br/>INTEGER (FK)<br/>INTEGER (FK)<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT<br/>TEXT | Primary Key<br/>Refers to listings(id)<br/>Refers to users(id)<br/>Refers to meeting_points(id)<br/>Borrower message<br/>Offered trade book<br/>Borrowing period<br/>Pending / Accepted / Done<br/>Owner meeting note |

### 4.4 Application Routes

| Route | Method | Function |
|---|---|---|
| `/` | GET | Opens main catalogue with keyword search and multi-parameter filtering. |
| `/listing/<id>` | GET | Displays full book metadata, meeting spot details, and request form. |
| `/listings/create` | GET, POST | Allows authenticated students to list books for Lend, Exchange, or Donate. |
| `/listings/<id>/edit` | GET, POST | Enables book owners to update description, condition, or status. |
| `/listing/<id>/express-interest` | POST | Submits borrower interest request with duration or trade offer. |
| `/requests/<id>/update` | POST | Owner accepts, declines, or marks handover as completed. |
| `/dashboard/my-listings` | GET | Displays student's posted books and pending request indicators. |
| `/dashboard/my-requests` | GET | Hub for managing incoming peer requests and outgoing borrow requests. |
| `/guidelines` | GET | Shows approved campus meeting points and safety protocols. |
| `/about-project` | GET | Comprehensive synopsis, mentor details, architecture, and viva guide. |
| `/register, /login, /logout` | GET, POST | Student authentication and session lifecycle management. |

---

## 5. Implementation

### 5.1 Project Folder Structure

| File / Folder | Role in the Project |
|---|---|
| `app.py` | Main Flask application containing route controllers, session handling, and validation. |
| `database.py` | SQLite connection utility, DDL schema executor, and sample dataset seeder. |
| `schema.sql` | Relational table definitions with constraints (users, listings, points, requests). |
| `test_app.py` | Automated unit test suite verifying catalog, filters, listings, and requests. |
| `run.bat` | One-click Windows batch launcher that boots Flask and launches default browser. |
| `templates/` | Jinja2 HTML templates (`base.html`, `index.html`, `listing_detail.html`, etc.). |
| `static/` | Frontend assets: custom CSS (`custom.css`) and client-side interactions (`main.js`). |

### 5.2 Core Modules and Business Logic
- **Dynamic Multi-Parameter Filtering:** Dynamically appends conditions to SQL SELECT statements using parameterized wildcard patterns.
- **Tri-Model Resource Sharing:** Dynamic forms adapt depending on whether the item is for *Lend* (recording loan duration), *Exchange* (recording reciprocal trade offer), or *Donate* (recording recipient request).
- **Request-Interest State Machine:**
  - `Available` &rarr; Book is open to all students.
  - `Pending Review` &rarr; Borrower expresses interest.
  - `Pending Handover` &rarr; Owner accepts request and designates a time.
  - `Completed` &rarr; Handover verified at approved campus spot.

### 5.3 Campus Safety, Privacy, and Handover Protocols
- **Zero Home Address Collection:** No residential or hostel fields stored.
- **Approved Campus Meeting Points:** Central Library Foyer, SAC Atrium, MCA Lab 102 corridors.
- **Daylight Hours Enforced:** Handover times restricted to 8:30 AM – 6:00 PM.
- **Physical Inspection Checklist:** Visual verification of book condition before marking exchange completed.

---

## 6. Testing

### 6.1 Sample Functional and Business Logic Test Cases

| # | Test Scenario / Input | Expected Output | Actual Output | Status |
|---|---|---|---|---|
| 1 | Load home page (`GET /`) | HTTP 200, displays hero banner and seed book cards | HTTP 200, 8 book cards rendered | **Pass** |
| 2 | Search query 'DBMS' or 'Korth' | Filters listings to show Database System Concepts | Shows Korth DBMS textbook | **Pass** |
| 3 | Filter by type 'Donate' | Displays only free donation materials (Java, Python Notes) | Displays matching donation cards | **Pass** |
| 4 | View book detail (`/listing/1`) | HTTP 200, displays full metadata & meeting point | HTTP 200, renders detail page | **Pass** |
| 5 | Post listing as unauthenticated user | Redirects to `/login` with flash warning message | Redirected to login successfully | **Pass** |
| 6 | Sign in via Roll No: `10517704426` | Validates password hash; starts session as Sanya | Logged in as Sanya (MCA 1-B) | **Pass** |
| 7 | Create listing without Title | Form validation halts; prompts for mandatory fields | Halted with alert notification | **Pass** |
| 8 | Submit valid listing (Automata Theory) | Inserts into listings; redirects to detail page | Saved to SQLite; detail loaded | **Pass** |
| 9 | Submit interest request on peer's book | Inserts into `exchange_requests` with status 'Pending' | Saved with status 'Pending' | **Pass** |
| 10 | Attempt requesting own listed book | Blocked with warning: cannot request own listing | Blocked with warning notice | **Pass** |
| 11 | Owner accepts request on their book | Request &rarr; 'Accepted'; Book &rarr; 'Pending Handover' | Statuses updated atomically | **Pass** |

### 6.2 Web Application Route Test Cases

| # | Test Scenario | Expected Behavior | Status |
|---|---|---|---|
| 1 | Open `/`, `/guidelines`, `/about-project` | All public routes load properly with HTTP status 200. | **Pass** |
| 2 | Student registration via `/register` | Saves student to users table and auto-authenticates session. | **Pass** |
| 3 | Duplicate enrollment number registration | Rejected by SQLite UNIQUE constraint with user-friendly alert. | **Pass** |
| 4 | 1-Click demo login (`/demo-login/1`) | Instantly switches session to Sanya (MCA 1-B) for viva evaluation. | **Pass** |
| 5 | Load `/dashboard/my-listings` and `/my-requests` | Displays student's materials and pending request notification badges. | **Pass** |
| 6 | Delete listing (`/listings/<id>/delete`) | Removes listing from SQLite and cascade-cleans associated requests. | **Pass** |

---

## 7. Results and Application Screenshots

When launched locally at `http://127.0.0.1:5000`, all modules of **BookBridge** execute smoothly:

- **Fig. 7.1 – Home Page & Course Material Catalogue:** Displays Hero banner, live campus stats counter, multi-parameter filter toolbar, and responsive book cards with condition and exchange badges.
- **Fig. 7.2 – Book Detail View & Express Interest Form:** Displays textbook metadata, author, condition remarks, approved campus meeting point card, and the interactive borrower request-interest form.
- **Fig. 7.3 – Student Dashboard (My Listings, Requests Hub) & Safe Handover Guidelines:** Displays the My Posted Materials management table, Incoming/Outgoing request coordination tabs with Accept/Complete controls, and the Safe Campus Handover Directory.

---

## 8. Limitations, Future Scope, and Conclusion

### 8.1 Limitations
- **Local Campus Deployment:** The current prototype runs locally and requires deployment on university intranet servers for cross-host access.
- **Manual Condition Verification:** Assessment of physical wear relies on student descriptions until visual inspection at the meeting point.
- **No Real-Time Push Notifications:** Students check their web dashboard to see new incoming requests rather than receiving SMS or push notifications.
- **Single University Scope:** Handover coordination is confined to approved spots on one physical campus.

### 8.2 Future Scope
- **Automated SMS & Email Alerts:** Integrate Twilio or college SMTP to notify owners immediately when an interest request is posted.
- **Handover QR Verification:** Generate unique QR codes scanned at the library desk to record return dates cryptographically.
- **ISBN Barcode Scanner:** Enable camera-based barcode scanning on mobile devices to auto-populate textbook title and edition.
- **AI-Based Syllabus Matcher:** Recommend relevant senior textbooks automatically based on enrolled course electives.

### 8.3 Conclusion
**BookBridge** fulfills all requirements established in the minor project synopsis. It provides university students with an affordable, sustainable, and privacy-conscious alternative to purchasing new commercial textbooks each semester. By combining a searchable web interface, a reliable relational database, a request-interest state machine, and approved on-campus handover protocols, the project demonstrates a practical, impactful application of web technologies and database engineering taught in the MCA curriculum.

---

## References
1. Flask Documentation – Pallets Projects (`flask.palletsprojects.com`)
2. Python 3 Documentation (`sqlite3`, `hashlib`, and `unittest` modules) – Python Software Foundation (`docs.python.org`)
3. SQLite Documentation & SQL Syntax – SQLite Consortium (`sqlite.org/docs.html`)
4. Bootstrap 5.3 Documentation – Twitter / The Bootstrap Authors (`getbootstrap.com/docs/5.3`)
5. MDN Web Docs: HTML5 Semantic Elements, CSS3 Layouts, and JavaScript Fetch API – Mozilla (`developer.mozilla.org`)
6. University Grants Commission (UGC) Guidelines on Campus Safety & Student Welfare (`ugc.gov.in`)

---

## Appendix A: Steps to Run the Project
```
1. Ensure Python 3.10 or later is installed on the system.
2. Open a terminal or PowerShell prompt inside the project directory: cd bookbridge
3. Install required web dependencies: pip install flask
4. Initialize the SQLite database and seed sample textbooks: python database.py
5. Start the Flask local development server: python app.py
6. Open your web browser and navigate to: http://127.0.0.1:5000
7. Execute automated verification test suite: python test_app.py
```

---

## Appendix B: Plagiarism Check Report
*Note: As instructed by the project mentor, the official plagiarism verification report obtained from the college library is attached below/following this page.*

```
+--------------------------------------------------------------------------+
|                                                                          |
|                   ATTACH LIBRARY PLAGIARISM REPORT HERE                  |
|                                                                          |
|       Student Name: Sanya • Enrollment No.: 10517704426 • Course: MCA 1-B  |
|                       Project Mentor: Dr. Cosmena                        |
|                                                                          |
+--------------------------------------------------------------------------+
```
