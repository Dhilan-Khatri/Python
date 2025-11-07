#make 2 classes of countries that have 3 methods to display (capital, language, type)
#use polymorhism to mkae a common interface for all.

class USA():
    def capital(self):
        print("Washington D.C.")
    def language(self):
        print("English")
    def type(self):
        print("Developed Country")
        
class Russia():
    def capital(self):
        print("Moscow")
    def language(self):
        print("Russia")
    def type(self):
        print("Developed Country")

obj1=USA()
obj2=Russia()

for item in (obj1, obj2):
    item.capital()
    item.language()
    item.type()