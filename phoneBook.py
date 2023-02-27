import pickle
#---------------------------------------------------------------------

"""Verify you have entered a good phone number."""
def isnumber(number):
    if number.isdigit()==False or len(number)!=9:
        return False
    
    else:
        return True
#---------------------------------------------------------------------
class Person():

    def __init__(self,name,lastName,phoneNumber):
        self.name=name
        self.lastName=lastName
        self.phoneNumber=phoneNumber
    
    def __str__(self):
        return ("\n Name: {} {}\n Phone Number: {}\n".format(self.name,self.lastName,self.phoneNumber))



class Phonebook():

    people=[]
    
    def __init__(self):
        file= open("phoneBook_DB","ab+")
        file.seek(0)

        try:
            self.people= pickle.load(file)

        except:
            pass

        finally:
            file.close()
            del(file)

    """Save the file with all the contacts you have in"""
    def __save(self):
        file=open("phoneBook_DB","wb")
        pickle.dump(self.people,file)

        file.close()
        del(file)

    """Add contact to the 'people' list, then it save the file"""
    def add(self,p):
        self.people.append(p)

        self.__save()

    """search a coincidence in phone number(because its unique) to delete the contact. then it save the file"""
    def delete(self):
        control=1

        while control==1:
            delUser=input("- User number you want to delete ( or Press 0 to exit) : ")

            if delUser=="0":
                control=0
            
            elif delUser!="0":

                count=0
                for i in self.people:
                    x= i.phoneNumber

                    if x==delUser:
                        count+=1

                        yn=input("- you will delete {}'s number. Are you sure? Y/N: ".format(i.name)).upper()

                        if yn=="Y" or yn=="YES":
                            self.people.pop(self.people.index(i))
                            print("- {} has been delete from your Phone book.".format(i.name))

                            control=0
                        
                        elif yn=="N" or yn=="NO":
                            pass

                        else:
                            print("- you have not entered a valid character. Please try again")

                if count==0:
                    print("- Phone number is not in your phone book. Try again.")
                    print()
                
            self.__save()

    """Show the contact list"""
    def show(self):
        for i in self.people:
            print(i)
            print("---- ---- ---- ---- ----")
        print("---- End of list ----")
    
    """Search by contact name"""
    def search(self):
        count=0
        user= input("Name to search for: ").capitalize()

        for i in self.people:
            x=i.name

            if x==user:
                count+=1
                print(i)
            
        print("---- Search ended ----")
        print("- There are {} contact matching".format(count))
        print()

        if count==0:
            print("There's no contact name like {}.".format(user))
#---------------------------------------------------------------------
book=Phonebook()
#---------------------------------------------------------------------
control=0

while control==0:
    print("Welcome to your Phone Book!")
    print()
    print("--------------------")
    print("---- Phone Book ----")
    print("--------------------")
    print()

    print("1.- Contact list")
    print("2.- Add/Delete number")
    print("3.- Search")

    print("             4.- Exit")
    print()

    choice= input("- What you want to do?: ").upper()
    print("---------------------------------------")

    if choice=="1" or choice=="CONTACT LIST": 
        control=1

        while control==1:
            book.show()
            print()

            yn=input("- Type '0' when yo want to exit to main menu: ").upper()
            
            if yn=="0":
                print()

                control=0

            else:
                control=1

    elif choice=="2" or choice=="ADD NUMBER" or choice=="DELETE NUMBER" or choice=="ADD/DELETE NUMBER": #Add/DELETE number
        print("---------------------------")
        print("---- Add/DELETE number ----")
        print("---------------------------")
        print()

        print("1.- Add number")
        print("2.- DELETE number")

        print("         3.- Exit")
        print()

        choice= input("- What you want to do?: ").upper()
        print("---------------------------------------")
        print()

        if choice=="1" or choice=="ADD NUMBER": 
            control=1
            
            while control==1:
                print("- please fill in the following:")
                print()

                name=input("Name: ").capitalize()
                lastName= input("Last name: ")
                phoneNumber=input("Phone number: ")

                tf= isnumber(phoneNumber)

                if tf==False: #Not a phone number
                    print("- you have not entered a valid Phone number. Try again")
                    print()

                else: #good phone number
                    p=Person(name,lastName,phoneNumber)
                    book.add(p)

                    print("- {} {} has been successfully added".format(name,lastName))
                    print()

                    control=0

        elif choice=="2" or choice=="DELETE NUMBER":
            book.delete()
            print()
        
        elif choice=="3" or choice=="EXIT": 
            pass
            
        else:
            print("- you have not entered a valid value. Try again")
    
    elif choice=="3" or choice=="SEARCH":
        control=1

        while control==1:
            book.search()

            yn=input("- Type '0' when yo want to exit to main menu: ").upper()
                
            if yn=="0":
                control=0
            else:
                control=1

    elif choice=="4" or choice=="EXIT": #Exit
        control=1
    
    else:
        print("you have not entered a valid value. Try again")
    
print("----------------------------------------------------------")
print("---- Thanks for use Phone Book. Hope to see you soon! ----")
print("----------------------------------------------------------")
