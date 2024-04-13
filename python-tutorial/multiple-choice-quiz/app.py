
from Question import Question

question_prompts = ["What is the color of the apples? \n (a) Red/Green \n(b) Purple \n(c) Orange \n\n",
                    "What is the color of the bananas? \n (a) Teal \n(b) Magenta \n(c) Yellow \n\n",
                    "What is the color of the strawberries? \n (a) Yellow \n(b) Red \n(c) Blue \n\n"]

questions =[ Question(question_prompts[0],"a"),
             Question(question_prompts[1],"c"),
             Question(question_prompts[2],"b")]


def quizz_init(questions):
    score =0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer :
            score +=1
    print("You scored " +str(score) +"/3 questions correct")


quizz_init(questions)