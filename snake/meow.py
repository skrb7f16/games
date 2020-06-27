import pygame
import random
pygame.init()
#colors
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
meow=(223,34,233)



#creating Window
gameWindow=pygame.display.set_mode((1200, 600))
pygame.display.set_caption("meow game")
pygame.display.update()


font=pygame.font.SysFont(None, 55)
clock = pygame.time.Clock()
def textdisplay(text,color,x,y):
    screentext=font.render(text,True,color)
    gameWindow.blit(screentext,(x,y))

def plotsnake(gameWindow, color, snake_list, snake_size):
    for x,y in snake_list:
        pygame.draw.rect(gameWindow, color, [x,y,snake_size,snake_size])


def welcome():
    exit_game=False
    while not exit_game:
        gameWindow.fill(meow)
        textdisplay("Welcome to my Meow Snake game", black, 200,300)
        textdisplay("Press Space to start the game", black, 220,350)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(30)


def gameloop():
    # setting variable
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 45
    snake_size = 15
    food_size = 15
    fps = 30
    velocity_x = 0
    velocity_y = 0
    food_x = random.randint(20, 800)
    food_y = random.randint(20, 400)
    score = 0
    snake_list = []
    snake_lenght = 1

    try:
        with open("hiscore.txt", "r") as f:
            hiscore=int(f.read())
    except:
        with open("hiscore.txt", "w") as f:
            f.write("0")
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            textdisplay("Game over :( \n Press enter to continue", red, 150,300)
            textdisplay("Your Score is :"+str(score), red, 150,400)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game=True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x=10
                        velocity_y=0
                    if event.key == pygame.K_LEFT:
                        velocity_x=-10
                        velocity_y=0
                    if event.key == pygame.K_UP:
                        velocity_y=-10
                        velocity_x=0
                    if event.key == pygame.K_DOWN:
                        velocity_y = 10
                        velocity_x = 0
                if event.type == pygame.QUIT:
                    exit_game=True
            snake_x=snake_x+velocity_x
            snake_y=snake_y+velocity_y

            if abs(snake_x-food_x)<10 and abs(snake_y-food_y)<10:
                score=score+10
                food_x = random.randint(20, 800)
                food_y = random.randint(20, 400)
                snake_lenght+=1
                if score > hiscore:
                    hiscore = score



            gameWindow.fill(white)
            pygame.draw.rect(gameWindow, black,[food_x,food_y,snake_size, snake_size])
            textdisplay("Score:" + str(score), red, 5, 5)
            textdisplay("hiscore:" + str(hiscore), red, 500,5)
            with open("hiscore.txt", "w") as f:
                f.write(str(hiscore))
            head=[]
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list)>snake_lenght:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over=True
            plotsnake(gameWindow,red,snake_list,snake_size)

            if snake_x<0:
                snake_x=snake_x+1200
            if snake_x>1200:
                snake_x=snake_x-1200
            if snake_y<0:
                snake_y+=600
            if snake_y>600:
                snake_y-=600


        pygame.display.update()
        clock.tick(fps)

    #quiting the game
    pygame.quit()
    quit()


welcome()