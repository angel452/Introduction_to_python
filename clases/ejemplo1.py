class Person():
    #atributos
    name = ""
    school = ""
    #metodos
    def print_name(self):
        print (self.name)
    def print_school(self):
        print (self.school)

jorgue = Person()
jorgue.name = "jorgue"
jorgue.school = "Universidad de la vida"
jorgue.print_name()
jorgue.print_school()
