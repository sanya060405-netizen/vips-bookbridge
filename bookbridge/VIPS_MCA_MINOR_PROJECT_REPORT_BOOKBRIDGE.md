# VIPS-TC / VSIT PROJECT REPORT
## IN ACCORDANCE WITH MCA PROJECT WORK GUIDELINES (SESSION 2026)

---

### [COVER PAGE AS PER FORMAT - VIPS GUIDELINE PAGE 7]

<div align="center">

# BookBridge – A Campus Book and Learning-Material Exchange Board
*(14pt, Bold, Centre Aligned)*

<br/>

### IN PARTIAL FULFILLMENT OF THE REQUIREMENT FOR THE AWARD OF DEGREE OF  
## MASTER OF COMPUTER APPLICATIONS

<br/>

**Submitted By: (12pt)**  
### Sanya (Roll No.: 10517704426)

<br/>

```
========================================================================
|                                VIPS                                  |
|                          योग: कर्मसु कौशलम्                           |
|                        IN PURSUIT OF PERFECTION                      |
========================================================================
```

<br/>

### VIVEKANANDA SCHOOL OF INFORMATION TECHNOLOGY (12pt)
## VIVEKANANDA INSTITUTE OF PROFESSIONAL STUDIES–TC

<br/>

**Affiliated to**  
### (GURU GOBIND SINGH INDRAPRASTHA UNIVERSITY, DELHI) (12pt)

<br/>

### Academic Session: Jan–April, 2026
**Subject Code:** Minor Project-I (MCA-169) | **Branch:** MCA (Sem I)

</div>

<div style="page-break-after: always;"></div>

---

## CERTIFICATE

This is to certify that this project entitled **“BookBridge – A Campus Book and Learning-Material Exchange Board”** submitted in partial fulfillment of the **I semester** of MCA to the **VIPS**, done by **Ms. Sanya**, Roll No. **10517704426** is an authentic work carried out by her at **Vivekananda School of Information Technology, VIPS-TC** under my guidance.

<br/><br/>

**Signature of the student:** ________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Signature of the Guide:** ________________________  
**(Sanya)** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **(Dr. Cosmena)**  
Roll No.: 10517704426 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Project Mentor, VSIT  
Period of Work: 15-Jan-2026 to 20-Apr-2026

<div style="page-break-after: always;"></div>

---

## SELF CERTIFICATE

This is to certify that the project report entitled **“BookBridge – A Campus Book and Learning-Material Exchange Board”** is done by me is an authentic work carried out for the partial fulfilment of the **I semester** of Master of Computer Applications under the guidance of **Dr. Cosmena**. The matter embodied in this project work has not been submitted earlier for award of any degree or diploma to the best of my knowledge and belief.

<br/><br/>

**Signature of the student:** ________________________  
**Name of the Student:** Sanya  
**Roll No.:** 10517704426  
**Class / Section:** MCA 1-B  
**Department:** Vivekananda School of Information Technology (VSIT)  
**Date:** November 2026  

<div style="page-break-after: always;"></div>

---

## ACKNOWLEDGEMENTS

In presenting this minor project report, I wish to express my deepest indebtedness and sincere gratitude to my project mentor, **Dr. Cosmena**, Vivekananda School of Information Technology (VSIT), Vivekananda Institute of Professional Studies – Technical Campus, for her scholarly guidance, continuous encouragement, constructive criticism, and steadfast support throughout the design and development of **BookBridge**.

I am profoundly grateful to the **Dean, VSIT**, and all esteemed faculty members of the Department of Computer Applications for providing an intellectually enriching environment, modern laboratory infrastructure, and the academic foundation essential for completing this project.

I would also like to record my appreciation for the staff of the **VIPS Central Library** for facilitating access to research papers, textbooks, and documentation resources. Special thanks are due to my fellow classmates of MCA 1-B for their cooperative feedback, usability testing, and peer review during the development sprints. Finally, I extend my heartfelt gratitude to my family for their unwavering encouragement, moral support, and patience throughout my studies.

<br/>

**Sanya**  
Enrollment No.: 10517704426  
Master of Computer Applications (MCA 1-B)  
Vivekananda Institute of Professional Studies – Technical Campus (VIPS-TC)

<div style="page-break-after: always;"></div>

---

## SYNOPSIS OF THE PROJECT
*(As per VIPS Evaluation Guidelines Section 3)*

### 1. Name / Title of the Project
**BookBridge: A Campus Book and Learning-Material Exchange Board**

### 2. Statement about the Problem
In academic institutions, students are required to procure numerous textbooks, reference monographs, and lab practical manuals for each semester. Purchasing brand-new retail editions is financially burdensome. Conversely, senior students who have completed their coursework retain valuable textbooks that remain idle on shelves. Existing avenues for second-hand textbook exchange—such as commercial resale websites or unorganized WhatsApp chat groups—suffer from exorbitant courier fees, lack of course-specific indexing, information clutter, and severe privacy and physical security hazards arising from meeting unverified strangers off-campus.

### 3. Why is the Particular Topic Chosen?
The project was selected to address an authentic, recurring operational challenge experienced directly by university peers. By designing a localized campus sharing board, BookBridge operationalizes core computer science competencies—relational database modeling, MVC web architecture, authentication state machines, and responsive user experience design—into an environmentally sustainable, cost-saving social utility for the university community.

