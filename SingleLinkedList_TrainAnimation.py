import pygame
import time

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Single Linked List Animation")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def display(self):
        nodes = []
        current = self.head
        x, y = 50, HEIGHT // 2
        while current:
            nodes.append((current.data, x, y))
            x += 150
            current = current.next
        return nodes

# Inisialisasi Linked List
llist = LinkedList()
data_list = [1, 2, 3, 4]
for data in data_list:
    llist.append(data)
    screen.fill((255, 255, 255))  # Background putih
    
    # Gambar node dan koneksi
    nodes = llist.display()
    for i, (data, x, y) in enumerate(nodes):
        # Gambar node (kotak)
        pygame.draw.rect(screen, (50, 150, 255), (x, y-25, 100, 50))
        font = pygame.font.Font(None, 36)
        text = font.render(str(data), True, (255, 255, 255))
        screen.blit(text, (x + 40, y - 15))
        
        # Gambar panah ke node berikutnya
        if i < len(nodes) - 1:
            pygame.draw.line(screen, (0, 0, 0), (x + 100, y), (x + 150, y), 3)
            pygame.draw.polygon(screen, (0, 0, 0), [(x + 145, y-5), (x + 150, y), (x + 145, y+5)])
    
    pygame.display.flip()
    time.sleep(1)  # Delay untuk animasi

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()