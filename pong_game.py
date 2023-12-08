import pygame
import random
import sys
import time
import json

pygame.init()
font = pygame.font.Font(None, 36)

player_score = 0
with open("configurations.json", "r") as json_file:
    configurations = json.load(json_file)
opponent_score = configurations.get("opponent_score", 0)

def render_pong_game(surface):
    surface.fill(bg_color)

    # Draw game elements on the surface
    pygame.draw.rect(surface, red, player)
    pygame.draw.rect(surface, blue, opponent)
    pygame.draw.ellipse(surface, green, ball)
    pygame.draw.aaline(surface, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
    font = pygame.font.Font(None, 36)


def welcome_screen():
    welcome_text = font.render('Welcome To Pong: First to 3 Wins', True, red)
    game_info = font.render('Use Up/Down Arrow to Move Player', True, light_grey)
    screen.blit(welcome_text, (screen_width / 2 - 200, screen_height / 2 - 50))
    screen.blit(game_info, (screen_width/2 -210, screen_height/2 - 10))
    pygame.display.flip()
    time.sleep(5)


def display_scores():
    player_text = font.render(str(player_score), True, light_grey)
    opponent_text = font.render(str(opponent_score), True, light_grey)
    screen.blit(player_text, (screen_width - 50, 20))
    screen.blit(opponent_text, (20, 20))
    # Update the display
    pygame.display.flip()


def ball_animation():
    global ball_speed_x, ball_speed_y, opponent_score, player_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    if ball.left <= 0:
        player_score += 1
        ball_restart()

    if ball.right >= screen_width:
        opponent_score += 1
        ball_restart()

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1


with open("configurations.json", "r") as json_file:
    configurations = json.load(json_file)

player_color = configurations.get("player_color", (255, 0, 0))
ball_color = configurations.get("ball_color", (255, 0, 0))
opponent_color = configurations.get("opponent_color", (255, 0, 0))
player_speed = configurations.get("player_speed", 0)
opponent_speed = configurations.get("opponent_speed", 7)

def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height


def opponent_ai():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= screen_height:
        opponent.bottom = screen_height


def ball_restart():
    global ball_speed_x, ball_speed_y, opponent_score, player_score
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


pygame.init()
clock = pygame.time.Clock()

screen_width = 1250
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong')
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)
red = (255, 0, 0)
orange = (255, 130, 85)
green = (0, 255, 0)
blue = (0, 0, 255)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))

welcome_screen()


def game_over():
    game_over_text = font.render('Game Over', True, (255, 255, 255))
    screen.blit(game_over_text, (screen_width // 2 - 70, screen_height // 2))
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()


def end_game():
    global player_score, opponent_score, player_speed
    if player_score == 3 or opponent_score == 3:
        game_over()



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
    ball_animation()
    player_animation()
    opponent_ai()
    end_game()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, player_color, player)
    pygame.draw.rect(screen, opponent_color, opponent)
    pygame.draw.ellipse(screen, ball_color, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
    display_scores()

    pygame.display.flip()
    clock.tick(60)
