class Person:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def introduce(self):
        print(f'Hello! My name is {self.name} and {self.age} years old and am a {self.gender}' )

Person1 = Person("Giddy", 21, "male")
Person1.introduce()