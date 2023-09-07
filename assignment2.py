import math
from socket import *


class Assignment2:

    def __init__(self, year=0):
        self.year = year

    def tellAge(self, currentYear):
        global age
        age = currentYear-self.year
        print("Your age is", age)

    def listAnniversaries(self):
        currentYear = 2022
        age = currentYear-self.year
        y = math.floor(age/10)
        anniversaries=[]
        count = 1
        for x in range(y):
            annis=count*10
            anniversaries.append(annis)
            count+=1
        return anniversaries

    def modifyYear(self, n):
        result = ""
        yearstr = str(self.year)
        for x in range(n):
            result += yearstr[0]
            result += yearstr[1]
        conv = str(self.year*n)
        count=1
        for x in range(len(conv)):
            if(count%2>0):
                result+=conv[count-1]
            count+=1
        return result


    @staticmethod
    def checkGoodString(string):
       count = 0
       amt = 0
       for x in range(len(string)):
           if (string[count].isnumeric()):
               amt += 1
               if(amt>1):
                   return False
           count += 1


       if ((len(string) >= 9) and (string[0].islower())  and (amt<=1)):
           return True
       else:
           return False

    @staticmethod
    def connectTcp(host, port):
        try:
            x = socket(AF_INET, SOCK_STREAM)
            address = gethostbyname(host)
            x.connect((address, port))
            x.close()
            return True
        except:
            return False
