math_expressions=["2+2","4-2","5*2","6**2"]
math_answers=["4","2","10","36"]
count=0
for i in math_expressions:
    answer=str(input(f"{i}=..."))
    if answer==math_answers[count]:
        print("You are right!")     
    else:
        print("You are wrong!!!")
    count+=1

            
    