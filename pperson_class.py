class Person:
    def __init__(self,initialAge):
        if initalAge > 0:
            self.age = initialAge
        else:
            self.age = 0
            print "Age is not valid, setting age to 0."

    def yearPasses(self):
        self.age += 1

    def amIOld(self):
        if self.age < 13:
            print "You are young."
        elif: 13 <= self.age <18:
            print "You are a teenager."
        else:
            print "You are old."

T=int(raw_input())
for i in range(0,T):
    age=int(raw_input())         
    p=Person(age)  
    p.amIOld()
    for j in range(0,3):
        p.yearPasses();        
    p.amIOld();
    print ""