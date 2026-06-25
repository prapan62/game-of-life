import pygame
import numpy as np
import sys

# --- Constants ---
CELL_SIZE = 12
GRID_W, GRID_H = 80, 60
WIN_W = GRID_W * CELL_SIZE
WIN_H = GRID_H * CELL_SIZE + 60  # extra bar for controls

FPS_OPTIONS = [5, 10, 20, 40]

# Palette
BG        = (10,  10,  18)
CELL_COL  = (80, 220, 160)
GRID_COL  = (25,  25,  40)
UI_BG     = (18,  18,  30)
BTN_COL   = (45,  45,  70)
BTN_HOV   = (70,  70, 110)
BTN_ACT   = (80, 220, 160)
TEXT_COL  = (200, 200, 220)
TEXT_ACT  = (10,  10,  18)
ACCENT    = (80, 220, 160)

pygame.init()
screen = pygame.display.set_mode((WIN_W, WIN_H))
pygame.display.set_caption("Conway's Game of Life")
clock = pygame.time.Clock()
font_sm = pygame.font.SysFont("monospace", 13, bold=True)
font_md = pygame.font.SysFont("monospace", 15, bold=True)


def empty_grid():
    return np.zeros((GRID_H, GRID_W), dtype=np.uint8)


def random_grid(density=0.3):
    return (np.random.rand(GRID_H, GRID_W) < density).astype(np.uint8)


def step(grid):
    # Count neighbours with wrap-around (toroidal)
    n = (
        np.roll(np.roll(grid, -1, 0), -1, 1) +
        np.roll(grid, -1, 0) +
        np.roll(np.roll(grid, -1, 0),  1, 1) +
        np.roll(grid,  1, 1) +
        np.roll(grid, -1, 1) +
        np.roll(np.roll(grid,  1, 0), -1, 1) +
        np.roll(grid,  1, 0) +
        np.roll(np.roll(grid,  1, 0),  1, 1)
    )
    # Rules
    survive = ((grid == 1) & ((n == 2) | (n == 3)))
    born    = ((grid == 0) & (n == 3))
    return (survive | born).astype(np.uint8)


def draw_grid(surface, grid, show_lines):
    surface.fill(BG)
    # Cells
    for r in range(GRID_H):
        for c in range(GRID_W):
            if grid[r, c]:
                pygame.draw.rect(surface, CELL_COL,
                                 (c * CELL_SIZE + 1, r * CELL_SIZE + 1,
                                  CELL_SIZE - 1, CELL_SIZE - 1))
    # Grid lines
    if show_lines:
        for c in range(GRID_W + 1):
            pygame.draw.line(surface, GRID_COL,
                             (c * CELL_SIZE, 0), (c * CELL_SIZE, GRID_H * CELL_SIZE))
        for r in range(GRID_H + 1):
            pygame.draw.line(surface, GRID_COL,
                             (0, r * CELL_SIZE), (WIN_W, r * CELL_SIZE))


class Button:
    def __init__(self, x, y, w, h, label):
        self.rect = pygame.Rect(x, y, w, h)
        self.label = label
        self.active = False
        self.hovered = False

    def draw(self, surface):
        col = BTN_ACT if self.active else (BTN_HOV if self.hovered else BTN_COL)
        pygame.draw.rect(surface, col, self.rect, border_radius=5)
        tc = TEXT_ACT if self.active else TEXT_COL
        txt = font_sm.render(self.label, True, tc)
        surface.blit(txt, txt.get_rect(center=self.rect.center))

    def check(self, pos):
        self.hovered = self.rect.collidepoint(pos)
        return self.hovered

    def clicked(self, pos):
        return self.rect.collidepoint(pos)


