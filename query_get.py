


# Consider a database schema with two tables: students and courses.

# The students table has the following columns:

# student_id (Primary Key)
# student_name
# age
# gender
# course_id (Foreign Key referencing courses table)
# The courses table has the following columns:

# course_id (Primary Key)
# course_name
# instructor
# credits
# Write an SQL query to find the names of all students enrolled in the course named 'Mathematics'.

query="""SELECT students.student_name
FROM students
INNER JOIN courses ON students.course_id = courses.course_id
WHERE courses.course_name = 'Mathematics'"""