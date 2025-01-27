from questions import questions

class Game:
    def __init__(self, id):
        self.id = id
        self.ready = False
        self.balls = [None] * 10  # None for unclaimed, 0 or 1 depending on player
        self.questions = {
            1: {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
           2: {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "O2", "CO2", "H2SO4"],
        "answer": "H2O"
    },
    3: {
        "question": "Who wrote 'Macbeth'?",
        "options": ["William Shakespeare", "Charles Dickens", "Leo Tolstoy", "Mark Twain"],
        "answer": "William Shakespeare"
    },
    4: {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": "Jupiter"
    },
    5: {
        "question": "What year did the Titanic sink?",
        "options": ["1912", "1905", "1898", "1923"],
        "answer": "1912"
    },
    6: {
        "question": "Which element has the atomic number 1?",
        "options": ["Oxygen", "Hydrogen", "Helium", "Carbon"],
        "answer": "Hydrogen"
    },
    7: {
        "question": "What is the fastest land animal?",
        "options": ["Cheetah", "Lion", "Eagle", "Horse"],
        "answer": "Cheetah"
    },
    8: {
        "question": "What is the main ingredient in guacamole?",
        "options": ["Tomato", "Avocado", "Onion", "Pepper"],
        "answer": "Avocado"
    },
    9: {
        "question": "Who painted the Mona Lisa?",
        "options": ["Leonardo da Vinci", "Vincent Van Gogh", "Pablo Picasso", "Claude Monet"],
        "answer": "Leonardo da Vinci"
    },
            10: {"question": "What is the hardest natural substance on Earth?", "options": ["Gold", "Iron", "Diamond", "Quartz"], "answer": "Diamond"}
        }

    def get_question(self, index):
        return self.questions[index + 1]

    def answer_question(self, index, player_id, answer):
        if self.questions[index + 1]["answer"] == answer:
            self.balls[index] = player_id  # Player claims the ball
            return True
        return False

    def all_balls_claimed(self):
        return all(ball is not None for ball in self.balls)

    def get_score(self):
        return self.balls.count(0), self.balls.count(1)  # Scores for player 0 and player 1
