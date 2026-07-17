import pygame
import sys

# 1. Oyun Kurulumu ve Sabitler
pygame.init()
GENISLIK, YUKSEKLIK = 600, 650
screen = pygame.display.set_mode([GENISLIK, YUKSEKLIK])
pygame.display.set_caption("Pygame Pac-Man")
clock = pygame.time.Clock()

# Renkler (RGB)
SIYAH = (0, 0, 0)
MAVI = (0, 0, 255)
SARI = (255, 255, 0)
KIRMIZI = (255, 0, 0)
BEYAZ = (240, 240, 240)

# 2. Harita Tasarımı (Grid Sistemi)
# 1 = Duvar, 0 = Boş alan (Yem var), 2 = Boş alan (Yem yok/Başlangıç noktası)
# Her bir hücre 30x30 piksel boyutunda olacak
HOCRE_BOYUTU = 30
HARITA = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1],
    [1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,0,1,1,1,1,1,1,0,1,0,1,1,0,1],
    [1,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,0,1,1,1,2,1,1,2,1,1,1,0,1,1,1,1],
    [2,2,2,1,0,1,2,2,2,2,2,2,2,2,1,0,1,2,2,2],
    [1,1,1,1,0,1,2,1,1,2,2,1,1,2,1,0,1,1,1,1],
    [2,2,2,2,0,2,2,1,2,2,2,2,1,2,2,0,2,2,2,2],
    [1,1,1,1,0,1,2,1,1,1,1,1,1,2,1,0,1,1,1,1],
    [2,2,2,1,0,1,2,2,2,2,2,2,2,2,1,0,1,2,2,2],
    [1,1,1,1,0,1,2,1,1,1,1,1,1,2,1,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,1],
    [1,0,1,1,0,1,1,1,0,1,1,0,1,1,1,0,1,1,0,1],
    [1,0,0,1,0,0,0,0,0,2,2,0,0,0,0,0,1,0,0,1],
    [1,1,0,1,0,1,0,1,1,1,1,1,1,0,1,0,1,0,1,1],
    [1,0,0,0,0,1,0,0,0,1,1,0,0,0,1,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
]

# Grid koordinatını gerçek piksel koordinatına çeviren yardımcı fonksiyon
def grid_to_pixel(satir, sutun):
    return sutun * HOCRE_BOYUTU + HOCRE_BOYUTU // 2, satir * HOCRE_BOYUTU + HOCRE_BOYUTU // 2

