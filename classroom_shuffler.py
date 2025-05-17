import random

class ExamClassroom:
    def __init__(self, subject_counts):
        self.subjects = []
        for subject, count in subject_counts.items():
            self.subjects.extend([subject] * count)
        self.layout = [['' for _ in range(7)] for _ in range(5)]  

    def is_valid_row(self, row):
        for i in range(6):  
            if row[i] != '' and row[i] == row[i + 1]:
                return False
        return True

    def arrange_students(self):
        students = self.subjects + [''] * (35 - len(self.subjects))  
        attempts = 0
        while attempts < 10000:
            attempts += 1
            random.shuffle(students)
            temp_layout = [students[i*7:(i+1)*7] for i in range(5)]
            if all(self.is_valid_row(row) for row in temp_layout):
                self.layout = temp_layout
                return True
        return False

    def display(self):
        for i, row in enumerate(self.layout):
            print(f"Row {i+1}: L:{row[0]} {row[1]}  C:{row[2]} {row[3]} {row[4]}  R:{row[5]} {row[6]}")


subject_counts = {'A': 20, 'B': 0, 'C': 15}


exam = ExamClassroom(subject_counts)
if exam.arrange_students():
    exam.display()
else:
    print("Couldn't find a valid arrangement")