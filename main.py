import pygame
import random
import os


pygame.init()
WIDTH, HEIGHT = 600, 600 
GRID_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(" Spaced Maze Snake ")
clock = pygame.time.Clock()


BLACK, GREEN, RED, BLUE, WHITE = (0,0,0), (0,255,0), (255,0,0), (0,0,255), (255,255,255)


def create_spaced_wall(x, y, length, horizontal=True, gap=3):
    """Creates a wall with gaps for strategic navigation."""
    wall = []
    for i in range(length):
        if i % gap != 0: 
            if horizontal:
                wall.append((x + i, y))
            else:
                wall.append((x, y + i))
    return wall


L1 = create_spaced_wall(5, 5, 20, True, 3) + create_spaced_wall(5, 24, 20, True, 3)
L2 = create_spaced_wall(10, 5, 20, False, 4) + create_spaced_wall(20, 5, 20, False, 4)
L3 = create_spaced_wall(5, 10, 20, True, 2) + create_spaced_wall(5, 20, 20, True, 2)
L4 = create_spaced_wall(5, 5, 20, True, 3) + create_spaced_wall(5, 5, 20, False, 3) + \
     create_spaced_wall(25, 5, 20, False, 3) + create_spaced_wall(5, 25, 21, True, 3)

levels = [L1, L2, L3, L4]

def main():
    snake = [(15, 15), (15, 16), (15, 17)] 
    direction = (0, -1)
    score = 0
    current_maze = levels[0]
    
    def get_food():
        while True:
            f = (random.randint(1, 28), random.randint(1, 28))
         
            if f not in snake and f not in current_maze: return f 
    


    food = get_food()
    running = True
    


    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if event.type == pygame.KEYDOWN: # Keyboard input handling [cite: 48, 50]
                if event.key == pygame.K_UP and direction != (0, 1): direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1): direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0): direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0): direction = (1, 0)



        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])




        if score < 5: current_maze = levels[0]
        elif score < 10: current_maze = levels[1]
        elif score < 15: current_maze = levels[2]
        else: current_maze = levels[3]
        
        
        if (new_head[0] < 0 or new_head[0] >= 30 or new_head[1] < 0 or new_head[1] >= 30 or 
            new_head in snake or new_head in current_maze):
            running = False

        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            food = get_food() 
        else: snake.pop()

   
        for wall in current_maze:
            pygame.draw.rect(screen, BLUE, (wall[0]*20, wall[1]*20, 20, 20))

        for seg in snake:
            pygame.draw.rect(screen, GREEN, (seg[0]*20, seg[1]*20, 20, 20))
            
        pygame.draw.rect(screen, RED, (food[0]*20, food[1]*20, 20, 20))



        font = pygame.font.SysFont("Arial", 18)
        info = font.render(f"Score: {score} | Level: {(score // 5) + 1}", True, WHITE)
        screen.blit(info, (15, 15))
        pygame.display.flip()
        clock.tick(10)
    pygame.quit()

if __name__ == "__main__": main()