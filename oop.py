class vehicle:
  def __init__(self, color, speed, name, model, price):
   self.color = color
   self.speed = speed
   self.name = name
   self.model = model
   self.price = price

honda = vehicle("BURGUNDY♥", 450,"HONDA", "DAIHATSU MIRA","5200K")
print(f"""The name of thIS car is {honda.name} {honda.model} model
with {honda.color} color {honda.speed}km/hr speed and the price
is {honda.price}""")
print()


BMW = vehicle("black", 600, "BMW","M6-27","2B"  )
print(f"""The name of this car is {BMW.name} {BMW.model} model
with {BMW.color} color {BMW.speed}km/hr speed and the price
is {BMW.price}""")




# book sec
class Book:
  def __init__(self, name, price, category):

    self.name= name
    self.price = price
    self.category = category

  def introduce(self):
    print(f"{self.name} is a {self.category} book available at {self.price} rupees")
    print()

book1 = Book("section e", 9000, "drama")
book2 = Book("Atomic Habit", 1200, "self help and personal development")

book1.introduce()
book2.introduce()


# student sec
class Student:
  def __init__(self, stu_name, marks):
    self.stu_name = stu_name
    self.marks = marks

  def student_info(self):
    print(f"Student: {self.stu_name}")
    print(f"marks: {self.marks}")

  def result_check(self):
    if self.marks >= 50:
      print("Result : pass")
      print()
    else:
      print("Result: fail")
      print()

s1 = Student("Aziz", 60)
s2  = Student("Sana", 30)
s3 =  Student("Julie",40)
s4 = Student("Tabitha", 80)

s1.student_info()
s1.result_check()
s2.student_info()
s2.result_check()
s3.student_info()
s3.result_check()
s4.student_info()
s4.result_check()

