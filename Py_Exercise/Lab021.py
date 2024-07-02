# Single Inheritance

class super_class():
    def super_function(self):
        print("From super class")

class derived_class():
    def derived_class(self):
        print("From derived class")


derived_obj = derived_class()
derived_obj.derived_class()
