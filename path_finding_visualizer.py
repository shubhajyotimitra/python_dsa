import pygame
import heapq
import random
from collections import deque

# Initialize pygame
pygame.init()

# Screen settings
WIDTH = 600
ROWS = 30
WIN = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Pathfinding Visualizer 🚀")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (200, 200, 200)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165 ,0)
PURPLE = (128, 0, 128)
YELLOW = (255, 255, 0)

# Node class
class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.color = WHITE
        self.neighbors = []
        self.width = width
        self.total_rows = total_rows
        self.weight = 1

    def get_pos(self):
        return self.row, self.col

    def is_closed(self): return self.color == RED
    def is_open(self): return self.color == GREEN
    def is_barrier(self): return self.color == BLACK
    def is_start(self): return self.color == ORANGE
    def is_end(self): return self.color == PURPLE
    def is_weighted(self): return self.color == YELLOW

    def reset(self): self.color = WHITE; self.weight = 1
    def make_start(self): self.color = ORANGE
    def make_closed(self): self.color = RED
    def make_open(self): self.color = GREEN
    def make_barrier(self): self.color = BLACK
    def make_end(self): self.color = PURPLE
    def make_path(self): self.color = BLUE
    def make_weighted(self): self.color = YELLOW; self.weight = 5

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def update_neighbors(self, grid, allow_diagonal=False):
        self.neighbors = []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        if allow_diagonal:
            directions += [(1,1), (1,-1), (-1,1), (-1,-1)]
        for dr, dc in directions:
            r, c = self.row + dr, self.col + dc
            if 0 <= r < self.total_rows and 0 <= c < self.total_rows:
                if not grid[r][c].is_barrier():
                    self.neighbors.append(grid[r][c])

