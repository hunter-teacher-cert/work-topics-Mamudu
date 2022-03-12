* Last Name: Wally
* First Name: Mamudu

## Collaborated with team: Eduardo, Michele and Mamudu

https://colab.research.google.com/drive/1-pivEpm8NUUIQAIP5_qKwfzf17TWzXVR#scrollTo=HDjKgjju3lNK

# Mamudu Homework Assignment query here.
# Please save it to your repository.

~/
sql_query_string = """

---Type your homework query below
SELECT First, Last, studentID, Grade, Scantime, (Period=1) AS pd1, Date, CourseSection
FROM
(
SELECT s.First, s.Last, s.studentID, s.Grade, s.ScanTime, s.Status, Date, CourseSection, Attendance, Teacher, Period 
FROM scan AS s
INNER JOIN periodAtt AS p
ON s.studentID=p.studentID AND SUBSTR(s.scanTime, 1, 9)=p.date
WHERE Attendance="A"
ORDER BY s.Last ASC) 
AS allCuts

"""
 
#Exectue the SQL query
result_df = sql_query_to_pd(sql_query_string, db_name='default.db')
result_df
~/
## Asyn Assignment
~/
# Mamudu Asynchronous Homework queries here.
#Note that you will need to complete the homework assignment first.
#Please post asynch. queries on the Slack when you are done.

sql_query_string = """

SELECT Teacher, COUNT(Attendance) AS TotalCuts
FROM (SELECT s.First AS First, s.Last AS Last, s.StudentID AS StudentID, s.ScanTime AS ScanTime, s.Status AS Status, 
p.Date AS Date, p.CourseSection AS CourseSection, p.Attendance AS Attendance, p.Teacher AS Teacher, p.Period AS Period
FROM scan AS s
INNER JOIN periodAtt AS p
ON s.studentID = p.studentID
AND substr(ScanTime,1,instr(s.scanTime, ' ')-1) = p.Date
WHERE p.Attendance = 'A'
ORDER BY s.Last, s.First ASC) AS allCuts
GROUP BY Teacher
ORDER BY TotalCuts DESC
"""
# Exectue the SQL query
result_df = sql_query_to_pd(sql_query_string, db_name='default.db')
result_df
~/
