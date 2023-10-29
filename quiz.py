questions =["1. What is the longest bone in the human body?",
            "2. What is the largest ocean on Earth?",
            "3. What is the largest city in the world?",
            "4. What is the capital of Italy?",
            "5. What is the largest planet in our solar system?",
            "6. What is the primary language spoken in Brazil?",
            "7. What is the tallest mountain in the world?",
            "8. Which is the nearest planet to our sun?",
            "9. What is the coldest planet in the solar system?",
            "10 What is the largest ocean trench on Earth?"]
answers = ["femur","pacific","tokyo","venice","jupiter","portuguese","everest","mercury","neptune","mariana trench"]
totalMark = 0
name = input("To enter the quiz type in your name:\n")
print("Let's start the quiz, Good Luck!")
for quizLoop in range(len(questions)):
    currentQuestion = questions[quizLoop]
    realAnswer = answers[quizLoop]
    print(currentQuestion)
    currentAnswer = input("Your answer: ".lower())
    if currentAnswer == realAnswer:
        totalMark += 1

comment = ""
if totalMark >= 6:
    comment = "You are smarter than i expected!"
elif totalMark >= 3 and totalMark < 6:
    comment = "You can do better!"
else:
    comment = "YOU FAILED..... Well,good luck next time."

print("Hello",name,",you got a",totalMark,"/ 10 in this quiz.",comment )