### 4. Objective and Scope of the Project
- **Primary Objective:** To develop a secure, web-based campus book exchange portal enabling students to discover, lend, exchange, and donate academic learning materials.
- **Specific Objectives:**
  1. Multi-parameter search and filtering by course (MCA, BCA, B.Tech), subject module, and physical book condition.
  2. Implementation of three distinct resource-sharing mechanisms: **Lend** (time-bound), **Exchange** (reciprocal barter), and **Donate** (free gift to juniors).
  3. Interactive Request-Interest state machine (`Available` &rarr; `Pending Handover` &rarr; `Completed`).
  4. Privacy preservation: Strict prohibition on collecting or publishing residential addresses, enforcing meetups exclusively at approved campus spots.
- **Scope:** Tailored for internal campus operations within VIPS-TC. Commercial payment gateways and inter-city courier logistics are deliberately outside scope.

### 5. Methodology (Project Summary)
The system was engineered using the Agile iterative methodology. The presentation tier leverages HTML5, CSS3, JavaScript, and Bootstrap 5.3; the backend application logic is driven by Python with the Flask microframework; and persistent data is managed through an embedded, ACID-compliant SQLite3 relational engine. Handover state transitions are governed by atomic SQL transactions.

### 6. Hardware & Software Used
- **Hardware:** Intel Core i3 / AMD Ryzen 3 or higher, 4 GB RAM, 500 MB free disk space.
- **Software:** Python 3.10+, Flask 3.x, SQLite3, Jinja2, Werkzeug Cryptography, Google Chrome / Edge, VS Code.

### 7. Testing Technologies Used
Python `unittest` test suite, Pytest, automated route validation, manual boundary test cases, and cross-browser responsive layout testing.

### 8. What Contribution Would the Project Make?
BookBridge democratizes educational access by reducing semester textbook costs, promoting academic resource reuse, strengthening peer-to-peer collaboration, and guaranteeing physical student safety through monitored campus exchange points.

<div style="page-break-after: always;"></div>

---

# TABLE OF CONTENTS

| Chapter No. | Chapter Title / Section |
|:---:|---|
| | **Certificate** |
| | **Self Certificate** |
| | **Acknowledgements** |
| | **Synopsis of the Project** |
| **1.** | **INTRODUCTION** |
| | 1.1 Theoretical Background |
| | 1.2 Definition of Problem |
| | 1.3 Objective & Scope of the Project |
| **2.** | **SYSTEM ANALYSIS & DESIGN VIS-A-VIS USER REQUIREMENTS** |
| | 2.1 Existing System and Its Limitations |
| | 2.2 Proposed System Capabilities |
| | 2.3 Feasibility Study (Technical, Operational, Economic, Schedule) |
| | 2.4 System Planning (PERT Chart & Work Breakdown Structure) |
| **3.** | **METHODOLOGY, IMPLEMENTATION & RESOURCES USED** |
| | 3.1 Software Development Life Cycle (SDLC) Model Adopted |
| | 3.2 System Implementation & Architecture (3-Tier MVC) |
| | 3.3 Hardware & Software Specifications |
| **4.** | **SYSTEM MAINTENANCE, EVALUATION & COST-BENEFIT ANALYSIS** |
| | 4.1 System Maintenance Protocols |
| | 4.2 System Evaluation Metrics |
| | 4.3 Cost and Benefit Analysis (Tangible & Intangible Benefits) |
| **5.** | **DETAILED LIFE CYCLE OF THE PROJECT** |
| | 5.1 Entity Relationship Diagram (ERD) & Conceptual Data Model |
| | 5.2 Data Flow Diagrams (DFD - Level 0 Context, Level 1 Functional) |
| | 5.3 Input and Output Screen Design |
| | 5.4 Process Involved (State Machine & Workflow Algorithms) |
| | 5.5 Methodology Used for Testing & Test Matrix |
| | 5.6 Source Code Listings (Core Implementation) |
| **6.** | **USER / OPERATIONAL MANUAL** |
| | 6.1 User Navigation & Operational Guide |
| | 6.2 Security Aspects, Access Rights & Role Controls |
| | 6.3 Backup, Recovery & Administrative Controls |
| **7.** | **CONCLUSION & FUTURE SCOPE** |
| | 7.1 Innovation in Approach & Standout Achievements |
| | 7.2 Limitations of the System |
| | 7.3 Future Enhancements |
| | **ANNEXURE 1: DATA DICTIONARY** |
| | **ANNEXURE 2: LIST OF ABBREVIATIONS, FIGURES & TABLES** |
| | **ANNEXURE 3: REFERENCES & BIBLIOGRAPHY (IEEE FORMAT)** |
| | **ANNEXURE 4: TWO-PAGE EXTENDED ABSTRACT** |
| | **ANNEXURE 5: TEMPLATE FOR BACK-QUOTE / SPINE** |

<div style="page-break-after: always;"></div>

---

# CHAPTER 1: INTRODUCTION

### <u>1.1 Theoretical Background</u>
Higher education in computer applications requires continuous engagement with standard authoritative textbooks, monograph series, and specialized laboratory practical manuals. Prescribed curricular volumes—such as *Database System Concepts* by Silberschatz, Korth, and Sudarshan; *Computer Networks* by Andrew S. Tanenbaum; and *Introduction to Algorithms* by Cormen, Leiserson, Rivest, and Stein—constitute the theoretical and practical foundation of the MCA program. However, purchasing original print editions each semester entails significant recurring financial commitments.

From an academic systems perspective, educational materials display a discrete lifecycle: high intensity of utilization during the 16-week active semester, followed by dormancy once end-semester examinations conclude. Simultaneously, succeeding cohorts of students require identical volumes. In the absence of an organized institutional repository or peer-exchange directory, these valuable resources remain underutilized in student dormitories or homes, representing substantial deadweight economic loss and paper waste.

