import string
import random
from csv import writer

def createCSV (platform, password):
    head = [platform, password]
    with open('08-project/passGen.csv', 'a') as w:
        writedata = writer(w)
        writedata.writerow(head)


def genPass():
    string1 = string.ascii_lowercase
    #print(string1)
    string2 = string.ascii_uppercase
    #print(string2)
    string3 = string.digits
    #print(string3)
    string4 = string.punctuation
    #print(string4)
    userInputPlatForm = str(input("Enter the platForm name <> "))
    userInputPassword = int(input("Enter the character length for password <> "))
    AllcharacterList = []
    AllcharacterList.extend(list(string1))
    AllcharacterList.extend(list(string2))
    AllcharacterList.extend(list(string3))
    AllcharacterList.extend(list(string4))
    #print(AllcharacterList)
    random.shuffle(AllcharacterList)
    #print(AllcharacterList)
   
    passGen = ("".join(AllcharacterList[0:userInputPassword]))
    createCSV(userInputPlatForm, passGen)

    print("Password:", passGen)
    #return passGen


genPass()
