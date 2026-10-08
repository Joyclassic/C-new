class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def avg_marks(self):
       
        for avg in self.marks:
            sum=0
            sum+=avg
        print("Hi", self.name,"your avg marks in",sum/3)
s1=student("karan",[35,40,50])
s1.avg_marks()