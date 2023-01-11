import pygame
import math
import random

class Body:
    def __init__(self, x, y, vx, vy, mass, color):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.color = color
        self.radius = self.mass ** 0.5 # Scale radius based on mass
        self.ax = 0
        self.ay = 0
    
    def update_position(self, formula):
        if formula == 1:
            self.vx += self.ax * dt
            self.vy += self.ay * dt
            self.x += self.vx * dt
            self.y += self.vy * dt
            
        elif formula == 2:
            self.vx += self.ax * dt
            self.vy += self.ay * dt
            self.x += self.vx * dt
            self.y += self.vy * dt

    def update_force(self, bodies, formula):
        self.ax = 0.0
        self.ay = 0.0
        for other in bodies:
            if self != other:
                dx = other.x - self.x
                dy = other.y - self.y
                d = math.sqrt(dx**2 + dy**2)
                if d > self.radius*2 and d > 0: # Avoid divide by zero And large number of force when d is so small
                    if formula == 1:
                        a = G * other.mass / d**2
                        theta = math.atan2(dy,dx) # math.asin(dy/d)
                        self.ax += a * math.cos(theta)
                        self.ay += a * math.sin(theta)
                    elif formula == 2:
                        a = G * other.mass / d**2
                        self.ax += a * dx
                        self.ay += a * dy
                    
        self.update_position(formula)


def simulate(bodies, formula):
    running = True
    t0 = pygame.time.get_ticks()
    while running:
        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
        
        # Update forces and positions
        for body in bodies:
            body.update_force(bodies, formula)
        
        # Clear the screen
        screen.fill((255, 255, 255))
        
        # Draw the bodies
        for body in bodies:
            x, y = body.x, body.y
            mass = body.mass
            radius = body.radius 
            pygame.draw.circle(screen, body.color, (x, y), radius)
        
        # Calculate and display FPS
        t1 = pygame.time.get_ticks()
        elapsed_time = t1 - t0
        t0 = t1
        if elapsed_time > 0: # Avoid division by zero
            fps = 1000 / elapsed_time  # FPS = 1000 / elapsed time in milliseconds
        else:
            fps = 0
        font = pygame.font.Font(None, 36)
        text = font.render(f"FPS: {fps:.2f}", True, (0, 0, 0))
        screen.blit(text, (10, 10))
        
        # Show number of particles
        text = font.render(f"Particles: {count}", True, "white")
        screen.blit(text, (10,40))

        # Show G
        text = font.render(f"G: {G}", True, "white")
        screen.blit(text, (10,70))
        
        # Show dt
        text = font.render(f"dt: {dt}", True, "white")
        screen.blit(text, (10,100))
        
        # Show method
        text = font.render(f"Method: {method}", True, "white")
        screen.blit(text, (10,130))
        
        # Update the display
        pygame.display.flip()

G = 0.067
dt = 1
width, height = 800, 800
method = 1
random.seed(10)
# Initialize Pygame and create a window
pygame.init()
screen = pygame.display.set_mode((width, height))   


# Create a new body with random position and mass
count = 300
bodies = []
for i in range(count):
    x = random.randint(0, width)
    y = random.randint(0, height)
    #vx = random.randint(0,10)
    #vy = random.randint(0,10)
    #mass = random.randint(10, 80)
    new_body = Body(x, y,0,0, 30, "Black")

    # Add the new body to the list of bodies
    bodies.append(new_body)

# usage:
simulate(bodies, method)






        
