#= float(input("marks_number: "))

def grade(marks):

    if marks < 50:
       return "fail"
    elif marks >= 60 and marks <= 70:
        return "pass"
    elif marks >= 61 and marks <= 80:
        return "fair"
    elif marks >= 81 and marks <= 90:
        return "excellent"
    else :
        return ("distinction")

score= float(input("marks_number: "))

print(grade(score))