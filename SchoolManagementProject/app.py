import json
from abc import ABC,abstractmethod
from pathlib import Path



databse = "school_data.json"

data = {
    "students" : [],
    "teachers" : []
}

if Path(databse).exists():
    with open(databse,"r") as f:
        content = f.read()
        if content:
            data = json.loads(content)


def save():
    with open(databse,"w") as f:
        json.dump(data,f,indent=4)


class Person(ABC):

    @abstractmethod
    def get_roles(self):
        pass

    @abstractmethod
    def register(self):
        pass

    @abstractmethod
    def show_Detials(self):
       pass

    @staticmethod
    def validate_email(email):
        return "@" in email and "." in email
    
 

class Student(Person):
    def __init__(self):
        super().__init__()
    def get_roles(self):
        return "student"

    def register(self):
        name = input("tell your name:- ")
        age = int(input("enter your age:-"))
        email = input("tell you email")
        roll_no = input("tell you roll number")


        if not Person.validate_email(email):
            print("Invalid Email!!...")
            return

        for i in data["students"]:
            if i["roll_no"] == roll_no:
                print("Student with RN exists!..")
                return


        data["students"].append({
            "name" : name,
            "age" : age, 
            "roll_no" : roll_no,
            "email" : email,
            "grades" : {}
        })
        save() # saving data to DB
        print(f"{name} with {roll_no} is registered successfully")

    def show_Detials(self):
           roll_no = input("tell Your roll Not:-")
           for s in data["students"]:
                if s["roll_no"] == roll_no:
                     grades = s["grades"]
                     avg = sum(grades.values()) / len(grades) if grades else 0
                     print(f"Name : {s["name"]}")
                     print(f"Roll No : {s["roll_no"]}")
                     print(f"Grades : {grades}")
                     print(f"Avg. : {avg:.1f}")


    def add_grades(self):
         roll_no = input("tell the roll number:-")
         subject = input("Subjects:-")
         marks = int(input("Marks :-"))

         for i in data["students"]:
              if i["roll_no"] == roll_no:
                    i["grades"][subject] = marks
                    save()
                    print("Grade added sucesfully!")
              else :
                  continue
    
class Teacher(Person):

    def __init__(self):
           super().__init__()
    def get_roles(self):
           return "teacher"
   
    def register(self):
           name = input("tell your name:- ")
           age = int(input("enter your age:-"))
           email = input("tell your email")
           emp_id = input("tell your emp_id number")
           subject = input("tell your subject")
   
   
           if not Person.validate_email(email):
               print("Invalid Email!!...")
               return
   
           for i in data["teachers"]:
               if i["emp_id"] == emp_id:
                   print("Student with RN exists!..")
                   return
   
   
           data["teachers"].append({
               "name" : name,
               "age" : age, 
               "emp_id" : emp_id,
               "email" : email,
               "subject" : subject
           })
           save() # saving data to DB
           print(f"Teacher with {name} and {emp_id} is registered successfully")
   
    def show_Detials(self):
               emp_id = input("tell Your Teacher emp_id:-")
               for t in data["teachers"]:
                    if t["emp_id"] == emp_id:
                         print(f"Name : {t["name"]}")
                         print(f"Empp No : {t["emp_id"]}")
                         print(f"suject is {t["subject"]}")

    
   

print("Press 1 to register a student")
print("press 2 to resiter teh teacher")
print("press 3 to add grades")
print("press 4 to show students detials")
print("press 5 to show teacher details")

choise = int(input("Please Enter Your Choise 1-5:- "))

stud = Student()
tech = Teacher()
if choise == 1:
    stud.register()
elif choise == 2:
    tech.register()
elif choise == 3:
    stud.add_grades()
elif choise == 4:
    stud.show_Detials()
elif choise == 5:
    tech.show_Detials()
else:
    print("Invalide choise.!!!")