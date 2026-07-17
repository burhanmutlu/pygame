

    # ÖNEMLİ: Her karede ekranı yeniden boyamazsak eski çizimler ekranda kalır!
    screen.fill(BEYAZ)

    # Daire çiz: (ekran, renk, (merkez_x, merkez_y), yarıçap)
    pygame.draw.circle(screen, MAVI, (400, 300), 50)

    # Dikdörtgen çiz: (ekran, renk, (sol_x, üst_y, genişlik, yükseklik))
    pygame.draw.rect(screen, KIRMIZI, (100, 100, 120, 80))

    # Çizgi çiz: (ekran, renk, başlangıç, bitiş, kalınlık)
    pygame.draw.line(screen, SARI, (0, 0), (800, 600), 5)


font = pygame.font.SysFont(None, 36)

text_surface = font.render("Score: 0", True, (255, 255, 255))

text_rect = text_surface.get_rect()
text_rect.topleft = (20, 20) # Position near top-left corner


pygame.mixer.Sound("efekt.wav").play()  # Play the sound effect