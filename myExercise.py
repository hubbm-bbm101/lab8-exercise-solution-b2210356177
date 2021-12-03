import sys

dictionary = {}

with open(sys.argv[1], "r") as f:
    for info in f:
        student_name, student_education = info.split(":")
        dictionary[student_name] = student_education[:]

        for student in sys.argv[2].split(","):
            try:
                print(f"Student name: {student}, University: {dictionary[student]}")

            except:
                print(f"No record of '{student}' was found!")