-- BookBridge Database Schema
-- Developed for MCA Mini-Project
-- Student: Sanya (Enrollment: 10517704426, MCA 1-B)
-- Mentor: Dr. Cosmena

DROP TABLE IF EXISTS exchange_requests;
DROP TABLE IF EXISTS listings;
DROP TABLE IF EXISTS meeting_points;
DROP TABLE IF EXISTS users;

-- 1. Users Table (Campus Students & Faculty)
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    enrollment_no TEXT UNIQUE NOT NULL,
    full_name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    department TEXT NOT NULL DEFAULT 'Computer Applications',
    course_year TEXT NOT NULL DEFAULT 'MCA 1st Year',
    contact_phone TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Approved Safe Campus Meeting Points
CREATE TABLE meeting_points (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    location_desc TEXT NOT NULL,
    operating_hours TEXT NOT NULL,
    safety_notes TEXT
);

-- 3. Book and Learning-Material Listings
CREATE TABLE listings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    subject TEXT NOT NULL,
    course TEXT NOT NULL,               -- e.g., MCA, B.Tech CS, BCA
    semester TEXT NOT NULL,             -- e.g., Semester 1, Semester 2
    listing_type TEXT NOT NULL,         -- 'Lend', 'Exchange', 'Donate'
    condition TEXT NOT NULL,            -- 'Like New', 'Good', 'Fair / Marked', 'Annotated / Notes'
    availability_status TEXT NOT NULL DEFAULT 'Available', -- 'Available', 'Pending Handover', 'Completed'
    description TEXT,
    preferred_meeting_point_id INTEGER,
    cover_image TEXT,                   -- image placeholder or category icon
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (preferred_meeting_point_id) REFERENCES meeting_points(id)
);

-- 4. Exchange & Request-Interest Table
CREATE TABLE exchange_requests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    listing_id INTEGER NOT NULL,
    requester_id INTEGER NOT NULL,
    meeting_point_id INTEGER,
    message TEXT NOT NULL,
    offered_exchange_item TEXT,         -- For 'Exchange' listings: what book the requester is offering
    proposed_duration TEXT,             -- For 'Lend' listings: e.g. "3 Weeks", "Until End-Sem Exams"
    status TEXT NOT NULL DEFAULT 'Pending', -- 'Pending', 'Accepted', 'Declined', 'Completed'
    owner_remarks TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (listing_id) REFERENCES listings(id) ON DELETE CASCADE,
    FOREIGN KEY (requester_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (meeting_point_id) REFERENCES meeting_points(id)
);
