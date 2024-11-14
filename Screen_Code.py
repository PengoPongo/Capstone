import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,480))     # setting screen size
pygame.display.set_caption('Capstone')      # name of window
clock = pygame.time.Clock()     # sets up clock in project

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (209, 42, 42)
GREEN = (54, 214, 54)
BLUE = (91, 91, 255)
GRAY = (201, 201, 201)

# Define states
HOME, IMAGE_SELECTION, TIMER = 0, 1, 2
current_state = HOME

# Function to display a title bar with shadow
def display_title(title, color):
    pygame.draw.rect(screen, GRAY, (3, 3, 800, 40))  # Shadow
    pygame.draw.rect(screen, color, (0, 0, 800, 40))  # Title bar
    font = pygame.font.Font(None, 36)
    text = font.render(title, True, BLACK)
    screen.blit(text, (400 - text.get_width() // 2, 5))

# Home screen display function
def display_home_screen():
    screen.fill(WHITE)
    display_title("Home", RED)

    # Draw two boxes with shadows and outlines
    box_rect1 = pygame.Rect(350, 80, 100, 100)
    box_rect2 = pygame.Rect(350, 250, 100, 100)

    pygame.draw.rect(screen, GRAY, box_rect1.move(7, 7), border_radius=15)
    pygame.draw.rect(screen, GREEN, box_rect1, border_radius=15)
    pygame.draw.rect(screen, BLACK, box_rect1.inflate(6, 6), 3, border_radius=18)  # Outline

    pygame.draw.rect(screen, GRAY, box_rect2.move(7, 7), border_radius=15)
    pygame.draw.rect(screen, BLUE, box_rect2, border_radius=15)
    pygame.draw.rect(screen, BLACK, box_rect2.inflate(6, 6), 3, border_radius=18)  # Outline

    # Additional shapes/text
    pygame.draw.circle(screen, BLACK, box_rect1.center, 15)
    pygame.draw.rect(screen, BLACK, box_rect1.inflate(-30, -50), 1)
    pygame.draw.rect(screen, BLACK, box_rect1.inflate(-30, -50), 2)

    font = pygame.font.Font(None, 24)
    text1 = font.render("Image Selection", True, BLACK)
    text2 = font.render("Timer Countdown", True, BLACK)
    screen.blit(text1, (340, 190))
    screen.blit(text2, (340, 360))


# Image selection screen display function
def display_image_selection_screen():
    screen.fill(WHITE)
    display_title("Image Selection", GREEN)

    # Large circle in center
    pygame.draw.circle(screen, BLACK, (400, 260), 200, 3)

    font = pygame.font.Font(None, 36)
    text = font.render("Image for Timer", True, BLACK)
    screen.blit(text, (400 - text.get_width() // 2, 50))


# Timer screen display function
def display_timer_screen():
    screen.fill(WHITE)
    display_title("Timer", BLUE)

    # Filled circle with outline
    pygame.draw.circle(screen, BLUE, (400, 260), 200)
    circle_border = pygame.draw.circle(screen, BLACK, (400, 260), 200, 3)
    timer_image = pygame.image.load('Image/blinka.JPG')
    screen.blit(timer_image, circle_border.center)

    # Display text
    font = pygame.font.Font(None, 36)
    text = font.render("Time Set to __ minutes", True, BLACK)
    screen.blit(text, (400 - text.get_width() // 2, 50))


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                current_state = HOME
            elif event.key == pygame.K_2:
                current_state = IMAGE_SELECTION
            elif event.key == pygame.K_3:
                current_state = TIMER

    # Display the current screen based on state
    if current_state == HOME:
        display_home_screen()
    elif current_state == IMAGE_SELECTION:
        display_image_selection_screen()
    elif current_state == TIMER:
        display_timer_screen()

    pygame.display.update()
    clock.tick(60)
