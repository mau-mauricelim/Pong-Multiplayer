from network import Network # capitalise Network since it was defined this way inside the py file as class
import os
from gamesetup import *
import winsound
import numpy as np

pygame.init()

# -------------------- Window --------------------
width = 800
height = 600
# center the display
os.environ['SDL_VIDEO_CENTERED'] = "True"
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Pong Multiplayer")

def display_countdown(player, player2):
    global oncep1ready, oncep2ready
    if oncep1ready == False:
        oncep1ready = True
        font = pygame.font.Font(None, 55)
        text = font.render("Press \"Spacebar\" when ready!", 1, (255, 255, 255))
        win.blit(text, (120, 20))
        text = font.render("Player 1 ready!", 1, (255, 0, 0))
        win.blit(text, (70, 280))
        text = font.render("Player 2 ready!", 1, (0, 0, 255))
        win.blit(text, (450, 280))
        winsound.PlaySound("sounds/ready.wav", winsound.SND_ASYNC)
        player.draw(win)  # draw player inside window
        player2.draw(win)
        pygame.display.update()
        pygame.time.wait(1000)
    elif oncep2ready == False:
        oncep2ready = True
        font = pygame.font.Font(None, 55)
        text = font.render("Press \"Spacebar\" when ready!", 1, (255, 255, 255))
        win.blit(text, (120, 20))
        text = font.render("Player 1 ready!", 1, (255, 0, 0))
        win.blit(text, (70, 280))
        text = font.render("Player 2 ready!", 1, (0, 0, 255))
        win.blit(text, (450, 280))
        winsound.PlaySound("sounds/ready.wav", winsound.SND_ASYNC)
        player.draw(win)  # draw player inside window
        player2.draw(win)
        pygame.display.update()
        pygame.time.wait(1000)

    font = pygame.font.Font(None, 80)
    countdown_timer = ["3", "2", "1"]
    winsound.PlaySound("sounds/321go.wav", winsound.SND_ASYNC)
    for i in range(len(countdown_timer)):
        win.fill((0, 0, 0))  # fill with black color
        text = font.render(countdown_timer[i], 1, (255, 255, 0))
        win.blit(text, (385, 220))
        player.draw(win)  # draw player inside window
        player2.draw(win)
        pygame.display.update()
        pygame.time.wait(600)


