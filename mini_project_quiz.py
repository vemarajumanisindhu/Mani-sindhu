text = '''welcome to the computer quiz! 
now you are going to have 5 questions and you will be awarded 1 mark for the correct answer  '''
print(text)
answer = input("Shall we start? ")
if answer.lower() != "yes":
    quit()
print("okay! let's get started\nHere you go")
score = 0

answer = input("what does CPU stand for?\n")
ans = "central processing unit"
if answer.lower() == "central processing unit":
    print("CORRECT")
    score+= 1
else:
    
    print("INCORRECT")
answer = input("what does ROM stand for?\n")
if answer.lower() == "read only memory":
    print("CORRECT")
    score+= 1
else:
    print("INCORRECT")
answer = input("what does RAM stand for?\n")
if answer.lower() == "random access memory":
    print("CORRECT")
    score+= 1
else:
    print("INCORRECT")
answer = input("what does PSU stand for?\n")
if answer.lower() == "power supply unit":
    print("CORRECT")
    score+= 1
else:
    print("INCORRECT")
answer = input("what does GPU stand for?\n")
if answer.lower() == "graphic processing unit":
    print("CORRECT")
    score+= 1
else:
    print("INCORRECT")
if score <= 2:
    print("need to improve,you score is ",score)

elif score == 5:
    print("Congrats you score is 5 out of 5 ")
else:
    print("you are almost there,your score is ",score)