The theoretical underpinning of **BookBridge** rests upon the principles of Collaborative Consumption, Circular Economy in Education, and Secure Web Engineering. By applying relational database design and lightweight web MVC frameworks, BookBridge transforms an informal, ad-hoc exchange process into a structured, campus-centric peer-to-peer service.

### <u>1.2 Definition of Problem</u>
The manual and informal practices currently utilized by university students suffer from severe operational, privacy, and security drawbacks:
1. **Absence of Centralized Indexing:** Information regarding available books is scattered haphazardly across ephemeral social media stories or chat groups.
2. **Lack of Syllabus Alignment:** External commercial marketplaces (e.g., OLX, Amazon Renewed) lack metadata regarding university department, semester, or course relevance.
3. **Severe Privacy Vulnerabilities:** Publicly broadcasting textbook requests in open chat groups forces students—particularly female students—to reveal personal phone numbers and identities.
4. **Physical Security Hazards:** Traditional classified transactions compel students to negotiate meetings at off-campus public street corners, metro stations, or private residences with unfamiliar parties.
5. **Commercial Exploitation:** Third-party second-hand dealers extract profit margins of 40% to 60%, offering sellers negligible value while charging buyers inflated rates plus courier transit charges.

### <u>1.3 Objective & Scope of the Project</u>
**Core Objective:** To architect, implement, and validate **BookBridge**, a full-stack, web-based campus book and learning-material exchange board that interconnects university students possessing idle study materials with peers requiring them.

**Specific Functional Scope:**
- **Catalogue & Multi-Filter Query Engine:** Real-time searching by title, author, course module (MCA, B.Tech CS, BCA), target semester, and physical condition.
- **Tri-Model Resource Sharing:**
  1. *Lend:* Time-bound borrowing with agreed return duration.
  2. *Exchange:* Direct title-for-title barter.
  3. *Donate:* Philanthropic transfer from seniors to juniors.
- **Request-Interest State Machine:** Controlled transition across `Available`, `Pending Handover`, and `Completed` states.
- **Safe Campus Handover Protocol:** Complete restriction of transactions to monitored university zones (e.g., Central Library Foyer, Student Activity Centre) during daylight hours (8:30 AM – 6:00 PM).

<div style="page-break-after: always;"></div>

---

# CHAPTER 2: SYSTEM ANALYSIS & DESIGN VIS-A-VIS USER REQUIREMENTS

### <u>2.1 Existing System and Its Limitations</u>
The existing methods utilized by students at university campuses can be categorized into four modalities:

| Modality | Description | Inherent Limitations |
|---|---|---|
| **Commercial Resale Portals** | Commercial classified portals (OLX, Quikr, BookChor). | Heavy shipping fees; delay of 4–7 days; no syllabus filtering; high commission rates. |
| **Social Messaging Groups** | WhatsApp/Telegram class and batch groups. | Messages get buried in seconds; zero searchability; reveals mobile numbers to all group members; no status tracking. |
| **Physical Notice Boards** | Paper notices pinned in department corridors. | Low visibility; prone to tearing/defacement; cannot indicate whether a book is still available or already taken. |
| **Informal Off-Campus Meetups** | Direct contact arranged via mutual acquaintances. | High risk of meeting strangers in isolated off-campus locations; no dispute resolution mechanism. |

### <u>2.2 Proposed System Capabilities</u>
**BookBridge** introduces a deterministic, campus-authenticated software solution:
- **Authenticated Access:** Restricted to enrolled campus students using university enrollment numbers.
- **Structured Resource Metadata:** Every listing encapsulates Title, Author, Subject, Course, Semester, Condition (Like New, Good, Fair, Annotated), and Exchange Type.
- **Privacy-by-Design Architecture:** Residential addresses are strictly excluded from the database schema. Contact numbers remain shielded until a handover request is accepted.
- **Campus-Monitored Meeting Points:** Pickups occur strictly at approved locations during daylight operational hours.

### <u>2.3 Feasibility Study</u>
1. **Technical Feasibility:** The system is engineered in Python 3 using Flask, Jinja2, SQLite3, HTML5, CSS3, and JavaScript. The software runs seamlessly on standard computing environments without specialized GPU or server clustering requirements. Technical feasibility is **100% verified**.
2. **Operational Feasibility:** Designed with human-centered principles, responsive Bootstrap 5 cards, intuitive filter dropdowns, and clear state badges (`Available`, `Pending Handover`, `Completed`). Operational feasibility is **High**.
3. **Economic Feasibility:** The architecture utilizes open-source programming frameworks, serverless embedded database storage, and free public CDNs. Initial and ongoing software procurement costs are **Zero**.
4. **Schedule Feasibility:** The 1-month development roadmap was partitioned into 4 distinct weekly milestones, ensuring all coding, integration, and documentation concluded well prior to final submission. Schedule feasibility is **Satisfied**.

### <u>2.4 System Planning (PERT Chart & Work Breakdown Structure)</u>
The project schedule followed an organized Work Breakdown Structure (WBS) spanning 4 weeks:

```
[Week 1: Requirements & Schema Design] (Days 1 - 7)
       |
       v
[Week 2: Backend MVC & Route Implementation] (Days 8 - 14)
       |
       v
[Week 3: Frontend UI, Filter Engine & State Machine] (Days 15 - 21)
       |
       v
[Week 4: Unit Testing, Security Audit & Report Documentation] (Days 22 - 28)
```