# Bir sonraki hareketin duvara çarpıp çarpmayacağını kontrol eden fonksiyon
def can_move(x, y, yon_x, yon_y):
    # Karakterin 4 köşesini de kontrol ediyoruz (yumuşak hareket için)
    tolerans = 2
    sol_x = (x - HOCRE_BOYUTU // 2 + tolerans) + yon_x
    sag_x = (x + HOCRE_BOYUTU // 2 - tolerans) + yon_x
    ust_y = (y - HOCRE_BOYUTU // 2 + tolerans) + yon_y
    alt_y = (y + HOCRE_BOYUTU // 2 - tolerans) + yon_y

    koseler = [
        (sol_x, ust_y),
        (sag_x, ust_y),
        (sol_x, alt_y),
        (sag_x, alt_y)
    ]

    for kx, ky in koseler:
        grid_x = kx // HOCRE_BOYUTU
        grid_y = ky // HOCRE_BOYUTU
        # Sınır dışı kontrolü
        if grid_y < 0 or grid_y >= len(HARITA) or grid_x < 0 or grid_x >= len(HARITA[0]):
            return False
        if HARITA[grid_y][grid_x] == 1:
            return False
    return True

# 3. Nesne Sınıfları
class Pacman:
    def __init__(self):
        # Başlangıç pozisyonu (Grid 16, 9 -> piksel cinsinden)
        self.x, self.y = grid_to_pixel(16, 9)
        self.hiz = 3
        self.yon_x = 0
        self.yon_y = 0
        self.istenen_yon_x = 0
        self.istenen_yon_y = 0

    def update(self):
        # Eğer oyuncu yeni bir yöne dönmek istiyorsa ve o yol boşsa yönü değiştir
        if can_move(self.x, self.y, self.istenen_yon_x * self.hiz, self.istenen_yon_y * self.hiz):
            self.yon_x = self.istenen_yon_x
            self.yon_y = self.istenen_yon_y

        # Mevcut yönde ilerle
        if can_move(self.x, self.y, self.yon_x * self.hiz, self.yon_y * self.hiz):
            self.x += self.yon_x * self.hiz
            self.y += self.yon_y * self.hiz

    def draw(self, surface):
        # Basit bir Pac-man çizimi (Sarı Daire)
        pygame.draw.circle(surface, SARI, (self.x, self.y), 13)
        
        # Ağız efekti (Hareket yönüne göre küçük bir üçgen/kesik çiziyoruz)
        if self.yon_x == 1: # Sağa
            pygame.draw.polygon(surface, SIYAH, [(self.x, self.y), (self.x + 15, self.y - 7), (self.x + 15, self.y + 7)])
        elif self.yon_x == -1: # Sola
            pygame.draw.polygon(surface, SIYAH, [(self.x, self.y), (self.x - 15, self.y - 7), (self.x - 15, self.y + 7)])
        elif self.yon_y == 1: # Aşağı
            pygame.draw.polygon(surface, SIYAH, [(self.x, self.y), (self.x - 7, self.y + 15), (self.x + 7, self.y + 15)])
        elif self.yon_y == -1: # Yukarı
            pygame.draw.polygon(surface, SIYAH, [(self.x, self.y), (self.x - 7, self.y - 15), (self.x + 7, self.y - 15)])

class Hayalet:
    def __init__(self):
        self.x, self.y = grid_to_pixel(8, 9)
        self.hiz = 2
        self.yon_x = 1
        self.yon_y = 0

    def update(self, hedef_x, hedef_y):
        # Basit Takip Yapay Zekası:
        # Yol ayrımlarında hedefe (Pac-man'e) en yakın olan boş yönü seçer
        if self.x % HOCRE_BOYUTU == HOCRE_BOYUTU // 2 and self.y % HOCRE_BOYUTU == HOCRE_BOYUTU // 2:
            olasi_yonler = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            en_iyi_yon = (self.yon_x, self.yon_y)
            en_kisa_mesafe = 999999
            
            for yx, yy in olasi_yonler:
                # Geriye doğru yürümeyi engelle
                if yx == -self.yon_x and yy == -self.yon_y:
                    continue
                if can_move(self.x, self.y, yx * self.hiz, yy * self.hiz):
                    # Bir adım sonraki hayali mesafe hesaplanır
                    gelecek_x = self.x + yx * HOCRE_BOYUTU
                    gelecek_y = self.y + yy * HOCRE_BOYUTU
                    mesafe = (gelecek_x - hedef_x)**2 + (gelecek_y - hedef_y)**2
                    if mesafe < en_kisa_mesafe:
                        en_kisa_mesafe = mesafe
                        en_iyi_yon = (yx, yy)
            
            self.yon_x, self.yon_y = en_iyi_yon

        # Hareket et
        if can_move(self.x, self.y, self.yon_x * self.hiz, self.yon_y * self.hiz):
            self.x += self.yon_x * self.hiz
            self.y += self.yon_y * self.hiz

    def draw(self, surface):
        # Hayalet kafası (Kırmızı daire) ve altındaki dalgalı gövdeyi taklit eden kutu
        pygame.draw.circle(surface, KIRMIZI, (self.x, self.y - 2), 13)
        pygame.draw.rect(surface, KIRMIZI, (self.x - 13, self.y - 2, 26, 15))
        # Gözler (İki beyaz küçük daire)
        pygame.draw.circle(surface, BEYAZ, (self.x - 5, self.y - 4), 4)
        pygame.draw.circle(surface, BEYAZ, (self.x + 5, self.y - 4), 4)

# 4. Oyun Nesnelerini Yaratma
pacman = Pacman()
blinky = Hayalet()
skor = 0
font = pygame.font.SysFont("Arial", 28, bold=True)
oyun_bitti = False

# Yol üzerindeki yemleri haritadan sayıp toplam yem hedefini buluyoruz
toplam_yem = sum(satir.count(0) for satir in HARITA)

# --- ANA OYUN DÖNGÜSÜ ---
while True:
    # 5. Olay Yönetimi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if oyun_bitti:
                # Oyun bittiğinde herhangi bir tuşa basılırsa sıfırla
                HARITA = [satir.copy() for satir in HARITA] # Haritayı yenile (Basitlik adına bu örnekte statik kalıyor)
                pacman = Pacman()
                blinky = Hayalet()
                skor = 0
                oyun_bitti = False
            else:
                # Tuş girdilerini kuyruğa al (istenen yön olarak kaydet)
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    pacman.istenen_yon_x, pacman.istenen_yon_y = 1, 0
                elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    pacman.istenen_yon_x, pacman.istenen_yon_y = -1, 0
                elif event.key == pygame.K_UP or event.key == pygame.K_w:
                    pacman.istenen_yon_x, pacman.istenen_yon_y = 0, -1
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    pacman.istenen_yon_x, pacman.istenen_yon_y = 0, 1

    # 6. Oyun Güncellemeleri (Fizik ve Mantık)
    if not oyun_bitti:
        pacman.update()
        blinky.update(pacman.x, pacman.y)

        # Yemleri Yeme Mantığı
        p_grid_x = pacman.x // HOCRE_BOYUTU
        p_grid_y = pacman.y // HOCRE_BOYUTU
        if HARITA[p_grid_y][p_grid_x] == 0:
            HARITA[p_grid_y][p_grid_x] = 2 # Yemi kaldır (boş alan yap)
            skor += 10

        # Çarpışma Kontrolü (Pac-man ile Hayalet arasındaki mesafe)
        mesafe_kare = (pacman.x - blinky.x)**2 + (pacman.y - blinky.y)**2
        if mesafe_kare < 400: # Yaklaşık 20 piksel mesafe (çarpışma)
            oyun_bitti = True

    # 7. Çizim / Ekranı Boyama
    screen.fill(SIYAH)

    # Haritayı ve Yemleri Çiz
    for satir_idx, satir in enumerate(HARITA):
        for sutun_idx, hucre in enumerate(satir):
            x = sutun_idx * HOCRE_BOYUTU
            y = satir_idx * HOCRE_BOYUTU
            if hucre == 1:
                # Duvarları çiz (Mavi kareler)
                pygame.draw.rect(screen, MAVI, (x + 1, y + 1, HOCRE_BOYUTU - 2, HOCRE_BOYUTU - 2), border_radius=4)
            elif hucre == 0:
                # Yemleri çiz (Küçük beyaz noktalar)
                pygame.draw.circle(screen, BEYAZ, (x + HOCRE_BOYUTU // 2, y + HOCRE_BOYUTU // 2), 3)

    # Karakterleri Çiz
    pacman.draw(screen)
    blinky.draw(screen)

    # Arayüz (Skor Tablosu) Çizimi
    skor_yazisi = font.render(f"SKOR: {skor}", True, BEYAZ)
    screen.blit(skor_yazisi, (15, YUKSEKLIK - 45))

    # Oyun Bitti Ekranı
    if oyun_bitti:
        overlay = pygame.Surface((GENISLIK, YUKSEKLIK))
        overlay.set_alpha(180)
        overlay.fill(SIYAH)
        screen.blit(overlay, (0, 0))
        
        bitti_yazisi = font.render("OYUN BITTI! Yeniden baslamak icin bir tusa basin.", True, KIRMIZI)
        bitti_rect = bitti_yazisi.get_rect(center=(GENISLIK // 2, YUKSEKLIK // 2))
        screen.blit(bitti_yazisi, bitti_rect)

    pygame.display.flip()
    clock.tick(60)