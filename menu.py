def main():
    startMenu

def init():

def startMenu():
    print "MainMenu: "
    print "     [1] Show All"
    print "     [2] New Person"
    print "     [3] Edit A Person"
    print "     [4] Delete A Person"

# read Funktion zum einlesen der Tasten eingabe
# es kann direkt die Funktion der Person aufgerufen werden.





class Person:
    angelegtePerson=0

    def __init__(self, name, address, email):
        self.__name = name
        self.__address = address
        self.__email = email
        Person.angelegtePerson += 1

    def __del__(self):
        Person.angelegtePerson -= 1

    def changeName(name):
        self.__name = name

    def changeAddress(address):
        self.__address = address

    def changeEmail(email):
        self.__email = email

    def showPerson(person):
        print "Name:   %s" % (person.name)
        print "Address %s" % (person.address)
        print "Email   %s" % (person.email)