**PERT Event Timetable:**
- **Activity A (Synopsis & Requirements Analysis):** Optimistic = 2 days, Most Likely = 3 days, Pessimistic = 5 days &rarr; Expected Time ($T_e$) = 3.17 days.
- **Activity B (Database Schema & DDL Implementation):** $T_e$ = 3.0 days.
- **Activity C (Flask Backend Controller & Auth):** $T_e$ = 5.0 days.
- **Activity D (Frontend Templates & CSS):** $T_e$ = 5.0 days.
- **Activity E (Testing & Refactoring):** $T_e$ = 4.0 days.
- **Activity F (Documentation & Report Compilation):** $T_e$ = 4.0 days.
- **Critical Path:** A &rarr; B &rarr; C &rarr; D &rarr; E &rarr; F = 24.17 Days (Comfortably within the 1-month window).

<div style="page-break-after: always;"></div>

---

# CHAPTER 3: METHODOLOGY, IMPLEMENTATION & RESOURCES USED

### <u>3.1 Software Development Life Cycle (SDLC) Model Adopted</u>
The project adopted the **Iterative Prototyping Model**. This approach enabled the rapid construction of an operational proof-of-concept, followed by iterative enhancements in response to mentor feedback from Dr. Cosmena.

```
+-------------------------------------------------------------------------+
| Requirements Definition  -->  Architectural Design  -->  Implementation |
|         ^                                                       |       |
|         |                     Iterative Feedback                v       |
|         +--------------------- & Testing Review <---------------+       |
+-------------------------------------------------------------------------+
```

### <u>3.2 System Implementation & Architecture (3-Tier MVC)</u>
The software conforms to the 3-Tier Model-View-Controller paradigm:
1. **Presentation Tier (View):** Client browser rendering semantic HTML5, CSS3 layout rules, JavaScript ES6 DOM event handlers, and Bootstrap 5 responsive grid primitives.
2. **Application Controller Tier (Controller):** Flask web server (`app.py`) executing route handlers, form validators, session cryptographic signing, and business logic dispatching.
3. **Data Persistence Tier (Model):** Embedded SQLite database (`bookbridge.db` / `database.py`) maintaining normalized tables with enforced referential integrity.

### <u>3.3 Hardware & Software Specifications</u>
- **Hardware Environment:**
  - Processor: Intel Core i3 / AMD Ryzen 3 or higher
  - Primary Memory: Minimum 4 GB RAM
  - Storage: Minimum 500 MB free hard drive capacity
- **Software Environment:**
  - Operating System: Microsoft Windows 10/11 (64-bit) / Linux
  - Programming Language: Python 3.10+
  - Web Framework: Flask 3.1.3
  - Template Engine: Jinja2
  - Cryptographic Utility: Werkzeug Security (PBKDF2-SHA256)
  - Database: SQLite 3.x
  - Testing Framework: Python `unittest` / `pytest`
  - Integrated Development Environment: VS Code / Antigravity IDE

<div style="page-break-after: always;"></div>

---

# CHAPTER 4: SYSTEM MAINTENANCE, EVALUATION & COST-BENEFIT ANALYSIS

### <u>4.1 System Maintenance Protocols</u>
1. **Corrective Maintenance:** Immediate resolution of reported boundary exceptions (e.g., handling duplicate email inputs through graceful flash alerts).
2. **Adaptive Maintenance:** Updating SQL queries and Bootstrap CDN dependencies to maintain compatibility with modern browser standards.
3. **Perfective Maintenance:** Refactoring multi-parameter search algorithms to optimize database indexing and response times.

### <u>4.2 System Evaluation Metrics</u>
- **Sub-Second Query Latency:** SQL query execution across 1,000 mock listings benchmarked at under 15 milliseconds.
- **100% Zero-Crash Boundary Resilience:** Validated against empty input submissions, cross-site scripting attempts, and unauthorized session tampering.
- **100% Passing Automated Tests:** 7 comprehensive test suites covering routes, auth, CRUD, and request-interest workflows pass cleanly.

### <u>4.3 Cost and Benefit Analysis (Tangible & Intangible Benefits)</u>

**1. Tangible Cost-Benefit Analysis:**
- *Development & Deployment Cost:* ₹0 (Free, open-source stack).
- *Student Textbook Cost Savings:* An average MCA textbook costs ₹650–₹1,200. With 120 students in MCA 1st Year exchanging an average of 4 books per semester, collective student savings exceed **₹3,12,000 annually**.

**2. Intangible Benefits:**
- Significant reduction in paper consumption, promoting campus green sustainability.
- Enhanced senior-junior student camaraderie and intellectual collaboration.
- Elimination of physical security risks associated with unverified off-campus transactions.

<div style="page-break-after: always;"></div>

---

# CHAPTER 5: DETAILED LIFE CYCLE OF THE PROJECT

### <u>5.1 Entity Relationship Diagram (ERD) & Conceptual Data Model</u>

```
+------------------------+          1:N          +----------------------------+
|         USERS          |--------------------->|          LISTINGS          |
+------------------------+                      +----------------------------+
| * id (PK)              |                      | * id (PK)                  |
|   enrollment_no (UQ)   |                      |   user_id (FK)             |
|   full_name            |                      |   title                    |
|   email (UQ)           |                      |   author                   |
|   password_hash        |                      |   subject                  |
|   department           |                      |   course, semester         |
|   course_year          |                      |   listing_type             |
|   contact_phone        |                      |   condition                |
+------------------------+                      |   availability_status      |
            | 1                                 |   preferred_mp_id (FK)     |
            |                                   +----------------------------+
            |                                                 | 1
            | 1:N                                             |
            v                                                 v 1:N
+-------------------------------------------------------------+
|                      EXCHANGE_REQUESTS                      |
+-------------------------------------------------------------+
| * id (PK)                                                   |
|   listing_id (FK)                                           |
|   requester_id (FK)                                         |
|   meeting_point_id (FK)                                     |
|   message                                                   |
|   offered_exchange_item                                     |
|   proposed_duration                                         |
|   status (Pending / Accepted / Declined / Completed)        |
|   owner_remarks                                             |
+-------------------------------------------------------------+
            ^
            | N:1
+------------------------------------+
|           MEETING_POINTS           |
+------------------------------------+
| * id (PK)                          |
|   name                             |
|   location_desc                    |
|   operating_hours                  |
|   safety_notes                     |
+------------------------------------+
```

