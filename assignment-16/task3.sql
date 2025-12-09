-- =====================================================================
-- Task 3: Basic Query - List all books borrowed by a specific member
-- =====================================================================

-- This query finds all books borrowed by the member with member_id = 1 (Alice Johnson).
-- It joins the Loans and Books tables to get the book titles.
SELECT
    b.title,
    b.author,
    l.loan_date,
    l.due_date
FROM
    Loans l
JOIN
    Books b ON l.book_id = b.book_id
WHERE
    l.member_id = 1; -- Example: for member Alice Johnson