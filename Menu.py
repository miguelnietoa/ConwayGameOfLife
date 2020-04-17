import pygame
import os
import Grafico

print('iniciado Menu')
pygame.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
pantalla = pygame.display.set_mode([600, 500])
pygame.display.set_caption('Menú - Juego de la Vida de Conway')
reloj = pygame.time.Clock()
pantalla.fill((0, 0, 0))

fuente = pygame.font.SysFont('Courier', 20)
btn_grafica = pygame.draw.rect(pantalla, (255, 255, 255), [200,
                                                           200,
                                                           200,
                                                           35])
btn_animacion = pygame.draw.rect(pantalla, (255, 255, 255), [200,
                                                             300,
                                                             200,
                                                             35])
text = fuente.render('Juego de la Vida de Conway', 1, (255, 255, 255))


def dibujar_texto(texto, btn_rect, fuente_render, color):
    text = fuente_render.render(texto, 1, color)
    rect_text = text.get_rect()
    x = (btn_rect.w - rect_text.w) // 2 + btn_rect.x
    y = (btn_rect.h - rect_text.h) // 2 + btn_rect.y
    pantalla.blit(text, [x, y])


op = 0
while op == 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            op = 3
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            if btn_grafica.collidepoint(pos):
                op = 1
            elif btn_animacion.collidepoint(pos):
                op = 2

    pantalla.fill((0, 0, 0))

    btn_grafica = pygame.draw.rect(pantalla, (255, 255, 255), [200,
                                                               200,
                                                               200,
                                                               35])
    btn_animacion = pygame.draw.rect(pantalla, (255, 255, 255), [200,
                                                                 300,
                                                                 200,
                                                                 35])
    dibujar_texto('Ver gráfica', btn_grafica, fuente, (0, 0, 0))
    dibujar_texto('Ver animación', btn_animacion, fuente, (0, 0, 0))
    pantalla.blit(text, [150, 100])
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
if op == 1:
    Grafico.start()
elif op == 2:
    pass
