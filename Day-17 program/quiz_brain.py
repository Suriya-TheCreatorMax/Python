#Author : Susindhar M
#Date   : 06.07.2023
#class-definition-for-quiz-program

class QuizBrain:
	def __init__(self,qList):
		self.question_number = 0
		self.question_list = qList
		self.score = 0
	
	#Method to display question and forward answer to check_answer method
	def next_question(self):
		current_question = self.question_list[self.question_number]
		self.question_number += 1
		ans = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
		self.check_answer(ans, current_question.answer)
	
	#Method to check if there are questions left
	def still_has_questions(self):
		if self.question_number != len(self.question_list):
			return 1
		else : return 0
	
	#Method to check the correctness of the given answer
	def check_answer(self, user_answer, correct_answer) :
		if user_answer.lower()==correct_answer.lower() :
			print("The answer is correct :)")
			self.score += 1

		else:
			print("Sorry you got it wrong :(")
		print("The correct answer is ", correct_answer)
		print(f"Your current score is :{self.score}/{self.question_number}")
 