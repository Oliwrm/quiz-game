from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]
for entry in question_data:
    q=entry["question"]
    a=entry["correct_answer"]
    newq=Question(q,a)
    question_bank.append(newq)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print(f"Congrats! You've completed the quiz! Your final score was: {quiz.score}/{quiz.question_number}")