# Heuristic for A*
def h(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Reconstruct path
def reconstruct_path(came_from, current, draw):
    while current in came_from:
        current = came_from[current]
        current.make_path()
        draw()

# BFS
def bfs(draw, grid, start, end):
    queue = deque([start])
    came_from = {}
    visited = {start}
    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
        current = queue.popleft()
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end(); start.make_start()
            return True
        for neighbor in current.neighbors:
            if neighbor not in visited:
                came_from[neighbor] = current
                visited.add(neighbor)
                queue.append(neighbor)
                neighbor.make_open()
        draw()
        if current != start: current.make_closed()
    return False

# DFS
def dfs(draw, grid, start, end):
    stack = [start]
    came_from = {}
    visited = {start}
    while stack:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
        current = stack.pop()
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end(); start.make_start()
            return True
        for neighbor in current.neighbors:
            if neighbor not in visited:
                came_from[neighbor] = current
                visited.add(neighbor)
                stack.append(neighbor)
                neighbor.make_open()
        draw()
        if current != start: current.make_closed()
    return False

# Dijkstra
def dijkstra(draw, grid, start, end):
    dist = {node: float("inf") for row in grid for node in row}
    dist[start] = 0
    pq = [(0, start)]
    came_from = {}
    while pq:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
        current_dist, current = heapq.heappop(pq)
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end(); start.make_start()
            return True
        for neighbor in current.neighbors:
            new_dist = current_dist + neighbor.weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                came_from[neighbor] = current
                heapq.heappush(pq, (new_dist, neighbor))
                neighbor.make_open()
        draw()
        if current != start: current.make_closed()
    return False

# A* Algorithm
def astar(draw, grid, start, end):
    count = 0
    open_set = [(0, count, start)]
    came_from = {}
    g_score = {node: float("inf") for row in grid for node in row}
    f_score = {node: float("inf") for row in grid for node in row}
    g_score[start] = 0; f_score[start] = h(start.get_pos(), end.get_pos())
    open_set_hash = {start}
    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit()
        current = heapq.heappop(open_set)[2]
        open_set_hash.remove(current)
        if current == end:
            reconstruct_path(came_from, end, draw)
            end.make_end(); start.make_start()
            return True
        for neighbor in current.neighbors:
            temp_g = g_score[current] + neighbor.weight
            if temp_g < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g
                f_score[neighbor] = temp_g + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    heapq.heappush(open_set, (f_score[neighbor], count, neighbor))
                    open_set_hash.add(neighbor)
                    neighbor.make_open()
        draw()
        if current != start: current.make_closed()
    return False

# Random Maze Generator
def generate_maze(grid, rows, cols):
    for row in grid:
        for node in row:
            node.make_barrier()

    directions = [(2,0), (-2,0), (0,2), (0,-2)]

    def in_bounds(r, c):
        return 0 <= r < rows and 0 <= c < cols

    def carve_passages(r, c):
        random.shuffle(directions)
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if in_bounds(nr, nc) and grid[nr][nc].color == BLACK:
                wall_r, wall_c = r + dr//2, c + dc//2
                grid[nr][nc].reset()
                grid[wall_r][wall_c].reset()
                carve_passages(nr, nc)

    start_r, start_c = random.randrange(0, rows, 2), random.randrange(0, cols, 2)
    grid[start_r][start_c].reset()
    carve_passages(start_r, start_c)

# Utilities
def make_grid(rows, width):
    gap = width // rows
    return [[Node(i, j, gap, rows) for j in range(rows)] for i in range(rows)]

def draw(win, grid, rows, width):
    win.fill(WHITE)
    for row in grid:
        for node in row:
            node.draw(win)
    gap = width // rows
    for i in range(rows):
        pygame.draw.line(win, GREY, (0, i*gap), (width, i*gap))
        pygame.draw.line(win, GREY, (i*gap, 0), (i*gap, width))
    pygame.display.update()

def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos
    return y // gap, x // gap

# Main
def main(win, width):
    grid = make_grid(ROWS, width)
    start, end = None, None
    run, allow_diagonal = True, False
    while run:
        draw(win, grid, ROWS, width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if pygame.mouse.get_pressed()[0]: # Left click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]
                if not start and node != end:
                    start = node; start.make_start()
                elif not end and node != start:
                    end = node; end.make_end()
                elif node != end and node != start:
                    node.make_barrier()
            elif pygame.mouse.get_pressed()[2]: # Right click
                pos = pygame.mouse.get_pos()
                row, col = get_clicked_pos(pos, ROWS, width)
                node = grid[row][col]; node.reset()
                if node == start: start = None
                elif node == end: end = None
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    allow_diagonal = not allow_diagonal
                    for row in grid:
                        for node in row: node.update_neighbors(grid, allow_diagonal)
                if event.key == pygame.K_w:
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_pos(pos, ROWS, width)
                    grid[row][col].make_weighted()
                if event.key == pygame.K_b and start and end:
                    for row in grid:
                        for node in row: node.update_neighbors(grid, allow_diagonal)
                    bfs(lambda: draw(win, grid, ROWS, width), grid, start, end)
                if event.key == pygame.K_f and start and end:
                    for row in grid:
                        for node in row: node.update_neighbors(grid, allow_diagonal)
                    dfs(lambda: draw(win, grid, ROWS, width), grid, start, end)
                if event.key == pygame.K_j and start and end:
                    for row in grid:
                        for node in row: node.update_neighbors(grid, allow_diagonal)
                    dijkstra(lambda: draw(win, grid, ROWS, width), grid, start, end)
                if event.key == pygame.K_a and start and end:
                    for row in grid:
                        for node in row: node.update_neighbors(grid, allow_diagonal)
                    astar(lambda: draw(win, grid, ROWS, width), grid, start, end)
                if event.key == pygame.K_m:  # Random Maze
                    start, end = None, None
                    generate_maze(grid, ROWS, ROWS)
                if event.key == pygame.K_c:
                    start, end = None, None
                    grid = make_grid(ROWS, width)
    pygame.quit()

main(WIN, WIDTH)
