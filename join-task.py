# onsider two tables: students and courses.

# students table has columns: student_id, name, and age.

# courses table has columns: course_id, course_name, and student_id (which represents the student enrolled in that course).

# Write an SQL query to find the names of all students who are enrolled in more than one course.





query="""SELECT s.name
FROM students s
JOIN courses c ON s.student_id = c.student_id
GROUP BY s.student_id, s.name
HAVING COUNT(c.course_id) > 1;
"""