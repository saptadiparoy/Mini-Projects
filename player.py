class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Player(Person):
    def __init__(self, num, name, age, team):
        super().__init__(name, age)
        self.team = team
        self.num = num


    def to_dict(self):
        return {"Number":self.num, "Name":self.name, "Age":self.age, "Team":self.team}
    
    def display(self):
        return f"Number: {self.num} | Name: {self.name} | Age: {self.age} | Team: {self.team}"
    
    