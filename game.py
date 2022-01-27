#Arsen Djurdjev, 2022 January



import pygame
import random


#generate a maze in function



import random
# create pygame window and make it infinite loop
pygame.init()




white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 100, 128)
 
screen_width = 480
screen_height = 640
score = 0

ime = ""



pygame.mixer.init()



display_surface = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("2D igra u Python")
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render(str(score), True, green, blue)
textRect = text.get_rect()
text2 = font.render(ime, True, green, blue)
textRect2 = text.get_rect()



#pygame title
screen = pygame.display.set_mode((screen_height, screen_width))
clock = pygame.time.Clock()
running = True
x = 320
y = 240
x1 = random.randint(100,screen_width-100)
y1 = random.randint(100, screen_height-100)

print(x1,y1)


b1 = random.randint(0, 255)
b2 = random.randint(0, 255)
b3 = random.randint(0, 255)

#generate random number in range 0-500
while running:
    if(pygame.key.get_pressed()[pygame.K_ESCAPE]):
        running = False
    
    
    text = font.render(str(score), True, white, blue)

    
    text2 = font.render(ime, True, green, blue)
    display_surface.blit(text2, textRect2)
    display_surface.blit(text, textRect)
    
    
    if((x-x1 <10) and (y-y1 < 10) and (x-x1 > -50) and (y-y1 > -50)):
        score+=1
        x1 = random.randint(100,screen_width-200)
        y1 = random.randint(100, screen_height-200)
        print("Nova lokacija",x1,y1)
    
    # check for quit event

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
    #print "hello world" function in pygame window      
            
            
    #print a shape
    #listen to wasd keys in keyboard
    #print(y)
    if pygame.key.get_pressed()[pygame.K_UP]:
        y -= 0.1
    elif pygame.key.get_pressed()[pygame.K_w]:
     y -= 0.1
        
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        y += 0.1
    elif pygame.key.get_pressed()[pygame.K_s]:
     y += 0.1
     
     
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        x -= 0.1
    elif pygame.key.get_pressed()[pygame.K_a]:
     x -= 0.1
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        x+=0.1
    elif pygame.key.get_pressed()[pygame.K_d]:
     x += 0.1
    
    if(y>=screen_width):
        y = 0
    if (y<-40):
        y = screen_width
    
    if(x>=screen_height):
        x = 0
        
    if(x<-40):
        x = screen_height
        
        
    #draw circle
    pygame.draw.circle(screen, (random.randint(0, 255),random.randint(0, 255),random.randint(0, 255)), (x1, y1), 10)   #HRANA
     
    #Igrac    
    pygame.draw.rect(screen, (200, 200, 100), (x, y, 50, 50), 20)
    pygame.draw.circle(screen, (255, 255, 255), (x+10, y+8), 6)   
    pygame.draw.circle(screen, (255, 255, 255), (x+40, y+8), 6)
    pygame.draw.circle(screen, (0, 80, 255), (x+10, y+8), 2)   
    pygame.draw.circle(screen, (0, 80, 255), (x+40, y+8), 2)
    pygame.draw.rect(screen, (255, 255, 255), (x+13, y+38, 25, 5), 6)
    pygame.draw.rect(screen, (255, 255, 255), (x+17, y+15, 15, 15), 30)     
    #kraj_igrac
    
    
# pygame.display.update()
# clock.tick(60)
    pygame.display.flip()
    # fill screen
    
    screen.fill((b1, b2, b3))
    if(b1>255):
        while(b1>=0):
            b1-=0.01
    b1+=0.01
    if(b2>255):
        while(b2>=0):
            b2-=0.002
    b2+=0.002
    if(b3>255):
        while(b3>=0):
            b3-=0.0003
    b3+=0.0003
   
    