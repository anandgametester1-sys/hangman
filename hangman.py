print("""..... HELLO......."
          WELCOME TO NEW GAME...""")

count=1
score = 0
import random
while count<=5:
    PLAYER= int (input("Hey... User Inter Your number.: "))
    num = random.randint(1,10)
    a= "PLAYER  apko ek point milli.."  
    print(num)
    if num == PLAYER:
       print(a)
       score= score+1
    else:
         print("aap dono ko point nahi mila ")
         
    count= count+1
print(score)


