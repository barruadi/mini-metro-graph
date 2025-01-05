import pygame
from aksi.station import add_station, node_positions, graph

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)


pygame.init()
screen = pygame.display.set_mode((800, 600))

def draw_graph():
    screen.fill((0, 0, 0)) 
    
    for node, pos in node_positions.items():
        pygame.draw.circle(screen, BLUE, pos, 10)
        font = pygame.font.Font(None, 24)
        text = font.render(str(node), True, WHITE)
        screen.blit(text, (pos[0], pos[1]))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: 
                print("Klik kiri")
                add_station(event.pos)
                print(node_positions)
    draw_graph()
    pygame.display.flip()