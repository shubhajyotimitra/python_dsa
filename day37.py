#day-25 solving

questions = [
            ["which language was used to create web pages?","python","javascript","php","none",4],
            
            ["which language was used to create web pages?","python","javascript","php","none",4],

            ["which language was used to create web pages?","python","javascript","php","none",4],

            ["which language was used to create web pages?","python","javascript","php","none",4],

]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money = 0
i = 0 
for i in range(0,len(questions)):
    question = questions[i]
    print(f"question for rs. {levels[i]}")
    print(f"a.  {question[1]}            b.  {question[2]} ")
    print(f"c.  {question[3]}            d.  {question[4]} ")
    reply = int(input("enter your answer :"))
    if(reply == question[-1]):
        print(f"congratulations! you have won rs. {levels[i]}")
        if(i==4):
            money = 4000
        elif(i==9):
            money = 320000
        elif(i==14):
            money = 1320000
    else:
        print("wrong answer! you are leaving with rs. 0")
        break