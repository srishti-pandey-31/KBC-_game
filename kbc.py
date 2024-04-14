a= (str(input("enter your name\n")))
print("hello",a,"we are going to play KBC\n")
print("Guidelines for the game are: \n"
"1.There will be 4 basic questions, each of Rupees 1000\n"
"2. There won't be any lifelines,as the questions are very basic\n"
"3. The last,Winner will get an amount of 4000 rupees!\n")

print("So, ",a," are you ready for the game?")
print("please reply in Yes/No\n")
n= str(input("your reply\n"))
if n.lower() == "No".lower():
    print("No worries! Take your time. Have a great day\n")
else:
    print("Here you go",a)

    questions =["Question1\n" "what is the capital of Karnataka?\n ","Question2\n" "Who was the first president of india?\n","Question 3\n" "What is the ancient language of india?\n","Question4\n" "Who was the first female president of india?\n",]
    answers=["Bengaluru","Doctor Rajendra Prasad","Sanskrit","Pratibha Patil"]
    
    a=1000
    b=2000
    c=3000
    d=4000
    
    answers1 =input(questions[0])
    if answers1.lower() == answers[0].lower():
        print("correct answer! you won",a,"rupees\n")
    else:
            print("wrong answer\n")
            print("game over\n")
    
    answers2 = input(questions[1])
    if answers2.lower()== answers[1].lower():
        print("well done! you have won",b,"rupees")
    else:
        print("oh no! wrong answer\n")
        print("game over\n")
    
    answers3 = input(questions[2])
    if answers3.lower()== answers[2].lower():
        print("Thats the correct answer! you won",c,"rupees lets move ahead\n")
    else:
        print("wrong answer!\n")
        print("better luck next time\n")
    
    answers4 = input(questions[3])
    if answers4.lower() == answers[3].lower():
        print("congratulations! you've won",d,"rupees")
    else:
        print("bad luck!\n")
    
    print("It was great playing with you!\n")
    
    
