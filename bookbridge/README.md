# BookBridge: A Campus Book and Learning-Material Exchange Board

> **MCA 1st Year Academic Mini-Project**  
> **Student Name:** Sanya  
> **Enrollment Number:** 10517704426  
> **Course / Section:** Master of Computer Applications (MCA 1-B)  
> **Project Mentor:** Dr. Cosmena  

---

## 1. Project Overview & Problem Statement
Textbooks, reference manuals, and semester notes represent a recurring cost for university students. After exams conclude, these valuable materials often sit unused in dorms or study desks. 

**BookBridge** is a web-based campus exchange board developed using **Python (Flask)**, **SQLite**, and **Bootstrap 5 / JavaScript**. It connects students within the campus community who possess idle learning materials with peers who need them. The platform supports **Lending**, **Book-for-Book Exchange**, and **Free Donation**, backed by an interactive **Request-Interest Workflow** and strict **Safe Campus Handover Guidelines** at monitored university locations.

---

## 2. Key Features

- **Searchable Course Material Catalogue:**
  - Real-time search across Book Titles, Authors, Course Modules, and Keywords.
  - Multi-parameter filtering by **Exchange Type** (*Lend*, *Exchange*, *Donate*), **Course** (*MCA*, *B.Tech CS*, *BCA*), and **Availability Status** (*Available*, *Pending Handover*, *Completed*).

- **Three Exchange Models:**
  1. **Lend:** Students can lend reference books for a designated period (e.g. 2–4 weeks or until midterm exams).
  2. **Exchange:** Students can swap books with reciprocal course materials.
  3. **Donate:** Seniors or graduating students can give away syllabus books and lab manuals for free to juniors.

- **Request-Interest Workflow:**
  - Students submit an interest request stating their need, proposed borrowing duration, or trade item.
  - Owners receive requests in real-time on their **Requests Hub** to *Accept* or *Decline*.
  - When accepted, the book automatically shifts to **Pending Handover**, and mutual contact details are unlocked.

- **Safe Campus Handover Protocols:**
  - Avoids publishing private residential addresses or personal numbers.
  - Requires handovers to occur at designated, high-visibility campus spots (e.g. *Central Library Foyer*, *Student Activity Centre / SAC*, *MCA Lab 102 Corridors*, *Cafeteria Gazebo*).
  - Defined daylight hours (8:30 AM – 6:00 PM) and visual condition inspection checklist.

- **Student Authentication & Role Management:**
  - Secure student registration with Roll Number, Department, and Semester.
  - Passwords hashed using PBKDF2/SHA-256 via Werkzeug.
  - **1-Click Demo Profile Switcher** built directly into the UI for teacher evaluations and viva presentations.

- **Presentation & Viva Reference Hub:**
  - Dedicated `/about-project` page embedded in the application showcasing the project synopsis, architectural overview, database schema, and common teacher viva questions with answers.

---

## 3. Technology Stack

| Layer | Technologies Used |
|---|---|
| **Frontend** | HTML5, CSS3, JavaScript (ES6), Bootstrap 5.3, Bootstrap Icons |
| **Backend** | Python 3 with Flask Web Microframework |
| **Database** | SQLite3 (relational tables with foreign key constraints) |
| **Security** | Werkzeug Cryptographic Password Hashing (PBKDF2-SHA256), Session Cookies |
| **Architecture**| Model-View-Controller (MVC) Pattern |

---

## 4. Database Schema Overview

The SQLite database (`bookbridge.db`) consists of 4 relational tables:

1. **`users`**: Student profiles (ID, Enrollment Number, Full Name, Email, Password Hash, Department, Course/Year, Contact Phone).
2. **`meeting_points`**: Monitored university locations with descriptions, operating hours, and safety notes.
3. **`listings`**: Uploaded learning materials (Title, Author, Subject, Course, Semester, Listing Type, Condition, Availability Status, Foreign Keys to `users` and `meeting_points`).
4. **`exchange_requests`**: Student interest requests (Listing ID, Requester ID, Message, Offered Trade Item, Duration, Status: Pending/Accepted/Declined/Completed, Owner Handover Remarks).

---

## 5. How to Run the Project (Step-by-Step)

### Prerequisites:
- Python 3.8+ installed on your system.

### Steps:

1. Open PowerShell or Command Prompt and navigate to the project directory:
   ```powershell
   cd C:\Users\SANYA\.gemini\antigravity\scratch\bookbridge
   ```

2. (Optional) Install dependencies:
   ```powershell
   python -m pip install flask
   ```

3. Initialize the database and load realistic MCA sample listings:
   ```powershell
   python database.py
   ```

4. Start the Flask web application:
   ```powershell
   python app.py
   ```

5. Open your web browser and visit:
   ```
   http://127.0.0.1:5000
   ```

> **Convenience Launcher:** On Windows, you can simply double-click the included `run.bat` file to automatically launch the server and open the application in your default browser.

---

## 6. Pre-Configured Demo Accounts (For Viva / Evaluation)

All seeded demo accounts use the standard password: `student123`

| Student Name | Role / Class | Roll Number | Email |
|---|---|---|---|
| **Sanya** | Project Lead / MCA 1-B | `10517704426` | `sanya.mca@campus.edu` |
| **Rahul Sharma** | Student / MCA 1-A | `10517704412` | `rahul.sharma@campus.edu` |
| **Priya Nair** | Senior / MCA 2nd Year | `10517704435` | `priya.nair@campus.edu` |
| **Amit Verma** | Student / B.Tech CS 3rd Year | `10517704448` | `amit.verma@campus.edu` |

*(Tip: In the navigation bar, click the **Demo Switch** dropdown to instantly switch between these profiles without having to type passwords during your project demo).*

---

## 7. Project Structure

```
bookbridge/
│
├── app.py                           # Main Flask controller & route endpoints
├── database.py                      # SQLite database connector & seed dataset
├── schema.sql                       # Relational DDL table definitions
├── run.bat                          # 1-click Windows runner script
├── README.md                        # Project documentation & run guide
├── PROJECT_REPORT_AND_VIVA_GUIDE.md # Academic documentation & Viva questions
│
├── static/
│   ├── css/
│   │   └── custom.css               # College portal styles & responsive layout
│   └── js/
│       └── main.js                  # Dynamic alerts, interactions & form helpers
│
└── templates/
    ├── base.html                    # Master layout with navbar, alerts & footer
    ├── index.html                   # Catalogue, search bar, filters & stats
    ├── listing_detail.html          # Book view & express interest form
    ├── create_listing.html          # Post a new book/notes form
    ├── edit_listing.html            # Update existing book details
    ├── my_listings.html             # Student's uploaded books dashboard
    ├── my_requests.html             # Incoming & outgoing request coordination
    ├── login.html                   # Student sign in & demo switchers
    ├── register.html                # Student registration with roll number
    ├── handover_guidelines.html     # Approved campus meeting points & rules
    └── about_project.html           # Synopsis, architecture & viva guide
```
