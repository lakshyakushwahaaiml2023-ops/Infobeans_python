'''13. Exam Portal
Problem

Create exam management system.

Requirements

Each exam object:

exam name
total marks
passing marks
Functionalities
Check pass/fail
Calculate grade
Maintain total exams conducted'''

class Exam:
  
  def __init__(self, name, tm, pm):
    self.__total_marks = tm
    self.__name = name
    self.__passing_marks = pm

  def get_total(self):
    return self.__total_marks

  def get_passing(self):
    return self.__passing_marks

class EMS:
  __exams = {}
  def add_exam(self, name, tm, pm):
    EMS.__exams[name] = Exam(name, tm, pm)

  def pass_fail(self, name, marks):
    if name not in EMS.__exams:
      print("Exam not found!")
    else:
      pm = EMS.__exams[name].get_passing()
      if marks >= pm:
        print("Pass!!!")
      else:
        print("Fail!!!")

  @classmethod
  def get_total_exams(cls):
    return len(cls.__exams)
        
  def grade(self, name, marks):
    if name not in EMS.__exams:
      print("Exam not found!")
    else:
      total = EMS.__exams[name].get_total()
      perc = (marks/total) * 100
      match perc:
        case p if p > 85:
          print("A Grade!!!")
        case p if p > 60:
          print("B Grade!!!")
        case p if p > 50:
          print("C Grade!!!")
        case p if p > 30:
          print("D Grade!!!")
        case _:
          print("Fail!!!")
    
e1 = EMS()
e1.add_exam("JEE-MAINS", 100, 33)
e1.add_exam("JEE-ADVANCED", 450, 150)
e1.add_exam("NEET-UG", 720, 330)
e1.add_exam("CUET-UG", 100, 33)
e1.pass_fail("JEE-ADVANCED", 420)
e1.grade("JEE-MAINS", 78)
print(EMS.get_total_exams())
