import pygame
import time

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Double Linked List Animation")

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
        new_node.prev = current

    def display(self):
        nodes = []
        current = self.head
        x, y = 50, HEIGHT // 2
        while current:
            nodes.append((current.data, x, y))
            x += 150
            current = current.next
        return nodes

# Inisialisasi Doubly Linked List
dllist = DoublyLinkedList()
data_list = [1, 2, 3, 4]
for data in data_list:
    dllist.append(data)
    screen.fill((255, 255, 255))
    
    # Gambar node dan koneksi dua arah
    nodes = dllist.display()
    for i, (data, x, y) in enumerate(nodes):
        pygame.draw.rect(screen, (255, 150, 50), (x, y-25, 100, 50))
        font = pygame.font.Font(None, 36)
        text = font.render(str(data), True, (255, 255, 255))
        screen.blit(text, (x + 40, y - 15))
        
        # Panah dua arah
        if i < len(nodes) - 1:
            pygame.draw.line(screen, (0, 0, 0), (x + 100, y), (x + 150, y), 3)  # Next
            pygame.draw.line(screen, (0, 0, 0), (x + 150, y-10), (x + 100, y-10), 3)  # Prev
            pygame.draw.polygon(screen, (0, 0, 0), [(x + 145, y-5), (x + 150, y), (x + 145, y+5)])  # Next arrow
            pygame.draw.polygon(screen, (0, 0, 0), [(x + 105, y-15), (x + 100, y-10), (x + 105, y-5)])  # Prev arrow
    
    pygame.display.flip()
    time.sleep(1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()