# ACADEMIC PROJECT REPORT & VIVA VOCE GUIDE
## BookBridge: A Campus Book and Learning-Material Exchange Board

---

### Project Metadata
- **Project Title:** BookBridge: A Campus Book and Learning-Material Exchange Board
- **Student Name:** Sanya
- **Enrollment Number:** 10517704426
- **Degree:** Master of Computer Applications (MCA)
- **Class / Section:** MCA 1-B
- **Project Mentor:** Dr. Cosmena
- **Academic Term:** Semester 1 Mini-Project

---

## 1. ABSTRACT / SYNOPSIS
Students often need textbooks, reference books, and other learning materials for their courses, but purchasing new copies can be expensive. At the same time, many students have books or study materials that they no longer use. These materials may remain unused even though other students could benefit from borrowing, exchanging, or receiving them.

**BookBridge** is a proposed web-based campus exchange directory that connects students who have unused learning materials with students who need them. Users are able to browse listings and find books by title, subject, or course. The platform supports listing materials for lending, exchange, or donation, while encouraging safe contact practices and handovers at approved campus meeting points.

The system combines a searchable web interface (HTML5, CSS3, JavaScript, Bootstrap 5), a lightweight backend (Python Flask), and a relational database (SQLite) to provide an end-to-end request-interest flow without sharing private addresses.

---

## 2. SYSTEM ARCHITECTURE & MODULES

### 2.1 Three-Tier Architecture
1. **Presentation Tier (Frontend):**
   - Built using HTML5, CSS3, JavaScript, and Bootstrap 5.3.
   - Provides an intuitive, responsive interface for catalog browsing, multi-criteria filtering, and handover tracking.
2. **Application Tier (Backend / Controller):**
   - Developed using Python 3 and the Flask framework.
   - Implements URL routing, request dispatching, session management, and business logic.
3. **Data Tier (Database):**
   - SQLite relational database with enforced Foreign Key constraints and indexed lookups.

### 2.2 System Modules
- **Authentication & Student Profile Module:** Manages registration with Roll Number, password encryption (PBKDF2/SHA-256), and secure session cookies.
- **Search & Catalog Management Module:** Provides real-time filtering by book title, subject, semester, condition, and exchange model.
- **Listing Lifecycle Module:** Handles listing creation, editing, status transitions (`Available` -> `Pending Handover` -> `Completed`), and deletion.
- **Request-Interest Workflow Module:** Facilitates peer communication with custom messages, duration proposals, and trade item offerings.
- **Campus Safety & Handover Coordination Module:** Enforces university-approved meeting points, daytime hours, and condition verification checklists.

---

## 3. ENTITY RELATIONSHIP (E-R) MODEL

```
+------------------+          1:N          +----------------------+
|      USERS       |--------------------->|       LISTINGS       |
+------------------+                      +----------------------+
| id (PK)          |                      | id (PK)              |
| enrollment_no    |                      | user_id (FK)         |
| full_name        |                      | title                |
| email            |                      | author               |
| password_hash    |                      | subject              |
| department       |                      | course, semester     |
| course_year      |                      | listing_type         |
| contact_phone    |                      | condition            |
+------------------+                      | availability_status  |
        | 1                               | preferred_mp_id (FK) |
        |                                 +----------------------+
        |                                            | 1
        | 1:N                                        |
        v                                            v 1:N
+---------------------------------------------------------+
|                    EXCHANGE_REQUESTS                    |
+---------------------------------------------------------+
| id (PK)                                                 |
| listing_id (FK)                                         |
| requester_id (FK)                                       |
| meeting_point_id (FK)                                   |
| message                                                 |
| offered_exchange_item                                   |
| proposed_duration                                       |
| status (Pending, Accepted, Declined, Completed)         |
| owner_remarks                                           |
+---------------------------------------------------------+
        ^
        | N:1
+--------------------------------+
|         MEETING_POINTS         |
+--------------------------------+
| id (PK)                        |
| name                           |
| location_desc                  |
| operating_hours                |
| safety_notes                   |
+--------------------------------+
```

---

## 4. DATA FLOW DIAGRAMS (DFD)

### Level 0: Context Diagram
```
[ Student / User ]
       |
       |--- 1. Login / Register Credential Details ------------>
       |--- 2. Post Book / Notes Listing ---------------------->
       |--- 3. Search / Filter Material Directory ------------->  +--------------------+
       |--- 4. Submit Interest Request ------------------------>  |     BookBridge     |
       |--- 5. Accept / Decline Handover Request -------------->  |   Campus Portal    |
       |                                                          +--------------------+
       |<-- 6. Browse Book Results & Availability Status -------
       |<-- 7. Receive Handover Note & Campus Spot Details -----
```

