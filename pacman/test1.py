import pygame

pygame.init()

# 1. IZGARA VE EKRAN AYARLARI
CELL_SIZE = 30  # Her bir karenin genişliği ve yüksekliği (30x30 piksel)

# 15 satır, 20 sütunluk haritamız
# (1: Duvar, 0: Yem, 2: Boş Alan)
MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1, 2, 1, 1, 2, 1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

# Ekran Boyutu Haritaya Göre Otomatik Hesaplatılır:
# Sütun Sayısı * CELL_SIZE = 20 * 30 = 600
# Satır Sayısı * CELL_SIZE = 15 * 30 = 450
WIDTH = len(MAP[0]) * CELL_SIZE
HEIGHT = len(MAP) * CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pacman Grid Game")
clock = pygame.time.Clock()

# Pac-Man Başlangıç Pozisyonu (Satır 10, Sütun 9'daki kareden başlasın)
grid_x = 9
grid_y = 10

# Gerçek Piksel Pozisyonları (Karelerin tam ortasında durması için)
x = grid_x * CELL_SIZE + CELL_SIZE // 2
y = grid_y * CELL_SIZE + CELL_SIZE // 2

dx = 0
dy = 0
SPEED = 3  # Hız CELL_SIZE'ın (30) tam böleni olmalı! (3, 5 veya 6 idealdir)

PACMAN_RADIUS = 12
score = 0
font = pygame.font.SysFont("Arial", 20, bold=True)


# 2. DUVARA ÇARPIŞMA KONTROLÜ
def can_move(next_x, next_y):
    """Bir sonraki adımda duvara çarpıp çarpmayacağımızı kontrol eden fonksiyon"""
    # Karakterin 4 köşesini de kontrol ediyoruz
    margin = 2  # Yumuşak dönüş için küçük tolerans
    corners = [
        (next_x - PACMAN_RADIUS + margin, next_y - PACMAN_RADIUS + margin),
        (next_x + PACMAN_RADIUS - margin, next_y - PACMAN_RADIUS + margin),
        (next_x - PACMAN_RADIUS + margin, next_y + PACMAN_RADIUS - margin),
        (next_x + PACMAN_RADIUS - margin, next_y + PACMAN_RADIUS - margin),
    ]

    for cx, cy in corners:
        col = int(cx // CELL_SIZE)  # Hangi sütunda?
        row = int(cy // CELL_SIZE)  # Hangi satırda?

        # Sınır dışı kontrolü
        if row < 0 or row >= len(MAP) or col < 0 or col >= len(MAP[0]):
            return False
        # Eğer gideceğimiz kare 1 (Duvar) ise gidemeyiz
        if MAP[row][col] == 1:
            return False
    return True


# 3. PACMAN VE MAP ÇİZİMİ
def draw_map():
    for row_idx, row in enumerate(MAP):
        for col_idx, cell in enumerate(row):
            px = col_idx * CELL_SIZE
            py = row_idx * CELL_SIZE

            if cell == 1:
                # Duvar (Mavi Kare)
                pygame.draw.rect(
                    screen, (0, 0, 255), (px + 1, py + 1, CELL_SIZE - 2, CELL_SIZE - 2)
                )
            elif cell == 0:
                # Yem (Küçük Kırmızı/Beyaz Nokta - Tam ortada)
                pygame.draw.circle(
                    screen,
                    (255, 255, 255),
                    (px + CELL_SIZE // 2, py + CELL_SIZE // 2),
                    3,
                )


def create_pacman(pacman_x, pacman_y):
    pygame.draw.circle(screen, (255, 255, 0), (pacman_x, pacman_y), PACMAN_RADIUS)


# 4. OYUN DÖNGÜSÜ
is_running = True
while is_running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                dx, dy = 0, SPEED
            elif event.key == pygame.K_UP:
                dx, dy = 0, -SPEED
            elif event.key == pygame.K_RIGHT:
                dx, dy = SPEED, 0
            elif event.key == pygame.K_LEFT:
                dx, dy = -SPEED, 0

    # BİR SONRAKİ ADIM KONTROLÜ
    # Eğer gideceğimiz yön duvar DEĞİLSE hareket et
    if can_move(x + dx, y + dy):
        x += dx
        y += dy

    # YEM YEME KONTROLÜ
    current_col = int(x // CELL_SIZE)
    current_row = int(y // CELL_SIZE)

    # Bulunduğumuz karede yem varsa (0 ise) yemi kaldır (2 yap)
    if MAP[current_row][current_col] == 0:
        MAP[current_row][current_col] = 2
        score += 10

    # ÇİZİMLER
    screen.fill((0, 0, 0))

    draw_map()  # Harita ve Yemler Çizilir
    create_pacman(x, y)  # Pac-Man Çizilir

    # Skor
    score_text = font.render(f"Skor: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 5))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()