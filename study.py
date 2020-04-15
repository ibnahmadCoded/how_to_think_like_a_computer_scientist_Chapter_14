import pygame
import time

def main():
    """Set up the game and run the main loop """
    pygame.init()   #Prepare the pygame module for use

    #Create surface of (width, height), and its window.
    main_surface = pygame.display.set_mode((480, 240))

    #set up the ball image to use in game loop
    ball = pygame.image.load("ball.png")

    # Instantiate 16 point Courier font to draw text.
    my_font = pygame.font.SysFont("Courier", 16)

    frame_count = 0
    frame_rate = 0
    t0 = time.time()


    while True:
        ev = pygame.event.poll()     #Look for any event
        if ev.type == pygame.QUIT:   #Window close butoon clicked?
            break                       #...leave game loop

        # Do other bits of logic for the game here
        frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.time()
            frame_rate = 500 / (t1 - t0)
            t0 = t1

        # Completely redraw the surface, starting with background
        main_surface.fill((0, 200, 255))

        # Put a red rectangle somewhere on the surface
        main_surface.fill((255,0,0), (300, 100, 150, 90))

        #display image in position(100, 200)
        main_surface.blit(ball, (100, 120))

        # Make a new surface with an image of the text
        the_text = my_font.render("Frame = {0}, rate = {1:.2f} fps"
                                  .format(frame_count, frame_rate), True, (0,0,0))
        # Copy the text surface to the main surface
        main_surface.blit(the_text, (10, 10))

        # Now that everything is drawn, put it on display!
        pygame.display.flip()

    pygame.quit() # Once we leave the loop, close the window.

main()
