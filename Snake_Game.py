import pygame
import random
import os

pygame.mixer.init()

pygame.init()

# COlors
white = (255,255,255)
red = (255,0,0)
black = (0,0,0)

screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width,screen_height))

# Background image
background_image = pygame.image.load("background_page.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height)) 

# Game Titel
pygame.display.set_caption("SNAKE GAME")
pygame.display.update()

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,55)

def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x,y])

def plot_snake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, black, [x, y, snake_size, snake_size])


def Welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill((233,200,255))
        text_screen("Welcome To Snake Game", black, 200, 250)
        text_screen("Press Space Bar To be Play This Game", black, 100, 290)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("background_music.mp3")
                    pygame.mixer.music.play()
                    gameloop()

        pygame.display.update()
        clock.tick(30)

#  game loop
def gameloop():
    # game specific variables
    exit_game = False
    game_over = False
    snake_X = 45
    snake_Y = 55
    valocity_X = 0
    valocity_Y = 0
    init_valocity = 6
    snake_list = [ ]
    snake_length = 1

    if(not os.path.exists("highScore.txt")):
        with open("highScore.txt", "w") as f:
            f.write("0")
    
    with open("highScore.txt", "r") as f:
        high_score = f.read()


    food_X = random.randint(10,screen_width/2)
    food_Y = random.randint(10, screen_height/2)
    fps = 30 # fps means Fream per seconds

    score = 0
    snake_size = 10 

    while not exit_game:
        if game_over:
            with open("highScore.txt", "w") as f:
                f.write(str(high_score))

            gameWindow.fill((255,230,210))
            text_screen("Game over! Press Enter To Continue...", red,120, 260)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        Welcome()
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        valocity_X = init_valocity
                        valocity_Y = 0

                    if event.key == pygame.K_LEFT:
                        valocity_X = -init_valocity      
                        valocity_Y = 0

                    if event.key == pygame.K_UP:
                        valocity_Y = -init_valocity
                        valocity_X = 0

                    if event.key == pygame.K_DOWN:
                        valocity_Y = init_valocity
                        valocity_X = 0

                    # Using Cheats Code this code is use to increse and decease a score in click any key
                    # if event.key == pygame.K_q:
                    #     score += 10

            snake_X += valocity_X
            snake_Y += valocity_Y

            if abs(snake_X - food_X)<6 and abs(snake_Y - food_Y)<6: # abs means Absulate
                score  += 10
                # print("Score : ",score)
                food_X = random.randint(20,screen_width/2)
                food_Y = random.randint(20, screen_height/2)
                snake_length += 5

                if score > int(high_score):
                    high_score = score

            gameWindow.fill((230,255,230))
            gameWindow.blit(background_image, ( 0, 0) )
            text_screen("score: "+ str(score) + "  HIgh Score: "+ str(high_score), red, 5, 5)
            pygame.draw.rect(gameWindow, red, [food_X, food_Y, snake_size, snake_size])

            head = [ ]
            head.append(snake_X)
            head.append(snake_Y)
            snake_list.append(head)

            if len(snake_list) > snake_length:
                del snake_list[0]

            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.load("game_over_music.mp3")
                pygame.mixer.music.play()

            if snake_X<0 or snake_X>screen_width or snake_Y<0 or snake_Y>screen_height:
                game_over = True
                pygame.mixer.music.load("game_over_music.mp3")
                pygame.mixer.music.play()
                # print("Game over")
            # pygame.draw.rect(gameWindow, black, [snake_X, snake_Y, snake_size, snake_size])
            plot_snake(gameWindow, black, snake_list, snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()

Welcome()
