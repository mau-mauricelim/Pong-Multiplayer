import pygame
import winsound
import random

# -------------------- Game setup --------------------
# Setting up a class for the character (object)
class Player():
    def __init__(self, x, y, width, height, color, ballx, bally, balldx, balldy, ballrad, ballcol):
        # Paddle
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height) # to draw character faster
        self.vel = 5 # vel definition
        self.score = [0, 0]
        self.ready = [0, 0]
        self.pause = [0, 0]
        self.restart = [0, 0]

        # Ball
        self.ballx = ballx
        self.bally = bally
        self.ballrad = ballrad
        self.ballcol = ballcol
        self.balldx = balldx # delta x
        self.balldy = balldy
        self.circle = (ballx, bally, balldx, balldy)

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect) # to draw character on the window
        pygame.draw.circle(win, self.ballcol, (self.ballx, self.bally), self.ballrad) # to draw ball on the window

    def move_paddle(self):
        keys = pygame.key.get_pressed() # dictionary of keys with a value of 0 or 1, allows for more than 1 key press

        # checking for events: keys pressed
        if keys[pygame.K_UP]:
            self.y -= self.vel
        if keys[pygame.K_DOWN]:
            self.y += self.vel

        # Paddle border check
        if self.y < 0:
            self.y = 0
        if self.y > 500:
            self.y = 500

        self.update()

    def move_ball(self):
        # Ball movement
        self.ballx += self.balldx
        self.bally += self.balldy
        # Ball border checking
        # width=800, height=600
        # top
        if self.bally <= 15:
            self.balldy *= -1
            winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)

        # bottom
        if self.bally >= 585:
            self.balldy *= -1
            winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)

        self.update()

    def change_ball_speed_and_score(self, score):
        # Point won/loss
        p1_score = score[0]
        p2_score = score[1]
        threshold_speed = 8 # speed above 8 cannot detect the collision...i think its caused by the step size
        threshold_score_1 = 1
        threshold_score_2 = 4
        threshold_score_3 = 7
        cond1 = threshold_score_1 < p1_score < threshold_score_2 and threshold_score_1 < p2_score < threshold_score_2
        cond2 = threshold_score_2 < p1_score < threshold_score_3 and threshold_score_2 < p2_score < threshold_score_3
        cond3 = threshold_score_3 < p1_score and threshold_score_3 < p2_score
        cond4 = p1_score <= threshold_score_1 and p2_score <= threshold_score_1

        if self.ballx < 10:
            self.ballx = 400
            self.bally = 300
            if self.balldy > 0 and cond4:
                self.balldy = abs(self.balldx) + random.randint(-1, 1)
            elif self.balldy < 0 and cond4:
                self.balldy = -abs(self.balldx) + random.randint(-1, 1)
            if self.balldy > 0 and self.balldy < threshold_speed and (cond1 or cond2 or cond3):
                self.balldy = abs(self.balldx) + random.randint(0,1)
            elif self.balldy < 0 and self.balldy > -threshold_speed and (cond1 or cond2 or cond3):
                self.balldy = -abs(self.balldx) - random.randint(0,1)
            if self.balldx > 0 and self.balldx < threshold_speed and (cond1 or cond2 or cond3):
                self.balldx += 1 # increments only can be made using an integer...
            elif self.balldx < 0 and self.balldx > -threshold_speed and (cond1 or cond2 or cond3):
                self.balldx -= 1
            if self.balldy == threshold_speed:
                self.balldy -= random.randint(0,1)
            elif self.balldy == -threshold_speed:
                self.balldy += random.randint(0, 1)
            if self.balldy > threshold_speed:
                self.balldy -= 1
            elif self.balldy < -threshold_speed:
                self.balldy += 1

            self.balldx *= -1
            self.balldy *= -1
            self.score[1] += 1

        if self.ballx > 790:
            self.ballx = 400
            self.bally = 300
            if self.balldy > 0 and cond4:
                self.balldy = abs(self.balldx) + random.randint(-1, 1)
            elif self.balldy < 0 and cond4:
                self.balldy = -abs(self.balldx) + random.randint(-1, 1)
            if self.balldy > 0 and self.balldy < threshold_speed and (cond1 or cond2 or cond3):
                self.balldy = abs(self.balldx) + random.randint(0, 1)
            elif self.balldy < 0 and self.balldy > -threshold_speed and (cond1 or cond2 or cond3):
                self.balldy = -abs(self.balldx) - random.randint(0, 1)
            if self.balldx > 0 and self.balldx < threshold_speed and (cond1 or cond2 or cond3):
                self.balldx += 1  # increments only can be made using an integer...
            elif self.balldx < 0 and self.balldx > -threshold_speed and (cond1 or cond2 or cond3):
                self.balldx -= 1
            if self.balldy == threshold_speed:
                self.balldy -= random.randint(0, 1)
            elif self.balldy == -threshold_speed:
                self.balldy += random.randint(0, 1)
            if self.balldy > threshold_speed:
                self.balldy -= 1
            elif self.balldy < -threshold_speed:
                self.balldy += 1

            self.balldx *= -1
            self.balldy *= -1
            self.score[0] += 1

        self.update()

    def update(self):
        # update using self
        # previously only using input parameters
        self.rect = (self.x, self.y, self.width, self.height)
        self.circle = (self.ballx, self.bally, self.balldx, self.balldy)

    def ready_screen(self):
        keys = pygame.key.get_pressed()  # dictionary of keys with a value of 0 or 1, allows for more than 1 key press
        if keys[pygame.K_SPACE]:
            if self.ready[0] == 0 and self.x == 40:
                self.ready[0] += 1
            elif self.ready[1] == 0 and self.x == 740:
                self.ready[1] += 1

    def pause_screen(self):
        keys = pygame.key.get_pressed()  # dictionary of keys with a value of 0 or 1, allows for more than 1 key press
        if keys[pygame.K_p]:
            if self.pause[0] == 0 and self.x == 40:
                self.pause[0] += 1
            elif self.pause[1] == 0 and self.x == 740:
                self.pause[1] += 1
            elif self.pause[0] == 1 and self.x == 40:
                self.pause[0] -= 1
            elif self.pause[1] == 1 and self.x == 740:
                self.pause[1] -= 1

    def restart_screen(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            if self.restart[0] == 0 and self.x == 40:
                self.restart[0] += 1
            elif self.restart[1] == 0 and self.x == 740:
                self.restart[1] += 1