import random
import pygame 
arquivo = open ("dados.txt","a")
nome = input(str( "Qual seu Nome?" ))
gmail = input(str( "Qual seu Gmail?" ))
arquivo.write(nome + " "+ gmail + " \n")
arquivo.close()

pygame.init()

pygame.display.set_caption("Jogo Educacional CC-IMED 2021")

largura = 1200
altura = 627 
display = pygame.display.set_mode( (largura, altura) )
fps = pygame.time.Clock()
fundo = pygame.image.load("assets/bibio.png")
estudante = pygame.image.load("assets/perso1.png")
branco = (255,255,255)
livro = pygame.image.load("assets/book3.png")

posicaoX = random.randint(10,1100)
posicaoY = 0
pontos = 0

def escrevendoPlacar(pontos):
    font = pygame.font.SysFont(None, 80)
    texto = font.render("Pontos: "+str(pontos), True, branco)
    display.blit(texto, (20, 130))

def verifica(x,y,posicaoX, posicaoY): 
    global pontos
    if x >= posicaoX and x <= posicaoX  + 70:
        if y >= posicaoY and y <= posicaoY + 50:
            posicaoY = 0 
            posicaoX = random.randint(10,1100)
            pontos += 1
    return posicaoX, posicaoY, pontos 

while True:
    display.fill((0,0,0))
   
    if pontos >= 20:
        pygame.quit()
        quit()
    x,y = pygame.mouse.get_pos()

    posicaoX, posicaoY, pontos = verifica(x,y,posicaoX, posicaoY)

    if posicaoY > 650:
        posicaoY = 0
        posicaoX = random.randint(10,1100)

    posicaoY = posicaoY + 6

    # verefica interação  do  usuario 
    for evento in pygame.event.get(): 
        if evento.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    # Fim da vereficação 
    display.blit(fundo, (0,0))
    display.blit(estudante,(550, 420))
    display.blit(livro,(posicaoX, posicaoY))

    escrevendoPlacar(pontos)

    pygame.display.update()

    fps.tick(60)