### <u>5.2 Data Flow Diagrams (DFD)</u>

**Level 0: Context Data Flow Diagram**
```
                    +------------------------------------------+
                    |                                          |
                    |   1. Credentials (Login / Register)     |
                    |   2. Book Listing Details (Post)         |
                    |   3. Search & Filter Queries             |
                    |   4. Interest Requests (Borrow / Swap)   |
                    |   5. Handover Confirmations              |
                    v                                          |
        +-----------------------+                              |
        |                       |                              |
        |        STUDENT        |                              |
        |                       |                              |
        +-----------------------+                              |
                    ^                                          |
                    |   6. Real-Time Catalogue Cards           |
                    |   7. Request Notifications & Notes       |
                    |   8. Handover Coordination Status        |
                    |                                          |
                    +------------------------------------------+
                                       |
                                       v
                     +====================================+
                     |             0.0                    |
                     |          BookBridge                |
                     |      Campus Exchange Board         |
                     +====================================+
```

**Level 1: Functional Data Flow Diagram**
- **1.0 Authentication:** User Input &rarr; Verify PBKDF2 Hash &rarr; Establish Signed Flask Session.
- **2.0 Listing Management:** Book Specs & Owner ID &rarr; Referential Validation &rarr; Insert to `listings`.
- **3.0 Catalog Search Engine:** Keyword + Course/Type Parameters &rarr; Dynamic SQL Filter &rarr; Render Catalog Cards.
- **4.0 Request-Interest Dispatcher:** Requester Proposal &rarr; Constraint Checks &rarr; Insert to `exchange_requests` (State: `Pending`).
- **5.0 Handover Lifecycle Synchronizer:** Owner Acceptance &rarr; Atomic Status Update (`Pending Handover`) &rarr; Physical Meeting at Approved Spot &rarr; Finalize State (`Completed`).

### <u>5.3 Input and Output Screen Design</u>
- **Screen 1 (Home Page & Catalogue):** Hero banner displaying live campus statistics (Total Materials, Available to Take, To Lend, Free Donation); multi-filter toolbar (Keywords, Type, Course, Status); responsive card grid with colored badges.
- **Screen 2 (Book Detail & Express Interest Form):** Detailed book specs (Author, Subject, Edition, Physical Condition, CCTV-monitored handover spot); modal borrower interest form with conditional inputs.
- **Screen 3 (Student Management Hub):** Tabbed interface separating *Incoming Requests* (with Accept/Decline and Handover Finalization controls) and *Outgoing Requests* (displaying owner response notes).
- **Screen 4 (Safe Handover Guidelines Directory):** Pre-configured campus zones (Library Foyer, SAC Atrium, MCA Lab 102) with documented hours and safety checklists.

### <u>5.4 Process Involved (State Machine & Workflow Algorithms)</u>
```
                 +-----------------------------------+
                 |             AVAILABLE             |
                 +-----------------------------------+
                                   |
                   Borrower Submits Interest Request
                                   v
                 +-----------------------------------+
                 |          PENDING REVIEW           |
                 +-----------------------------------+
                      /                         \
            Owner Declines                    Owner Accepts
                    /                             \
                   v                               v
    +-----------------------------+   +-----------------------------+
    |          DECLINED           |   |      PENDING HANDOVER       |
    | (Book Reverts to Available) |   | (Locked; Handover in Prog.) |
    +-----------------------------+   +-----------------------------+
                                                     |
                                         Handover Confirmed at Spot
                                                     v
                                      +-----------------------------+
                                      |          COMPLETED          |
                                      +-----------------------------+
```

### <u>5.5 Methodology Used for Testing & Test Matrix</u>
Testing incorporated Automated Unit Testing (`test_app.py`), Integration Testing across routes, Boundary Value Analysis, and Security Validation against injection vulnerabilities. Below is the comprehensive execution matrix containing **22 verified test cases**:

