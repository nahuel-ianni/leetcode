-- Solution to the 'Students and Examinations' problem.
-- Write your PostgreSQL query statement below.

SELECT S.student_id, S.student_name, T.subject_name, COUNT(E.student_id) AS attended_exams
FROM Students S
CROSS JOIN Subjects T
LEFT JOIN Examinations E 
    ON S.student_id = E.student_id 
    AND T.subject_name = E.subject_name
GROUP BY S.student_id, S.student_name, T.subject_name
ORDER BY S.student_id, T.subject_name;