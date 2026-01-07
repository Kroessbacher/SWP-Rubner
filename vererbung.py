
class Grandparent:
    def __init__(self):
        self.eye_color = "blau"

    def eye_surgery(self):
        self.eye_color = "grün"


class Parent(Grandparent):
    def __init__(self):
        super().__init__()
        self.head_shape = "rund"


class Child(Parent):
    def __init__(self, name, age):
        super().__init__()
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1


def main():
    child1 = Child("Enes", 1)

    print(child1.name)
    print(child1.age)
    print(child1.eye_color)
    print(child1.head_shape)

    child1.eye_surgery()
    child1.birthday()

    print(child1.age)
    print(child1.eye_color)

if __name__ == '__main__':
    try:
        main()
    except:
        print("Error")