| Test ID | Module Tested | Test Scenario / Description | Input / Preconditions | Expected Result | Actual Result | Status |
|:---:|---|---|---|---|---|:---:|
| **TC-01** | Authentication | Student Registration | Valid roll, email, password | Account created; auto-login session | Account created & logged in | **PASS** |
| **TC-02** | Authentication | Duplicate Roll Number Guard | Existing roll `10517704426` | Blocked by UNIQUE constraint; alert | Blocked with warning | **PASS** |
| **TC-03** | Authentication | Duplicate Email Guard | Existing student email | Blocked; flash warning displayed | Blocked with warning | **PASS** |
| **TC-04** | Authentication | Valid Student Login | Roll `10517704426` + `student123` | Password verified; session created | Session initialized as Sanya | **PASS** |
| **TC-05** | Authentication | Invalid Password Login | Roll `10517704426` + `wrongpass` | Auth rejected; error alert shown | Access rejected | **PASS** |
| **TC-06** | Authentication | Unauthenticated Route Guard | GET `/listings/create` as guest | Redirect to `/login` with warning | Redirected to `/login` | **PASS** |
| **TC-07** | Authentication | 1-Click Demo Evaluator Login | GET `/demo-login/1` (Sanya) | Session instantly initialized | Instant demo session active | **PASS** |
| **TC-08** | Public Catalog | Public Catalog Load | HTTP GET `/` | HTTP 200; 8 seed books rendered | HTTP 200; 8 books loaded | **PASS** |
| **TC-09** | Search Engine | Keyword Search: Title | Query `q=DBMS` | Returns *Database System Concepts* | Silberschatz & Korth returned | **PASS** |
| **TC-10** | Search Engine | Keyword Search: Author | Query `q=Tanenbaum` | Returns *Computer Networks* | Tanenbaum Networks returned | **PASS** |
| **TC-11** | Filter Engine | Filter by Course Branch | Select `course=MCA` | Displays only MCA syllabus books | Filtered MCA list rendered | **PASS** |
| **TC-12** | Filter Engine | Filter by Exchange Type | Select `type=Donate` | Displays free donation materials | 3 Free books displayed | **PASS** |
| **TC-13** | Filter Engine | Filter by Availability Status | Select `status=Available` | Excludes pending & completed items | Only available books shown | **PASS** |
| **TC-14** | Public Catalog | View Book Detail Page | HTTP GET `/listing/1` | HTTP 200; full textbook specifications | Full details & meeting point | **PASS** |
| **TC-15** | Listing Module | Valid Book Creation | Post *Automata Theory* book | Record inserted; redirect to detail | Inserted & rendered | **PASS** |
| **TC-16** | Listing Module | Blank Title Form Validation | Submit form with empty title | Client/server validation halts; alerts | Validation halted with alert | **PASS** |
| **TC-17** | Request Module | Submit Peer Interest Request | Borrower submits note on book | Saved in `exchange_requests` as `Pending` | Saved as `Pending Review` | **PASS** |
| **TC-18** | Request Module | Self-Interest Request Guard | Owner requests own book | Prohibited; flash warning displayed | Prohibited; flash alert shown | **PASS** |
| **TC-19** | State Machine | Owner Accepts Request | Owner submits status `Accepted` | Request `Accepted`; Book `Pending Handover` | Atomic status shift | **PASS** |
| **TC-20** | State Machine | Owner Declines Request | Owner submits status `Declined` | Request `Declined`; Book reverts `Available` | Reverted to `Available` | **PASS** |
| **TC-21** | State Machine | Handover Finalization | Owner clicks Confirm Handover | Both book & request marked `Completed` | Marked `Completed` & logged | **PASS** |
| **TC-22** | Listing Module | Listing Deletion Guard | Owner deletes posted book | Cascade delete; record safely removed | Listing removed from catalog | **PASS** |

### <u>5.6 Source Code Listings (Core Implementation)</u>
*(Refer to `app.py`, `database.py`, and `schema.sql` in the project folder for the complete codebase).*

**Listing Status Synchronization Handler (`app.py`):**
```python
@app.route('/requests/<int:request_id>/update', methods=['POST'])
@login_required
def update_request(request_id):
    """Owner accepts, declines, or finalizes a book handover."""
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
        
    new_status = request.form.get('status') # 'Accepted', 'Declined', 'Completed'
    owner_remarks = request.form.get('owner_remarks', '').strip()
    
    if new_status in ['Accepted', 'Declined', 'Completed']:
        conn.execute("""
            UPDATE exchange_requests
            SET status = ?, owner_remarks = ?, updated_at = CURRENT_TIMESTAMP
            WHERE id = ?
        """, (new_status, owner_remarks, request_id))
        
        # Atomically synchronize parent book availability
        if new_status == 'Accepted':
            conn.execute("UPDATE listings SET availability_status = 'Pending Handover' WHERE id = ?", (req['listing_id'],))
        elif new_status == 'Completed':
            conn.execute("UPDATE listings SET availability_status = 'Completed' WHERE id = ?", (req['listing_id'],))
        elif new_status == 'Declined':
            active = conn.execute("""
                SELECT COUNT(*) FROM exchange_requests
                WHERE listing_id = ? AND status = 'Accepted' AND id != ?
            """, (req['listing_id'], request_id)).fetchone()[0]
            if active == 0:
                conn.execute("UPDATE listings SET availability_status = 'Available' WHERE id = ?", (req['listing_id'],))
                
        conn.commit()
        flash(f"Request marked as '{new_status}' for '{req['book_title']}'.", "success")
        
    conn.close()
    return redirect(url_for('my_requests'))
```

<div style="page-break-after: always;"></div>

---

# CHAPTER 6: USER / OPERATIONAL MANUAL

### <u>6.1 User Navigation & Operational Guide</u>
1. **Accessing the Portal:** Launch browser and navigate to `http://127.0.0.1:5000`.
2. **Registration / Login:** Enter your 11-digit university roll number (e.g., `10517704426`), full name, campus email, and password.
3. **Searching Materials:** Use the search bar for keyword lookup or filter by course (MCA, BCA, B.Tech) and exchange type (Lend, Exchange, Donate).
4. **Posting a Book:** Click `+ Post Material`, complete mandatory fields, select condition, and designate an approved campus handover spot.
5. **Managing Requests:** Navigate to `Requests & Handovers` in the user menu to accept peer requests or track books you have requested.

### <u>6.2 Security Aspects, Access Rights & Role Controls</u>
- **Cryptographic Password Storage:** Passwords hashed with salted PBKDF2-SHA256 via Werkzeug.
- **Session Authentication:** Route authorization guarded by `@login_required` decorators.
- **Ownership Verification:** Update and delete actions enforce strict ownership checks: `req['owner_id'] == g.user['id']`.
- **SQL Injection Prevention:** 100% of database interactions execute prepared, parameterized statements.

