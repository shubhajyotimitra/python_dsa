#day-25 solving

questions = [
            ["which language was used to create web pages?","python","javascript","php","none",3],
            ["In Python, which of the following is used to take input from the user?","cin","scanf","input","get",3],
            ["Which of the following is not a programming language?","HTML","Python","Java","C++",1],
            ["Which of the following is a Python web framework?","Django","Laravel","Spring","Rails",1],
            ["What does 'CPU' stand for?","Central Processing Unit","Computer Personal Unit","Central Performance Unit","Control Processing Unit",1],
            ["Which of the following is used to style web pages?","HTML","CSS","JavaScript","Python",2],
            ["What is the output of 3 + 2 * 2 in Python?","10","7","8","9",2],
            ["Which of the following is a Python data type?","String","Integer","List","All of the above",4],
            ["What does 'HTTP' stand for?","HyperText Transfer Protocol","HighText Transfer Protocol","HyperText Transmission Protocol","None of the above",1],
            ["Which of the following is used for version control?","Git","Docker","Kubernetes","Jenkins",1]
            ]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]
money = 0
i = 0 
for i in range(0,len(questions)):
    question = questions[i]
    print(f"question for rs. {levels[i]}")
    print(f"a. {question[1]:<20} b. {question[2]:<20}")
    print(f"c. {question[3]:<20} d. {question[4]:<20}")

    reply = int(input("enter your answer :"))
    if(reply == question[-1]):
        print(f"congratulations! you have won rs. {levels[i]}")
        if(i==4):
            money = 5000
        elif(i==9):
            money = 800000
        elif(i==14):
            money = 3200000
    else:
        print("wrong answer! you are leaving with rs. 0")
        break
print(f"you are leaving with rs. {money}")