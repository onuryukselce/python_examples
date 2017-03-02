from secrets import randbelow
import random

#-------------------------
# Random password generator 
#-------------------------


    

CHARS = ["A", "B", "C", "Ç" ,"D", "E", "F", "G", "Ğ", "H", "I", "İ", "J", "K", "L",
                   "M", "N", "O", "Ö", "P", "R", "S", "Ş", "T", "U", "Ü", "V", "Y", "Z",
         "1","2","3","4","5","6","7","8","9","0","!","-","£","#",
         "a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i" ,"j", "k", "l",
         "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]


#---function is here----
def generateLetter(x,y):
    i=0
    while i < y:
            randomChar = random.choice(CHARS)
            x=x+randomChar
            i=i+1
    print(str(x))
    
    
#--- declaration ----
passw=""
r=0

#--Main Program--

passCount = int(input("How many passwords will be generated: "))    
passSize = int(input("How many characters: "))


while r < passCount:
    generateLetter(passw,passSize)
    r=r+1
