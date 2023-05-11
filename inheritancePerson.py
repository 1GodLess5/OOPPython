class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printName(self):
        print(self.firstName + self.lastName)


class Student(Person):
    def __init__(self, firstName, lastName, age):
        super().__init__(firstName, lastName)

        self.age = age

    def isAdult(self):
        if self.age >= 18:
            print(self.firstName + " " + self.lastName + " is adult.")
        else:
            print(self.firstName + " " + self.lastName + "is not adult.")


class Worker(Person):
    def __init__(self, firstName, lastName, age, workingExperince, field):
        super().__init__(firstName, lastName)

        self.age = age
        self.workingExperience = workingExperince
        self.field = field

    def yearsExperience(self):
        print(self.firstName + " " + self.lastName + " is " + str(self.age) + " years old, and works for " + str(self.workingExperience)
              + " years in " + self.field + " field")


studentAlbert = Student("Albert", "Gacek", 20)
studentAlbert.isAdult()

workerAlbert = Worker("Albert", "Gacek", 20, 2, "programming")
workerAlbert.yearsExperience()