oncep1ready = False
oncep2ready = False
gameover = False
gameoversound = False
challengerarrivedsound = False
challengeacceptedsound = False
p1challenge = False
p2challenge = False
challengeaccepted = False
def redrawWindow(win, player, player2):
    win.fill((0, 0, 0)) # fill with black color
    ready_test = np.array(player.ready) + np.array(player2.ready)
    pause_test = np.array(player.pause) + np.array(player2.pause)

    score_test = np.array(player.score) + np.array(player2.score)
    gameoverscore = 10 # default 10

    restart_test = np.array(player.restart) + np.array(player2.restart)

    # Game over
    global gameover, gameoversound, challengerarrivedsound, challengeacceptedsound, p1challenge, p2challenge, challengeaccepted
    if score_test[0] == gameoverscore or score_test[1] == gameoverscore:
        gameover = True
        if gameoversound == False:
            winsound.PlaySound("sounds/victory.wav", winsound.SND_ASYNC)
            gameoversound = True

        # Display scores:
        font = pygame.font.Font(None, 55)
        text = font.render("Player 1: " + str(score_test[0]), 1, (255, 255, 255))
        win.blit(text, (80, 10))
        text = font.render("Player 2: " + str(score_test[1]), 1, (255, 255, 255))
        win.blit(text, (510, 10))
        font = pygame.font.Font(None, 80)
        text = font.render("Gameover!", 1, (255, 255, 255))
        win.blit(text, (240, 220))
        font = pygame.font.Font(None, 55)

        if score_test[0] == gameoverscore:
            text = font.render("Player 1 wins!", 1, (255, 255, 255))
            win.blit(text, (260, 340))
        if score_test[1] == gameoverscore:
            text = font.render("Player 2 wins!", 1, (255, 255, 255))
            win.blit(text, (260, 340))
        # display help
        font = pygame.font.Font(None, 25)
        text = font.render("Press \"enter\" to restart game", 1, (255, 255, 255))
        win.blit(text, (270, 580))
        # display restart screen
        font = pygame.font.Font(None, 55)

        if restart_test[0] == 1 and restart_test[1] == 0:
            text = font.render("Player 1 wants a rematch. Do you accept?", 1, (255, 0, 0))
            win.blit(text, (20, 130))
            p1challenge = True
        elif restart_test[0] == 0 and restart_test[1] == 1:
            text = font.render("Player 2 wants a rematch. Do you accept?", 1, (0, 0, 255))
            win.blit(text, (20, 130))
            p2challenge = True

        if (p1challenge == True or p2challenge == True) and challengerarrivedsound == False:
            winsound.PlaySound("sounds/challengerarrived.wav", winsound.SND_ASYNC)
            challengerarrivedsound = True

        if restart_test[0] == 1 and restart_test[1] == 1 and p1challenge == True:
            text = font.render("Player 1 wants a rematch. Do you accept?", 1, (255, 0, 0))
            win.blit(text, (20, 130))
            font = pygame.font.Font(None, 80)
            text = font.render("Challenge accepted!", 1, (0, 0, 255))
            win.blit(text, (120, 450))
            challengeaccepted = True
        elif restart_test[0] == 1 and restart_test[1] == 1 and p2challenge == True:
            text = font.render("Player 2 wants a rematch. Do you accept?", 1, (0, 0, 255))
            win.blit(text, (20, 130))
            font = pygame.font.Font(None, 80)
            text = font.render("Challenge accepted!", 1, (255, 0, 0))
            win.blit(text, (120, 450))
            challengeaccepted = True

        if challengeaccepted == True and challengeacceptedsound == False:
            winsound.PlaySound("sounds/challengeaccepted.wav", winsound.SND_ASYNC)
            challengeacceptedsound = True

    if ready_test[0] == 1 and ready_test[1] == 1 and pause_test[0] == 0 and pause_test[1] == 0 and gameover == False:
        global both_ready, countdown_start
        both_ready = True

        if countdown_start == 0:
            countdown_start += 1
        elif countdown_start == 1:
            # Display countdown:
            display_countdown(player, player2) # call function
            countdown_start += 1
        else:
            # display help when countdown finishes; game starts
            font = pygame.font.Font(None, 25)
            text = font.render("Press \"p\" to pause game", 1, (255, 255, 255))
            win.blit(text, (300, 580))

        # Display scores:
        font = pygame.font.Font(None, 55)
        text = font.render("Player 1: " + str(score_test[0]), 1, (255, 255, 255))
        win.blit(text, (80, 10))
        text = font.render("Player 2: " + str(score_test[1]), 1, (255, 255, 255))
        win.blit(text, (510, 10))

        # Paddle and Ball collissions
        if (player.ballx > 65 and player.ballx < 70) and player.bally in range(player.y-10, player.y+110, 1):
            player.balldx *= -1
            winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)
        if (player.ballx > 735 and player.ballx < 740) and player.bally in range(player2.y-10, player2.y+110, 1):
            player.balldx *= -1
            winsound.PlaySound("sounds/bounce.wav", winsound.SND_ASYNC)

    elif ready_test[0] == 1 and ready_test[1] == 0 and pause_test[0] == 0 and pause_test[1] == 0:
        font = pygame.font.Font(None, 55)
        text = font.render("Press \"Spacebar\" when ready!", 1, (255, 255, 255))
        win.blit(text, (120, 20))
        text = font.render("Player 1 ready!", 1, (255, 0, 0))
        win.blit(text, (70, 280))
        global oncep1ready
        if oncep1ready == False:
            winsound.PlaySound("sounds/ready.wav", winsound.SND_ASYNC)
            oncep1ready = True

    elif ready_test[0] == 0 and ready_test[1] == 1 and pause_test[0] == 0 and pause_test[1] == 0:
        font = pygame.font.Font(None, 55)
        text = font.render("Press \"Spacebar\" when ready!", 1, (255, 255, 255))
        win.blit(text, (120, 20))
        text = font.render("Player 2 ready!", 1, (0, 0, 255))
        win.blit(text, (450, 280))
        global oncep2ready
        if oncep2ready == False:
            winsound.PlaySound("sounds/ready.wav", winsound.SND_ASYNC)
            oncep2ready = True

    if ready_test[0] == 0 and ready_test[1] == 0 and pause_test[0] == 0 and pause_test[1] == 0:
        font = pygame.font.Font(None, 55)
        text = font.render("Press \"Spacebar\" when ready!", 1, (255, 255, 255))
        win.blit(text, (120, 20))

    if pause_test[0] == 1 and pause_test[1] == 0:
        font = pygame.font.Font(None, 55)
        text = font.render("Player 1 paused", 1, (255, 0, 0))
        win.blit(text, (260, 220))
    elif pause_test[0] == 0 and pause_test[1] == 1:
        font = pygame.font.Font(None, 55)
        text = font.render("Player 2 paused", 1, (0, 0, 255))
        win.blit(text, (260, 340))
    elif pause_test[0] == 1 and pause_test[1] == 1:
        font = pygame.font.Font(None, 55)
        text = font.render("Player 1 paused", 1, (255, 0, 0))
        win.blit(text, (260, 220))
        text = font.render("Player 2 paused", 1, (0, 0, 255))
        win.blit(text, (260, 340))


    player.draw(win)  # draw player inside window
    player2.draw(win)
    pygame.display.update()


# -------------------- Main Game loop --------------------

both_ready = False
startup = False
countdown_start = 0
def main():
    global startup
    run = True
    n = Network() # connect to network
    p = n.getP() # from Network class in network.py

    clock = pygame.time.Clock()

    while run:
        clock.tick(60) # 60fps
        # for player 2
        p2 = n.send(p)

        for event in pygame.event.get(): # event in Pygame
            if event.type == pygame.QUIT:
                run = False # stop the main loop
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    p.pause_screen()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    p.ready_screen()
                if event.key == pygame.K_RETURN and gameover == True:
                    p.restart_screen()

        # -------------------- test cases --------------------
        # print(p.ready, p2.ready)
        # print(p.score, p2.score)
        # print(p.pause, p2.pause)
        # print(p.balldx, p.balldy, p2.balldx, p2.balldy)
        # print(p.restart, p2.restart)

        score_test = np.array(p.score) + np.array(p2.score)
        p.change_ball_speed_and_score(score_test)

        if startup == False:
            winsound.PlaySound("sounds/getready.wav", winsound.SND_ASYNC)
            startup = True

        pause_test = np.array(p.pause) + np.array(p2.pause)
        if pause_test[0] == 0 and pause_test[1] == 0 and both_ready == True and countdown_start != 1 and gameover == False:
            p.move_paddle() # move characters based on what keys are pressed then redraw the window
            p.move_ball()
            redrawWindow(win, p, p2)  # linked to for event loop

        else:
            p.move_paddle()
            redrawWindow(win, p, p2) # linked to for event loop

main()
# main() # executing main function
# can also use while loop