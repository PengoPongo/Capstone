import pygame
import math
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 480))  # Setting screen size
pygame.display.set_caption('Capstone')  # Name of window
clock = pygame.time.Clock()  # Sets up clock in project

# Define colors
WHITE = pygame.Color('antiquewhite')
BLACK = pygame.Color(0, 0, 0)
RED = pygame.Color('brown1')
DARKRED = pygame.Color('brown4')
GREEN = pygame.Color('seagreen3')
DARKGREEN = pygame.Color('seagreen4')
BLUE = pygame.Color('cyan3')
DARKBLUE = pygame.Color('darkcyan')
GRAY = pygame.Color('antiquewhite3')

# Define states
HOME, IMAGE_SELECTION, TIMER = 0, 1, 2
current_state = HOME

# Function to display a title bar with shadow
def display_title(title, color, border):
    pygame.draw.rect(screen, GRAY, (5, 0, 797, 45), border_radius=10)  # Shadow
    pygame.draw.rect(screen, border, (-1, -10, 801, 53), border_radius=10)
    pygame.draw.rect(screen, color, (0, -10, 800, 50), border_radius=10)  # Rounded title bar
    font = pygame.font.Font(None, 36)
    text = font.render(title, True, BLACK)
    screen.blit(text, (400 - text.get_width() // 2, 7))

# Home screen display function
def display_home_screen():
    global image_button, timer_button

    screen.fill(WHITE)
    display_title("Home", RED, DARKRED)

    # Define button dimensions
    button_width, button_height = 200, 200
    image_button = pygame.Rect(150, 160, button_width, button_height)  # Image button
    timer_button = pygame.Rect(450, 160, button_width, button_height)  # Timer button

    # Draw image button with shadow, color, and outline
    pygame.draw.rect(screen, GRAY, image_button.move(7, 7), border_radius=15)
    pygame.draw.rect(screen, GREEN, image_button, border_radius=15)
    pygame.draw.rect(screen, DARKGREEN, image_button.inflate(6, 6), 3, border_radius=18)  # Outline

    # Draw timer button with shadow, color, and outline
    pygame.draw.rect(screen, GRAY, timer_button.move(7, 7), border_radius=15)
    pygame.draw.rect(screen, BLUE, timer_button, border_radius=15)
    pygame.draw.rect(screen, DARKBLUE, timer_button.inflate(6, 6), 3, border_radius=18)  # Outline

    # Load and position icons on buttons
    timer_UI = pygame.image.load('UI/timer.PNG')
    timer_UI = pygame.transform.scale(timer_UI, (150, 150))
    screen.blit(timer_UI, (timer_button.centerx - 75, timer_button.centery - 75))  # Center the image

    camera_UI = pygame.image.load('UI/camera.PNG')
    camera_UI = pygame.transform.scale(camera_UI, (150, 150))
    screen.blit(camera_UI, (image_button.centerx - 75, image_button.centery - 75))  # Center the image

    # Add text under each button
    font = pygame.font.Font(None, 24)
    text1 = font.render("Image Selection", True, DARKGREEN)
    text2 = font.render("Timer Countdown", True, DARKBLUE)
    screen.blit(text1, (image_button.centerx - text1.get_width() // 2, image_button.bottom - 20))
    screen.blit(text2, (timer_button.centerx - text2.get_width() // 2, timer_button.bottom - 20))


# Image selection screen display function
def display_image_selection_screen():
    global home_button, timer_button

    screen.fill(WHITE)
    display_title("Image Selection", GREEN, DARKGREEN)

    button_width, button_height = 50, 50
    home_button = pygame.Rect(5, 70, button_width, button_height)  # Home button
    timer_button = pygame.Rect(5, 135, button_width, button_height)  # Timer button
    side_bar = pygame.Rect(-15, 60, 80, 135)

    # Draw side bar  with shadow, color, and outline
    pygame.draw.rect(screen, GRAY, side_bar.move(5, 5), border_radius=15)
    pygame.draw.rect(screen, DARKGREEN, side_bar.inflate(5,5), border_radius=17)
    pygame.draw.rect(screen, GREEN, side_bar, border_radius=15)

    # Draw home button with color and outline
    pygame.draw.rect(screen, RED, home_button, border_radius=15)
    pygame.draw.rect(screen, DARKRED, home_button.inflate(6, 6), 3, border_radius=18)  # Outline

    # Draw timer button with color and outline
    pygame.draw.rect(screen, BLUE, timer_button, border_radius=15)
    pygame.draw.rect(screen, DARKBLUE, timer_button.inflate(6, 6), 3, border_radius=18)  # Outline

    # Load and position icons on buttons
    timer_UI = pygame.image.load('UI/timer.PNG')
    timer_UI = pygame.transform.scale(timer_UI, (45, 45))
    screen.blit(timer_UI, (timer_button.centerx - 23, timer_button.centery - 23))  # Center the image

    home_UI = pygame.image.load('UI/home.PNG')
    home_UI = pygame.transform.scale(home_UI, (40, 40))
    screen.blit(home_UI, (home_button.centerx - 20, home_button.centery - 20))  # Center the image

    # Large circle in center
    pygame.draw.circle(screen, BLACK, (400, 260), 200, 3)


# Timer screen display function
def display_timer_screen():
    global image_button, home_button

    screen.fill(WHITE)
    display_title("Timer", BLUE, DARKBLUE)

    button_width, button_height = 50, 50
    home_button = pygame.Rect(5, 70, button_width, button_height)  # Home button
    image_button = pygame.Rect(5, 135, button_width, button_height)  # Image Selection button
    side_bar = pygame.Rect(-15, 60, 80, 135)

    # Draw sidebar with shadow, color, and outline
    pygame.draw.rect(screen, GRAY, side_bar.move(5, 5), border_radius=15)
    pygame.draw.rect(screen, DARKBLUE, side_bar.inflate(5, 5), border_radius=17)
    pygame.draw.rect(screen, BLUE, side_bar, border_radius=15)

    # Draw home button with color and outline
    pygame.draw.rect(screen, RED, home_button, border_radius=15)
    pygame.draw.rect(screen, DARKRED, home_button.inflate(6, 6), 3, border_radius=18)  # Outline

    # Draw image selection button with color and outline
    pygame.draw.rect(screen, GREEN, image_button, border_radius=15)
    pygame.draw.rect(screen, DARKGREEN, image_button.inflate(6, 6), 3, border_radius=18)  # Outline

    # Load and position icons on buttons
    home_UI = pygame.image.load('UI/home.PNG')
    home_UI = pygame.transform.scale(home_UI, (40, 40))
    screen.blit(home_UI, (home_button.centerx - 20, home_button.centery - 20))  # Center the image

    image_UI = pygame.image.load('UI/camera.PNG')
    image_UI = pygame.transform.scale(image_UI, (45, 45))
    screen.blit(image_UI,(image_button.centerx - 23, image_button.centery - 23))  # Center the image

    # Filled circle with outline
    pygame.draw.circle(screen, BLUE, (400, 260), 200)
    circle_border = pygame.draw.circle(screen, BLACK, (400, 260), 200, 3)
    timer_image = pygame.image.load('Image/blinka.JPG')
    screen.blit(timer_image, (400 - (timer_image.get_width() / 2), 260 - (timer_image.get_height() / 2)))

    # Add twelve spokes
    center_x, center_y = 400, 260
    radius = 200
    for i in range(24):
        angle = math.radians(i * 15)  # 360 degrees divided by 24 = 15 degrees per spoke
        end_x = center_x + radius * math.cos(angle)
        end_y = center_y + radius * math.sin(angle)
        pygame.draw.line(screen, BLACK, (center_x, center_y), (end_x, end_y), 3)

    # Display text
    font = pygame.font.Font(None, 36)
    timer_minutes = 5  # Example value
    text = font.render(f" {timer_minutes} minutes", True, BLACK)
    screen.blit(text, (640, 250))


# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # Detect mouse click
            mouse_x, mouse_y = event.pos
            if current_state == HOME:
                if image_button.collidepoint(mouse_x, mouse_y):  # Click on Image Selection button
                    current_state = IMAGE_SELECTION
                elif timer_button.collidepoint(mouse_x, mouse_y):  # Click on Timer button
                    current_state = TIMER
            elif current_state == IMAGE_SELECTION:
                if home_button.collidepoint(mouse_x, mouse_y):  # Click on Home button
                    current_state = HOME
                elif timer_button.collidepoint(mouse_x, mouse_y):  # Click on Timer button
                    current_state = TIMER
            elif current_state == TIMER:
                if home_button.collidepoint(mouse_x, mouse_y):  # Click on Home button
                    current_state = HOME
                elif image_button.collidepoint(mouse_x, mouse_y):  # Click on Image Selection button
                    current_state = IMAGE_SELECTION

    # Display the current screen based on state
    if current_state == HOME:
        display_home_screen()
    elif current_state == IMAGE_SELECTION:
        display_image_selection_screen()
    elif current_state == TIMER:
        display_timer_screen()

    pygame.display.update()
    clock.tick(60)
