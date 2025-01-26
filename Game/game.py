import random

class Game:
    def __init__(self, id):
        self.id = id
        self.ready = False
        self.players = [False, False, False]  # Tracks whether each of the three players has joined
        self.balls = [None] * 10  # Represents the 10 balls, None means unclaimed
        self.scores = [0, 0, 0]  # Tracks the number of balls each player has claimed

    def connect_player(self):
        for i in range(3):
            if not self.players[i]:
                self.players[i] = True
                if all(self.players):
                    self.ready = True
                return i
        return None  # If all players are already connected

    def play(self, player, ball_index, answer):
        # This method will handle player's attempts to claim a ball
        if self.balls[ball_index] is None:  # Check if the ball is still unclaimed
            correct_answer = self.get_correct_answer(ball_index)  # Get correct answer for the quiz at this ball
            if answer.lower() == correct_answer.lower():
                self.balls[ball_index] = player
                self.scores[player] += 1
                return True
            else:
                return False
        return False

    def get_correct_answer(self, ball_index):
        # Placeholder for getting the correct answer, this should be implemented based on your quiz logic
        # For example, you could have a dictionary of questions and answers, or fetch from a database
        return "correct_answer"  # Just a placeholder

    def check_winner(self):
        # Determines if the game is over and who the winner is
        if None not in self.balls:  # Check if all balls are claimed
            # Game is over, determine who has the most balls
            max_score = max(self.scores)
            winners = [i for i, score in enumerate(self.scores) if score == max_score]
            return winners  # Can be more than one winner if scores are tied
        return None

    def reset_game(self):
        # Resets the game to start over, but keeping the same players
        self.balls = [None] * 10
        self.scores = [0, 0, 0]

