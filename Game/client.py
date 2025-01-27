import pygame
import pickle
from network import Network

pygame.font.init()

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

class Ball:
    def __init__(self, x, y, radius, color=(0, 0, 255)):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def click(self, pos):
        distance = ((self.x - pos[0]) ** 2 + (self.y - pos[1]) ** 2) ** 0.5
        return distance <= self.radius

def redraw_window(win, game, balls, player):
   
    background = pygame.image.load("background.png")
    background = pygame.transform.scale(background, (width, height))
    win.blit(background, (0, 0))

    if not game.ready:
        draw_text(win, "Waiting for the pair...", (width // 2 - 150, height // 2 - 20), 50, (255, 245, 0))
        pygame.display.update()
        return
    for index, ball in enumerate(balls):
        if game.balls[index] is None:
            ball.color = (0, 0, 255)
        elif game.balls[index] == 0:
            ball.color = (255, 0, 0)
        else:
            ball.color = (0, 255, 0)
        ball.draw(win)


    draw_text(win, f"You are player {player}", (10, 10), 20, (0, 0, 0))
    pygame.display.update()

def draw_text(win, text, pos, size, color):
    font = pygame.font.SysFont("comicsans", size)
    render = font.render(text, True, color)
    win.blit(render, pos)

def draw_button(win, text, pos, size, color, bg):
    # Ensure 'size' here refers to the font size, not the button size
    # Let's say 'font_size' should be an integer value you pass to the function
    font_size = 20  # or another appropriate value for your design
    font = pygame.font.SysFont("comicsans", font_size)
    text_render = font.render(text, True, color)
    text_rect = text_render.get_rect(center=(pos[0] + size[0] // 2, pos[1] + size[1] // 2))
    pygame.draw.rect(win, bg, (pos[0], pos[1], size[0], size[1]))
    win.blit(text_render, text_rect)
    return text_rect

def draw_overlay(win, question, options):
    # Cover the entire window with a semi-transparent overlay
    overlay = pygame.Surface((width, height))
    overlay.set_alpha(128)  # Transparency level
    overlay.fill((0, 0, 0))
    win.blit(overlay, (0, 0))

    # Draw the question
    draw_text(win, question, (50, 50), 30, (255, 255, 255))

    # Draw options as buttons and return their rects for click detection
    buttons = []
    for idx, option in enumerate(options):
        rect = draw_button(win, option, (50, 150 + 60 * idx), (600, 50), (255, 255, 255), (100, 100, 100))
        buttons.append(rect)
    pygame.display.update()
    return buttons

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    player = int(n.getP())
    print("You are player", player)
    balls = [Ball(100 * (i % 5) + 50, 100 * (i // 5) + 50, 30) for i in range(10)]
  
    question_active = False
    option_buttons = []

    while run:
        if not question_active:
            response = n.send("get")
            game = pickle.loads(response)
            redraw_window(win, game, balls, player)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if not question_active and game.ready:
                    for i, ball in enumerate(balls):
                        if ball.click(pos):
                            response = n.send(f"get_question {i}")
                            game = pickle.loads(response)
                            active_question = game.get_question(i)
                            option_buttons = draw_overlay(win, active_question['question'], active_question['options'])
                            question_active = True
                            break
                else:
                    for idx, rect in enumerate(option_buttons):
                        if rect.collidepoint(pos):
                            user_answer = active_question['options'][idx]
                            response = n.send(f"answer {i} {user_answer}")
                            correct = pickle.loads(response)
                            if correct:
                                print("Correct!")
                            else:
                                print("Wrong!")
                            question_active = False
                            pygame.display.update()  # Redraw the original game window
                            break

    pygame.quit()

if __name__ == "__main__":
    main()