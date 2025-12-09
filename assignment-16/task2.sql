-- =====================================================================
-- Task 2: Insert Sample Data (3 records per table)
-- =====================================================================

-- Insert sample data into Books
INSERT INTO Books (title, author, isbn, published_year, genre) VALUES
('The Great Gatsby', 'F. Scott Fitzgerald', '978-0743273565', 1925, 'Fiction'),
('To Kill a Mockingbird', 'Harper Lee', '978-0061120084', 1960, 'Fiction'),
('1984', 'George Orwell', '978-0451524935', 1949, 'Dystopian');

-- Insert sample data into Members
INSERT INTO Members (first_name, last_name, email, phone_number) VALUES
('Alice', 'Johnson', 'alice.j@example.com', '123-456-7890'),
('Bob', 'Smith', 'bob.s@example.com', '234-567-8901'),
('Charlie', 'Brown', 'charlie.b@example.com', '345-678-9012');

-- Insert sample data into Loans
-- Let's assume Alice borrowed 'The Great Gatsby' and Bob borrowed '1984'
INSERT INTO Loans (book_id, member_id, due_date) VALUES
(1, 1, '2024-06-30'), -- Alice borrows The Great Gatsby
(3, 2, '2024-07-05'), -- Bob borrows 1984
(2, 1, '2024-07-10'); -- Alice also borrows To Kill a Mockingbird
