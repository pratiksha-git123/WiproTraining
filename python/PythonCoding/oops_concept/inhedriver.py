
from oops_concept.college import College
from oops_concept.student import Student
from oops_concept.teacher import Teacher
from studentgrade import StudentGrade
cc = int(input("C code: "))
cn = input("C name: ")
ci = input("City: ")
rno = int(input("Roll no: "))
sn = input("Student name: ")
m1 = int(input("M1: "))
m2 = int(input("M2: "))
m3 = int(input("M3: "))
eid = int(input("Eid: "))
tn = input("Teacher name: ")
de = input("Department: " )
bp = float(input("Basicpay: "))

# project = College (ccode = cc, cname = cn, ccity = ci)
#
# project.welcome_message()
# project.display_college_details()

# project = Student(ccode = cc, cname = cn, ccity = ci, rno = rno, sname = sn,
#                    m1 = m1, m2 = m2, m3 = m3)
project = StudentGrade(ccode = cc, cname = cn, ccity = ci, rno = rno, sname = sn,
                       m1 = m1, m2 = m2, m3 = m3)
project.welcome_message()
project.display_college_details()
print(f'Roll NO: {project.rollno} \t Name: {project.stuname} \t Total: {project.calculate_total()} \nAverage: {project.calculate_average()}')
project.calculate_grade()
print(f'Result: {project.result} \t Grade: {project.grade}')
teach = Teacher(ccode = cc, cname = cn, ccity = ci,eid = eid, tn = tn, de = de, bp = bp )
print(f'Eid: {teach.empid} \t Name: {teach.tname} \t Dept: {teach.dept}')
print(f'Salary: {teach.calculate_salary()}')