from questions import questions

class Game:
    def __init__(self, id):
        self.id = id
        self.ready = False
        self.balls = [None] * 10  # None for unclaimed, 0 or 1 depending on player
        self.questions = questions
        self.claimed_balls = [False] * 10
    def get_question(self, index):
        return self.questions[index + 1]

    def answer_question(self, index, player_id, answer):
        if self.claimed_balls[index]:
            return False

        if self.questions[index + 1]["answer"] == answer:
            self.balls[index] = player_id  # Player claims the ball
            self.claimed_balls[index] = True
            return True
        return False

    def all_balls_claimed(self):
        return all(ball is not None for ball in self.balls)

    def get_score(self):
        return self.balls.count(0), self.balls.count(1)  # Scores for player 0 and player 1
