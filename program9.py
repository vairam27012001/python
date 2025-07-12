class dad():
    def phone(self):
        print("phone")
class mom():
    def sweet(self):
        print ("sweet")
class son(dad,mom):
    def laptop(self):
        print("laptop")

ram=son()
ram.phone()
ram.sweet()
