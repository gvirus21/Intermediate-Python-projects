from quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank=[]
for item in question_data:
    question=item["text"]
    answer=item["answer"]
    new_question=Question(question,answer)
    question_bank.append(new_question)

quiz=QuizBrain(question_bank)

while quiz.still_has_questions() :
    quiz.nextQuestion()

print("you've completed the quiz!!")
print(f"your final score is: {quiz.score}/{quiz.question_number}")
