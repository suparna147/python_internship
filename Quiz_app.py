class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question['question'])
        for idx, option in enumerate(question['options'], 1):
            print(f"{idx}. {option}")

    def get_user_answer(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(self.questions[0]['options']):
                    return choice
                else:
                    print("Invalid choice. Please enter a number within the given range.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_answer(self, question, user_answer):
        correct_answer = question['answer']
        if user_answer == correct_answer:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect. The correct answer is:", question['options'][correct_answer - 1])

    def run_quiz(self):
        for question in self.questions:
            self.display_question(question)
            user_choice = self.get_user_answer()
            self.check_answer(question, user_choice)
        print("Quiz completed!")
        print("Your final score is:", self.score)


if __name__ == "__main__":
    questions = [
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Venus", "Mars", "Jupiter"],
            "answer": 2
        },
        {
            "question": "Who wrote the famous play Romeo and Juliet?",
            "options": ["William Shakespeare", "Charles Dickens", "Jane Austen"],
            "answer": 1
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "CO2", "O2"],
            "answer": 1
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Michelangelo", "Pablo Picasso", "Leonardo da Vinci"],
            "answer": 1
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["China", "Japan", "India"],
            "answer": 2
        }
    ]

    quiz = Quiz(questions)
    quiz.run_quiz()

