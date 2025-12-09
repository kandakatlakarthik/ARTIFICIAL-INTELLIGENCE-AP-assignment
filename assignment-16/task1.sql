-- =====================================================================
-- Task 1: Schema Generation for Library Management System
-- =====================================================================

-- Drop tables if they exist to ensure a clean slate for creation.
DROP TABLE IF EXISTS Loans;
DROP TABLE IF EXISTS Books;
DROP TABLE IF EXISTS Members;

-- Create the Books table
-- This table stores all the information about the books in the library.
CREATE TABLE Books (
    book_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    published_year YEAR,
    genre VARCHAR(100),
    is_available BOOLEAN DEFAULT TRUE
);

-- Create the Members table
-- This table holds information about the library members.
CREATE TABLE Members (
    member_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone_number VARCHAR(20),
    join_date DATE NOT NULL DEFAULT CURRENT_DATE
);

-- Create the Loans table
-- This table tracks which books are loaned to which members.
CREATE TABLE Loans (
    loan_id INT AUTO_INCREMENT PRIMARY KEY,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    loan_date DATE NOT NULL DEFAULT CURRENT_DATE,
    due_date DATE NOT NULL,
    return_date DATE,
    FOREIGN KEY (book_id) REFERENCES Books(book_id) ON DELETE RESTRICT,
    FOREIGN KEY (member_id) REFERENCES Members(member_id) ON DELETE RESTRICT
);
