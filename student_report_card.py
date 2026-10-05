name = input("Enter student name: ")
admisssion_number = input(" Enter admission number: ")
institution = input("Enter institution name: ")
course = input("Enter course name: ")
required_courses = {"mathemaatics", "communication skills", "data tools"}
enrolled_courses = {"mathematics", "data tools"}
core_met = enrolled_courses. intersection(required_courses)
missing_courses = required_courses. difference(enrolled_courses)
total_marks = float(input("Enter total marks: "))
total_marks_obtained = float(60)
status = "pass" if total_marks >= 40 else "fail"
status = "fail" if total_marks < 40 else "pass"
print("student name:", name)
print("admisssion number:", admisssion_number)
print("instituion:", institution)
print("course:", course)
print("required course:", required_courses)
print("enrolled course:",enrolled_courses )
print("core met:", core_met)
print("missing_course:", missing_courses)
print("total_marks:", total_marks)
print("total_marks_obtained:", total_marks_obtained)
print("status:", status)



                                   


        



 

