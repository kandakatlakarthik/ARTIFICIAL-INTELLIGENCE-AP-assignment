-- =====================================================================
-- Task 4: Update and Delete Queries
-- =====================================================================

-- Part 1: Update a book's availability to FALSE when borrowed.
-- Let's say member 'Charlie Brown' (member_id = 3) borrows 'To Kill a Mockingbird' (book_id = 2).
-- This should be done in a transaction to ensure data integrity.
-- START TRANSACTION;
-- -- Add the new loan record
-- INSERT INTO Loans (book_id, member_id, due_date) VALUES (2, 3, '2024-07-15');
-- -- Update the book's availability status
-- UPDATE Books SET is_available = FALSE WHERE book_id = 2;
-- COMMIT;

-- For demonstration, here is the standalone UPDATE query.
-- This would be run after a new loan is created.
UPDATE Books SET is_available = FALSE WHERE book_id IN (SELECT book_id FROM Loans WHERE return_date IS NULL);


-- Part 2: Delete a member record safely.
-- To safely delete a member, we must first ensure they have no outstanding loans.
-- The FOREIGN KEY constraint with ON DELETE RESTRICT will prevent deletion if active loans exist.
-- The following DELETE will fail for member_id = 1 (Alice) because she has active loans.
-- DELETE FROM Members WHERE member_id = 1;

-- To successfully delete a member, they must have returned all books.
-- Let's assume member_id = 3 (Charlie Brown) has no loans. This will succeed.
DELETE FROM Members WHERE member_id = 3;