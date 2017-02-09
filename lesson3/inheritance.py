class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor called")
        self.last_name = last_name
        self.eye_color = eye_color
    def show_info(self):
        print("Last Name - " + self.last_name)

class Child(Parent):
    def __init__ (self, last_name, eye_color, number_of_toys):
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        # Use super method in Python
        Parent.show_info(self)
        print("Last Name2 - " + self.last_name)

parent = Child("Name", "blue", 5)
print(parent.last_name)
print(parent.number_of_toys)
parent.show_info()
