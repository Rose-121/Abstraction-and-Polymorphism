class India():
    def capital(self):
        print("New Dilhi is the Capital of India.")
        
    def language(self):
        print("Hindi is the most widely spoken of India")
        
    def type(self):
        print("India is a developing country")
        
        
class Bangladesh():
    def capital(self):
        print("Dhaka is the Capital of Bangladesh.")
        
    def language(self):
        print("Bangla is the mother language of Bangladesh")
        
    def type(self):
        print("Bangladesh is a developing country")
        
        
objInd = India()
objBD = Bangladesh()

for country in (objInd, objBD):
    country.capital()
    country.language()
    country.type()
    print()
        