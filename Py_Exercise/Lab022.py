# Multiple Inheritance

class Mother:
    mother_name = ""

    def mother(self):
        mother_nme = self.mother
        print(mother_nme)


class Father:
    father_name = ""

    def father(self):
        father_nme = self.father_name
        print(father_nme)


class Child(Mother, Father):
    def parents(self):
        print(self.father_name)
        print(self.mother_name)


childObj = Child()
childObj.father_name = "Sita"
childObj.mother_name = "Ram"
childObj.parents()
