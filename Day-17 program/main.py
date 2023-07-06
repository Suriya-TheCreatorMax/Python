#Author : Susindhar M
#Date   : 06.07.2023
#quiz-program-day-17

#Importing methods and data from class files
from question_model import Questions
from data import question_data
from quiz_brain import QuizBrain

#Creating a question bank from data
question_bank=[]
for q in question_data: 
	Question = Questions(q["text"],q["answer"])
	question_bank.append(Question)

#Start the quiz
quiz = QuizBrain(question_bank)
while quiz.still_has_questions() :
	quiz.next_question()

#Conclude the quiz
print("Thank you for taking the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")