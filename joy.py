class student:
    def __init__(self,name,marks):
        self.marks=marks
        self.name=name
    def welcome(self):
        print("Welcome student")
    def get_marks(self):
        return marks
s1=student("karan",28)
     
s1.welcome()
print(s1.get_marks())