### Level 1: Functional DFD
1. **User Authentication:** Input -> Validate Credentials -> Generate Session.
2. **Listing Registration:** Input Book Specs -> Verify Ownership -> Store in `listings` table.
3. **Catalog Query:** Search Keyword + Type/Course Filters -> Query SQLite Database -> Return matching cards.
4. **Interest Submission:** Borrower fills interest form -> Store in `exchange_requests` with status `Pending`.
5. **Handover Processing:** Book owner accepts -> Update `listings.availability_status` to `Pending Handover` -> Display contact info & meeting point -> Finalize upon physical exchange.

---

## 5. TEST CASES & VERIFICATION MATRIX

| Test ID | Module | Scenario / Input | Expected Result | Status |
|---|---|---|---|---|
| **TC-01** | Authentication | Register with valid Enrollment & Email | Account created; student auto-logged in | **PASS** |
| **TC-02** | Authentication | Register with duplicate Enrollment No | System alerts: student already registered | **PASS** |
| **TC-03** | Material Listing | Post listing without Book Title | Form validation stops submit; alerts user | **PASS** |
| **TC-04** | Material Listing | Post book with 'Lend' & condition 'Good' | Book appears in catalogue with 'To Lend' badge | **PASS** |
| **TC-05** | Catalogue Filter | Search keyword "Korth" or select "MCA" | Only DBMS by Korth or MCA books displayed | **PASS** |
| **TC-06** | Request Interest | Student expresses interest on peer's book | Record saved as 'Pending'; owner notified | **PASS** |
| **TC-07** | Request Interest | Student tries to request their own book | Prevented with notification alert | **PASS** |
| **TC-08** | Handover Status | Owner clicks 'Accept' on student request | Request is Accepted; Book becomes 'Pending Handover' | **PASS** |
| **TC-09** | Handover Finalize | Owner clicks 'Confirm Book Handed Over' | Listing & request updated to 'Completed' | **PASS** |

---

## 6. VIVA VOCE QUESTIONS & MODEL ANSWERS (FOR MCA EVALUATION)

### Q1: What was the primary motivation behind developing BookBridge?
> **Answer:** In colleges, students purchase costly textbooks each semester that are discarded or lie unused once examinations conclude. Simultaneously, junior students often struggle with the financial cost of purchasing these same books brand-new. BookBridge bridges this gap by creating an organized campus intranet directory where students can lend, exchange, or donate learning materials securely within university premises.

### Q2: Why did you choose Python with Flask rather than Django?
> **Answer:** For a focused, 1-month MCA semester project, Flask is ideal because it is a lightweight microframework that does not impose heavy boilerplate. It allows direct, transparent control over routing, session handling, request objects, and database interactions, making the code clean, readable, and easy to explain during academic viva voce.

### Q3: How does the application safeguard student privacy during book exchanges?
> **Answer:** Unlike public classified websites, BookBridge never asks for or displays personal residential addresses or dorm room numbers. All physical handovers are restricted to official university meeting points (such as the Central Library Foyer, SAC, or Department Lab lobbies) during daytime hours. Contact telephone numbers are only visible after the owner explicitly accepts a request.

### Q4: Explain the difference between the three listing types: Lend, Exchange, and Donate.
> **Answer:**
> - **Lend:** The owner retains permanent ownership of the book and lends it to a peer for a specified duration (e.g., 2 weeks or until semester midterms).
> - **Exchange:** A book-for-book barter where the requester offers a reciprocal book or study notes in exchange.
> - **Donate:** A permanent give-away, typically from seniors to juniors, promoting community reuse and zero waste.

### Q5: How is data consistency maintained when an owner accepts a request?
> **Answer:** When an owner clicks "Accept" on an interest request, an atomic SQL `UPDATE` statement sets the request status to `'Accepted'` and concurrently updates the book's `availability_status` in the `listings` table from `'Available'` to `'Pending Handover'`. This automatically alerts other students browsing the catalog that a handover is currently underway.

### Q6: How are passwords protected against security vulnerabilities?
> **Answer:** Passwords are never stored in plaintext. We utilize Werkzeug's cryptographic utilities `generate_password_hash()` and `check_password_hash()`. This implementation utilizes PBKDF2 with SHA-256 and unique cryptographic salts per user, mitigating rainbow table attacks and credential leakage.

### Q7: What are the future enhancements planned for BookBridge?
> **Answer:** Potential future extensions include:
> 1. Automated SMS / Email alerts via college SMTP when a request is submitted.
> 2. QR-code scan at the library desk to verify and timestamp physical handover completion.
> 3. AI-assisted syllabus matching to recommend relevant textbooks based on enrolled course electives.
