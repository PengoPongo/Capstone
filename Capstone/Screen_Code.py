import pygame
import math
import os
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 480),pygame.NOFRAME)  # Setting screen size
clock = pygame.time.Clock()  # Sets up clock in project

# Define colors
WHITE = pygame.Color('antiquewhite')
BLACK = pygame.Color('grey14')
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
last_update_time = pygame.time.get_ticks()  # Record initial time
timer_running = False
timer_seconds = 0
time_set = 60    # default time for clock
timer_minutes = time_set
finish = True

# Load image filenames from the "Image" folder
image_folder = "Image"      # file path to images
image_files = []            # array to store image names
current_image_index = 0

# Get all files in the "Image" folder and filter for image files (e.g., .png, .jpg)
for filename in os.listdir(image_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
        image_files.append(filename)

# Function to create a circular mask for the image
def crop_image_to_circle(image, radius):
    # Create a surface with an alpha channel (RGBA) to allow transparency
    circle_surface = pygame.Surface((radius * 2, radius * 2), pygame.SRCALPHA)

    # Create a circular mask (White circle on a transparent background)
    pygame.draw.circle(circle_surface, (255, 255, 255), (radius, radius), radius)

    # Copy the image onto the circle surface using the mask
    image_rect = image.get_rect(center=(radius, radius))
    circle_surface.blit(image, image_rect, special_flags=pygame.BLEND_RGBA_MIN)  # Use blending to apply the mask

    return circle_surface

# Function to display a title bar with shadow
def display_title(title, color, border):
    pygame.draw.rect(screen, GRAY, (5, 0, 797, 45), border_radius=10)  # Shadow
    pygame.draw.rect(screen, border, (-1, -10, 801, 53), border_radius=10)
    pygame.draw.rect(screen, color, (0, -10, 800, 50), border_radius=10)  # Rounded title bar
    font = pygame.font.Font(None, 40)
    text = font.render(title, True, border)
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
    timer_UI = pygame.transform.smoothscale(timer_UI, (150, 150))
    screen.blit(timer_UI, (timer_button.centerx - 75, timer_button.centery - 75))  # Center the image

    camera_UI = pygame.image.load('UI/camera.PNG')
    camera_UI = pygame.transform.smoothscale(camera_UI, (150, 150))
    screen.blit(camera_UI, (image_button.centerx - 75, image_button.centery - 75))  # Center the image

    # Add text under each button
    font = pygame.font.Font(None, 24)
    text1 = font.render("Image Selection", True, DARKGREEN)
    text2 = font.render("Timer Countdown", True, DARKBLUE)
    screen.blit(text1, (image_button.centerx - text1.get_width() // 2, image_button.bottom - 20))
    screen.blit(text2, (timer_button.centerx - text2.get_width() // 2, timer_button.bottom - 20))


# Image selection screen display function
def display_image_selection_screen():
    global home_button, timer_button, current_image_index, left_rect, right_rect
    screen.fill(WHITE)
    display_title("Image Selection", GREEN, DARKGREEN)

    button_width, button_height = 50, 50
    home_button = pygame.Rect(5, 70, button_width, button_height)  # Home button
    timer_button = pygame.Rect(5, 135, button_width, button_height)  # Timer button
    side_bar = pygame.Rect(-15, 60, 80, 135)

    # Draw side bar with shadow, color, and outline
    pygame.draw.rect(screen, GRAY, side_bar.move(5, 5), border_radius=15)
    pygame.draw.rect(screen, DARKGREEN, side_bar.inflate(5, 5), border_radius=17)
    pygame.draw.rect(screen, GREEN, side_bar, border_radius=15)

    # Draw home button with color and outline
    pygame.draw.rect(screen, RED, home_button, border_radius=15)
    pygame.draw.rect(screen, DARKRED, home_button.inflate(6, 6), 3, border_radius=18)  # Outline

    # Draw timer button with color and outline
    pygame.draw.rect(screen, BLUE, timer_button, border_radius=15)
    pygame.draw.rect(screen, DARKBLUE, timer_button.inflate(6, 6), 3, border_radius=18)  # Outline

    # Load and position icons on buttons
    timer_UI = pygame.image.load('UI/timer.png')
    timer_UI = pygame.transform.smoothscale(timer_UI, (45, 45))
    screen.blit(timer_UI, (timer_button.centerx - 23, timer_button.centery - 23))  # Center the image

    home_UI = pygame.image.load('UI/home.png')
    home_UI = pygame.transform.smoothscale(home_UI, (40, 40))
    screen.blit(home_UI, (home_button.centerx - 20, home_button.centery - 20))  # Center the image

    left_UI = pygame.image.load('UI/left.png')
    left_UI = pygame.transform.smoothscale(left_UI, (75, 75))
    left_rect = screen.blit(left_UI, (100, 223))

    right_UI = pygame.image.load('UI/right.png')
    right_UI = pygame.transform.smoothscale(right_UI, (75, 75))
    right_rect = screen.blit(right_UI, (620, 225))

    pygame.draw.circle(screen, GRAY, (403, 263), 200, 5)

    # Display the current image in the center of the circle (if available)
    if image_files:
        current_image_path = os.path.join(image_folder, image_files[current_image_index])  # Get path of current image
        try:
            # Load the image
            image = pygame.image.load(current_image_path)
            # Crop the image to a circle
            circular_image = crop_image_to_circle(image, 200)
            # Draw the circular image in the center of the circle
            screen.blit(circular_image, (400 - circular_image.get_width() // 2, 260 - circular_image.get_height() // 2))
        except Exception as e:
            print(f"Error loading image {current_image_path}: {e}")

    # Display "Preview of [current image]" text under the circle
    font = pygame.font.Font(None, 24)
    if image_files:
        preview_text = f"Preview of {image_files[current_image_index]}"
    else:
        preview_text = "No images available"
    text = font.render(preview_text, True, DARKGREEN)
    screen.blit(text, (400 - text.get_width() // 2, 463))  # Center the text under the circle

    # Filled circle with outline
    circle_border = pygame.draw.circle(screen, DARKGREEN, (400, 260), 200, 5)

    # Add twelve spokes (for visual decoration)
    center_x, center_y = 400, 260
    radius = 195
    even_spoke_length = 25
    odd_spoke_length = 15

    for i in range(24):
        angle = math.radians(i * 15)  # 360 degrees divided by 24 = 15 degrees per spoke

        # Determine if it's an odd or even spoke to choose length
        if i % 2 == 0:  # Even spokes
            spoke_length = even_spoke_length
        else:  # Odd spokes
            spoke_length = odd_spoke_length

        start_x = center_x + radius * math.cos(angle)
        start_y = center_y + radius * math.sin(angle)
        end_x = center_x + (radius - spoke_length) * math.cos(angle)
        end_y = center_y + (radius - spoke_length) * math.sin(angle)

        # Draw the line (spoke) from the edge of the circle towards the center
        pygame.draw.line(screen, DARKGREEN, (start_x, start_y), (end_x, end_y), 3)


# Updated Timer screen display function
def display_timer_screen():
    global image_button, home_button, plus_button, minus_button, play_button, stop_button, reset_button
    global timer_minutes, timer_seconds, timer_running, time_set, finish, last_update_time

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
    home_UI = pygame.image.load('UI/home.png')
    home_UI = pygame.transform.smoothscale(home_UI, (40, 40))
    screen.blit(home_UI, (home_button.centerx - 20, home_button.centery - 20))  # Center the image

    image_UI = pygame.image.load('UI/camera.png')
    image_UI = pygame.transform.smoothscale(image_UI, (45, 45))
    screen.blit(image_UI, (image_button.centerx - 23, image_button.centery - 23))  # Center the image

    #sets up the code for the plus and minus buttons
    plus_button = pygame.Rect(680, 185, 45, 45)  # Plus button
    minus_button = pygame.Rect(680, 295, 45, 45)  # Minus button

    plus_UI = pygame.image.load('UI/plus.png')
    plus_UI = pygame.transform.smoothscale(plus_UI, (45, 45))
    screen.blit(plus_UI, plus_button.topleft)  # Use rect to position

    minus_UI = pygame.image.load('UI/minus.png')
    minus_UI = pygame.transform.smoothscale(minus_UI, (45, 45))
    screen.blit(minus_UI, minus_button.topleft)  # Use rect to position

    #sets up the play, stop, reset buttons
    play_button = pygame.Rect(110, 145, 45, 45)  # play button
    stop_button = pygame.Rect(110, 235, 45, 45)  # stop button
    reset_button = pygame.Rect(110, 325, 45, 45)  # reset button

    font = pygame.font.Font(None, 30)
    play_text = font.render('Play', True, DARKBLUE)
    screen.blit(play_text, (115, 125))  # Center the text under the circle
    play_UI = pygame.image.load('UI/play.png')
    play_UI = pygame.transform.smoothscale(play_UI, (50, 50))
    screen.blit(play_UI, play_button.topleft)  # Use rect to position

    play_text = font.render('Stop', True, DARKBLUE)
    screen.blit(play_text, (114, 215))  # Center the text under the circle
    stop_UI = pygame.image.load('UI/stop.png')
    stop_UI = pygame.transform.smoothscale(stop_UI, (50, 50))
    screen.blit(stop_UI, stop_button.topleft)  # Use rect to position

    play_text = font.render('Reset', True, DARKBLUE)
    screen.blit(play_text, (107, 305))  # Center the text under the circle
    reset_UI = pygame.image.load('UI/reset.png')
    reset_UI = pygame.transform.smoothscale(reset_UI, (50, 50))
    screen.blit(reset_UI, reset_button.topleft)  # Use rect to position

    # Countdown logic
    if timer_running:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - last_update_time

        if elapsed_time >= 1000:  # 1000 milliseconds = 1 second
            last_update_time = current_time
            if timer_seconds > 0:
                timer_seconds -= 1
            elif timer_minutes > 0:
                timer_minutes -= 1
                timer_seconds = 59
            else:
                timer_running = False  # Stop timer when it reaches zero
                finish = True
                # add beeping code here

    # Display timer
    time_text = font.render(f"{timer_minutes:02}:{timer_seconds:02}", True, DARKBLUE)
    screen.blit(time_text, (375, 462))

    pygame.draw.circle(screen, GRAY, (403, 263), 200, 5)

    # Display the current image in the center of the circle (if available)
    if image_files:
        current_image_path = os.path.join(image_folder, image_files[current_image_index])  # Get path of current image
        try:
            # Load the image
            image = pygame.image.load(current_image_path)
            # Crop the image to a circle
            circular_image = crop_image_to_circle(image, 200)
            # Draw the circular image in the center of the circle
            screen.blit(circular_image, (400 - circular_image.get_width() // 2, 260 - circular_image.get_height() // 2))
        except Exception as e:
            print(f"Error loading image {current_image_path}: {e}")


    # Filled circle with outline
    circle_border = pygame.draw.circle(screen, DARKBLUE, (400, 260), 200, 5)

    # Add twelve spokes (for visual decoration)
    center_x, center_y = 400, 260
    radius = 195
    even_spoke_length = 25
    odd_spoke_length = 15

    for i in range(24):
        angle = math.radians(i * 15)  # 360 degrees divided by 24 = 15 degrees per spoke

        # Determine if it's an odd or even spoke to choose length
        if i % 2 == 0:  # Even spokes
            spoke_length = even_spoke_length
        else:  # Odd spokes
            spoke_length = odd_spoke_length

        start_x = center_x + radius * math.cos(angle)
        start_y = center_y + radius * math.sin(angle)
        end_x = center_x + (radius - spoke_length) * math.cos(angle)
        end_y = center_y + (radius - spoke_length) * math.sin(angle)

        # Draw the line (spoke) from the edge of the circle towards the center
        pygame.draw.line(screen, DARKBLUE, (start_x, start_y), (end_x, end_y), 3)

    # Display the timer text
    font = pygame.font.Font(None, 36)
    text = font.render(f"{time_set} minutes", True, DARKBLUE)
    screen.blit(text, (640, 250))


# Main loop
while True:
    font = pygame.font.Font(None, 36)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:  # Escape key pressed
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
                elif left_rect.collidepoint(event.pos):  # Check if left button was clicked
                    # Move to previous image, wrap around if at the start
                    current_image_index = (current_image_index - 1) % len(image_files)
                elif right_rect.collidepoint(event.pos):  # Check if right button was clicked
                    # Move to next image, wrap around if at the end
                    current_image_index = (current_image_index + 1) % len(image_files)
            elif current_state == TIMER:
                if home_button.collidepoint(mouse_x, mouse_y):  # Click on Home button
                    current_state = HOME
                elif image_button.collidepoint(mouse_x, mouse_y):  # Click on Image Selection button
                    current_state = IMAGE_SELECTION
                elif play_button.collidepoint(mouse_x, mouse_y):    # Click on play button
                    timer_running = True
                    finish = False
                elif stop_button.collidepoint(mouse_x, mouse_y) and timer_running == True:    # Click on stop button
                    timer_running = False
                elif reset_button.collidepoint(mouse_x, mouse_y):
                    timer_running = False
                    finish = True
                    timer_minutes = time_set
                    timer_seconds = 0
                elif plus_button.collidepoint(mouse_x, mouse_y) and finish == True:  # Click on Plus button
                    if time_set < 60:
                        time_set += 5
                        timer_minutes = time_set
                elif minus_button.collidepoint(mouse_x, mouse_y) and finish == True:  # Click on Minus button
                    if time_set > 5:
                        time_set -= 5
                        timer_minutes = time_set

    # Display the current screen based on state
    if current_state == HOME:
        display_home_screen()
    elif current_state == IMAGE_SELECTION:
        display_image_selection_screen()
    elif current_state == TIMER:
        display_timer_screen()

    pygame.display.update()
    clock.tick(60)