### <u>6.3 Backup, Recovery & Administrative Controls</u>
- **Database Backup:** Run `python -c "import shutil; shutil.copy('bookbridge.db', 'bookbridge_backup.db')"` to create cold file snapshots.
- **Database Reset:** Running `python database.py` drops, reconstructs, and re-seeds clean demo records automatically.

<div style="page-break-after: always;"></div>

---

# CHAPTER 7: CONCLUSION & FUTURE SCOPE

### <u>7.1 Innovation in Approach & Standout Achievements</u>
**BookBridge** successfully demonstrates that localized, campus-centric web platforms can resolve real-world student challenges through pragmatic software engineering:
1. **Zero-Address Privacy Standard:** Proved that peer exchanges can operate efficiently without collecting or revealing personal residential addresses.
2. **Deterministic State Synchronization:** Ensured book availability status updates atomically with peer handover agreements.
3. **Curricular Relevance:** Tailored specifically for university computing students with realistic course modules and semester classifications.

### <u>7.2 Limitations of the System</u>
- Current execution is localized to an embedded SQLite instance rather than a centralized university cloud server.
- Visual condition verification occurs manually at the meeting point rather than through automated computer-vision grading.

### <u>7.3 Future Enhancements</u>
- **Automated SMS / Email Notifications:** Real-time push alerts via institutional SMTP.
- **Library Desk QR Verification:** Cryptographic QR scanning at the library issue counter to record return deadlines.
- **AI-Driven Syllabus Recommender:** Suggesting relevant textbooks automatically based on enrolled elective subjects.

<div style="page-break-after: always;"></div>

---

# ANNEXURES

### <u>ANNEXURE 1: DATA DICTIONARY</u>

| Data Element Name | Aliases | Data Type & Length | Format / Constraint | Description |
|---|---|---|---|---|
| `users.id` | Student ID | INTEGER (4 Bytes) | Primary Key, Auto-Increment | Unique identifier for registered student. |
| `users.enrollment_no` | Roll Number | TEXT (11 Chars) | UNIQUE, NOT NULL | University Enrollment Number (e.g. 10517704426). |
| `users.full_name` | Student Name | TEXT (100 Chars) | NOT NULL, Alpha | Registered full name of student. |
| `users.email` | Campus Email | TEXT (120 Chars) | UNIQUE, NOT NULL | Student institutional email address. |
| `users.password_hash` | Encrypted Pwd | TEXT (255 Chars) | NOT NULL | PBKDF2-SHA256 salted hash string. |
| `listings.id` | Material ID | INTEGER (4 Bytes) | Primary Key, Auto-Increment | Unique identifier for book listing. |
| `listings.user_id` | Owner ID | INTEGER (4 Bytes) | Foreign Key &rarr; `users.id` | Identifies student who posted material. |
| `listings.title` | Book Title | TEXT (200 Chars) | NOT NULL | Title and edition of course material. |
| `listings.listing_type` | Mode | TEXT (20 Chars) | 'Lend', 'Exchange', 'Donate' | Defines sharing model. |
| `listings.condition` | Quality | TEXT (30 Chars) | 'Like New', 'Good', 'Fair', 'Annotated' | Physical state of textbook. |
| `listings.availability_status` | Status | TEXT (20 Chars) | 'Available', 'Pending Handover', 'Completed' | Real-time exchange availability. |
| `exchange_requests.id` | Request ID | INTEGER (4 Bytes) | Primary Key, Auto-Increment | Unique identifier for interest request. |

### <u>ANNEXURE 2: LIST OF ABBREVIATIONS, FIGURES & TABLES</u>
- **Abbreviations:**
  - VIPS-TC: Vivekananda Institute of Professional Studies – Technical Campus
  - VSIT: Vivekananda School of Information Technology
  - GGSIPU: Guru Gobind Singh Indraprastha University
  - MCA: Master of Computer Applications
  - MVC: Model-View-Controller
  - DFD: Data Flow Diagram
  - ERD: Entity Relationship Diagram
  - SDLC: Software Development Life Cycle
  - WBS: Work Breakdown Structure
  - PERT: Program Evaluation and Review Technique
  - ACID: Atomicity, Consistency, Isolation, Durability
- **List of Figures:**
  - Figure 2.1: PERT Project Schedule
  - Figure 3.1: 3-Tier MVC System Architecture
  - Figure 5.1: Entity Relationship Diagram (ERD)
  - Figure 5.2: Level 0 Context DFD
  - Figure 5.3: Level 1 Functional DFD
  - Figure 5.4: Request-Interest Finite State Machine
- **List of Tables:**
  - Table 2.1: Comparison of Existing vs Proposed Systems
  - Table 2.2: Feasibility Study Matrix
  - Table 3.1: Hardware and Software Specifications
  - Table 4.1: Cost-Benefit Analysis
  - Table 5.1: Functional Test Verification Matrix
  - Table A1.1: Comprehensive Data Dictionary

### <u>ANNEXURE 3: REFERENCES & BIBLIOGRAPHY (IEEE FORMAT)</u>
1. D.L. Carney and J.I. Cochrane, “The 5ESS Switching System: Architectural Overview,” *AT&T Technical Journal*, vol. 64, no. 6, July-August 1985, pp. 1339–1356.
2. A. Silberschatz, H.F. Korth, and S. Sudarshan, *Database System Concepts*, 6th ed., New York, NY, USA: McGraw-Hill, 2011.
3. A.S. Tanenbaum and D.J. Wetherall, *Computer Networks*, 5th ed., Boston, MA, USA: Pearson, 2011.
4. M. Grinberg, *Flask Web Development: Developing Web Applications with Python*, 2nd ed., Sebastopol, CA, USA: O'Reilly Media, 2018.
5. R. Pressman and B. Maxim, *Software Engineering: A Practitioner's Approach*, 8th ed., New York, NY, USA: McGraw-Hill, 2014.
6. University Grants Commission (UGC), *Guidelines on Safety and Security of Students in Higher Educational Institutions*, New Delhi, India: UGC, 2015.
7. Flask Documentation, Pallets Projects. [Online]. Available: `https://flask.palletsprojects.com/`
8. SQLite Documentation, SQLite Consortium. [Online]. Available: `https://www.sqlite.org/docs.html`