def main():
    grid = random_grid()
    running = False
    show_lines = True
    fps_idx = 1
    generation = 0
    drawing = None   # True=paint, False=erase

    bar_y = GRID_H * CELL_SIZE
    bh = 36
    by = bar_y + 12

    btn_play  = Button(10,  by, 80, bh, "PLAY")
    btn_step  = Button(100, by, 80, bh, "STEP")
    btn_clear = Button(190, by, 80, bh, "CLEAR")
    btn_rand  = Button(280, by, 80, bh, "RANDOM")
    btn_grid  = Button(370, by, 80, bh, "GRID: ON")
    btn_fps   = Button(460, by, 100, bh, f"FPS: {FPS_OPTIONS[fps_idx]}")

    buttons = [btn_play, btn_step, btn_clear, btn_rand, btn_grid, btn_fps]
    btn_play.active = False

    while True:
        mx, my = pygame.mouse.get_pos()
        for b in buttons:
            b.check((mx, my))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    running = not running
                    btn_play.active = running
                    btn_play.label = "PAUSE" if running else "PLAY"
                elif event.key == pygame.K_c:
                    grid = empty_grid(); generation = 0; running = False
                    btn_play.active = False; btn_play.label = "PLAY"
                elif event.key == pygame.K_r:
                    grid = random_grid(); generation = 0
                elif event.key == pygame.K_RIGHT and not running:
                    grid = step(grid); generation += 1
                elif event.key == pygame.K_g:
                    show_lines = not show_lines
                    btn_grid.label = "GRID: ON" if show_lines else "GRID: OFF"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # Buttons
                    if btn_play.clicked((mx, my)):
                        running = not running
                        btn_play.active = running
                        btn_play.label = "PAUSE" if running else "PLAY"
                    elif btn_step.clicked((mx, my)):
                        grid = step(grid); generation += 1
                    elif btn_clear.clicked((mx, my)):
                        grid = empty_grid(); generation = 0
                        running = False; btn_play.active = False; btn_play.label = "PLAY"
                    elif btn_rand.clicked((mx, my)):
                        grid = random_grid(); generation = 0
                    elif btn_grid.clicked((mx, my)):
                        show_lines = not show_lines
                        btn_grid.label = "GRID: ON" if show_lines else "GRID: OFF"
                    elif btn_fps.clicked((mx, my)):
                        fps_idx = (fps_idx + 1) % len(FPS_OPTIONS)
                        btn_fps.label = f"FPS: {FPS_OPTIONS[fps_idx]}"
                    elif my < bar_y:
                        r, c = my // CELL_SIZE, mx // CELL_SIZE
                        if 0 <= r < GRID_H and 0 <= c < GRID_W:
                            drawing = not bool(grid[r, c])
                            grid[r, c] = 1 if drawing else 0

            if event.type == pygame.MOUSEBUTTONUP:
                drawing = None

            if event.type == pygame.MOUSEMOTION and drawing is not None:
                if my < bar_y:
                    r, c = my // CELL_SIZE, mx // CELL_SIZE
                    if 0 <= r < GRID_H and 0 <= c < GRID_W:
                        grid[r, c] = 1 if drawing else 0

        # Simulation step
        if running:
            grid = step(grid)
            generation += 1

        # --- Draw ---
        draw_grid(screen, grid, show_lines)

        # UI bar
        pygame.draw.rect(screen, UI_BG, (0, bar_y, WIN_W, 60))
        pygame.draw.line(screen, ACCENT, (0, bar_y), (WIN_W, bar_y), 1)

        for b in buttons:
            b.draw(screen)

        # Stats
        alive = int(grid.sum())
        info = f"Gen: {generation:>6}   Alive: {alive:>5}   [SPACE] play/pause  [→] step  [G] grid  [R] random  [C] clear"
        txt = font_sm.render(info, True, (100, 100, 130))
        screen.blit(txt, (WIN_W - txt.get_width() - 8, bar_y + 4))

        pygame.display.flip()
        clock.tick(FPS_OPTIONS[fps_idx] if running else 60)


if __name__ == "__main__":
    main()