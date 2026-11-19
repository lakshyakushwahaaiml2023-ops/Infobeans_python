'''14. Multiple Inheritance Example

Classes:

Father
Mother
Child(Father, Mother)

Access methods from both.'''

class Father:
    def __init__(self, name):
        self.__name = name

    def set_mother(self, name):
        self.__name = name

    def get_father(self):
        return self.__name

        

class Mother:
    def __init__(self, name):
        self.__name = name

    def get_mother(self):
        return self.__name
    

class Child(Father, Mother):
    def __init__(self, name, f_name, m_name):
        Father.__init__(self, f_name)
        Mother.__init__(self, m_name)
        self.__name = name

    def __str__(self):
        return f"Father: {self.get_father()} | Mother: {self.get_mother()} | Child: {self.__name}"

c =Child("Lakshya", "Ashok", "Kusum")
print(c)