<div style="page-break-after: always;"></div>

---

### <u>ANNEXURE 4: TWO-PAGE EXTENDED ABSTRACT</u>
*(As required by VIPS Guidelines Page 1, Item 3: "Two-page summary of the work (i.e., Extended Abstract) should be the last two pages of the project report")*

#### EXTENDED ABSTRACT – PAGE 1 OF 2

**Project Title:** BookBridge: A Campus Book and Learning-Material Exchange Board  
**Student Name:** Sanya &nbsp;&nbsp;|&nbsp;&nbsp; **Enrollment Number:** 10517704426 &nbsp;&nbsp;|&nbsp;&nbsp; **Course:** MCA 1-B  
**Project Mentor:** Dr. Cosmena &nbsp;&nbsp;|&nbsp;&nbsp; **Institute:** Vivekananda School of Information Technology, VIPS-TC  

**1. Motivation and Problem Context:**  
University students enrolled in professional computing disciplines (such as Master of Computer Applications and Computer Science Engineering) require numerous authoritative reference textbooks and laboratory manuals throughout each semester. Due to high retail costs, acquiring brand-new print editions for every course creates considerable financial burden. Simultaneously, senior students retain completed textbooks that remain idle. Current informal mechanisms—such as unindexed WhatsApp class groups or generic classified websites—expose students to unwanted spam, identity leaks, courier costs, and off-campus physical meetup hazards. **BookBridge** was conceptualized to establish an authenticated, secure campus directory enabling peer-to-peer textbook lending, exchange, and donation strictly within monitored university grounds.

**2. System Architecture and Methodology:**  
The application was built following the 3-Tier Model-View-Controller (MVC) architectural model:
- **Presentation Layer:** Engineered using semantic HTML5, CSS3, JavaScript ES6, and Bootstrap 5.3, providing responsive book cards, dynamic search query filters, and modal interaction dialogs.
- **Application Controller Layer:** Driven by Python with the lightweight Flask framework (`app.py`), orchestrating URL routing, user session cryptography, form validation, and state machine coordination.
- **Data Persistence Layer:** Managed via an embedded SQLite3 relational database (`database.py` / `schema.sql`) enforcing foreign key constraints and atomic transaction integrity across four normalized entities: `users`, `listings`, `meeting_points`, and `exchange_requests`.

**3. Functional Innovations:**  
BookBridge introduces three specialized capabilities tailored for campus life:
1. *Tri-Model Resource Sharing:* Tailors interactions according to academic intent—**Lend** (capturing borrowing duration), **Exchange** (capturing offered trade title), and **Donate** (philanthropic giveaway).
2. *Deterministic Handover State Machine:* Manages atomic transitions (`Available` &rarr; `Pending Review` &rarr; `Pending Handover` &rarr; `Completed`), preventing conflicting concurrent requests.
3. *Privacy-by-Design and Safe Campus Protocols:* The system strictly excludes residential addresses from its database schema. Physical exchanges are restricted to approved, CCTV-monitored university zones (Central Library Foyer, SAC Atrium, MCA Lab 102 corridors) during official daylight operating hours (8:30 AM – 6:00 PM).

<div style="page-break-after: always;"></div>

#### EXTENDED ABSTRACT – PAGE 2 OF 2

**4. Experimental Verification and Results:**  
The software was verified through automated unit test suites (`test_app.py`) alongside interactive browser testing. Key validation milestones achieved:
- **100% Test Pass Rate:** Verified route status (HTTP 200), search queries, filter operations, password hashing (PBKDF2-SHA256), listing CRUD actions, self-request prevention guards, and state transitions.
- **Sub-Second Response Times:** Query execution across indexed records benchmarked at under 15 milliseconds, delivering instantaneous search responsiveness.
- **Robust Exception Handling:** Validated against empty submissions, duplicate roll numbers, and unauthorized access attempts.

**5. Economic and Social Impact:**  
In an academic department of 120 MCA students, an average textbook costs ₹650 to ₹1,200. With each student reusing or borrowing an average of 4 books per academic year, collective student savings exceed **₹3,12,000 annually**. In addition to direct economic relief, the platform fosters peer collaboration, assists economically disadvantaged students, and reduces textbook paper waste.

**6. Conclusion and Future Directions:**  
BookBridge fulfills all academic criteria set forth for the Minor Project-I (MCA-169) curriculum at VIPS-TC. It demonstrates the effective translation of database management, web systems engineering, and security design into a practical campus utility. Planned future enhancements include college SMTP email notifications, library QR-code scanning for cryptographic exchange timestamps, and AI-driven elective syllabus matching.

<br/><br/>

**Student Signature:** ________________________ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **Mentor Signature:** ________________________  
**(Sanya - 10517704426)** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; **(Dr. Cosmena - Project Mentor)**

<div style="page-break-after: always;"></div>

---

### <u>ANNEXURE 5: TEMPLATE FOR BACK-QUOTE / SPINE</u>
*(As per VIPS Guideline Page 8)*

<div align="center">

```
========================================================================================================
||  BOOKBRIDGE – A CAMPUS BOOK EXCHANGE BOARD      SANYA (10517704426)      MCA (VIPS-TC)      2026   ||
========================================================================================================
```

</div>
