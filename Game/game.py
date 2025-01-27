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

   
    def get_scores(self):
        # Calculate the scores for each player
        player_0_score = self.balls.count(0)
        player_1_score = self.balls.count(1)
        return player_0_score, player_1_score

    def get_winner(self):
        # Determine the winner based on scores
        player_0_score, player_1_score = self.get_scores()
        if player_0_score > player_1_score:
            return "Player 1 (Red)", player_0_score, player_1_score
        elif player_1_score > player_0_score:
            return "Player 2 (Green)", player_0_score, player_1_score
        else:
            return "It's a Tie!", player_0_score, player_1_score