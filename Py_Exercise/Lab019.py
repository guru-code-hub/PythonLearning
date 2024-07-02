# Class demo

class man:
    name = None
    age = None

    def __init__(self, name, age):
        print("Man is initialization")
        self.name = name
        self.age = age

    def walk(self):
        print("Man is walking", self.name, self.age)

    def talk(self):
        print("Man is talking", self.name, self.age)

    def sleep(self):
        print("Man is sleeping", self.name, self.age)


obj_man = man("Guru", 42)
obj_man.walk()
obj_man.talk()
obj_man.sleep()
