#!/usr/local/bin/python
import pygame
import sys



def check_quit():
    global pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

def syskargs(sysargs):
    args = []
    kargs = {}

    for arg in sysargs[1:]:
        if '=' in arg:
            k,v = arg.split('=')
            kargs[k] = v
        else:
            args.append(arg)
    return args,kargs

def defaultValue(dict,key,val): 
      
    if not key in dict.keys(): 
        dict[key] = val

    return dict

def draw_dot(color,x,y):
    global pygame
    global screen
    pygame.draw.line(screen,color,[x+1,y-1],[x-1,y+1])
    pygame.draw.line(screen,color,[x-1,y-1],[x+1,y+1])

if __name__=='__main__':

    args,kargs = syskargs(sys.argv)

    # kargs = defaultValue(kargs,'width',800)
    # kargs = defaultValue(kargs,'height',640)
    # kargs = defaultValue(kargs,'space',20)

    # Define the colors we will use in RGB format
    BLACK = (  0,   0,   0)
    WHITE = (255, 255, 255)
    BLUE =  (  0,   0, 255)
    GREEN = (  0, 255,   0)
    RED =   (255,   0,   0)

    width = kargs.get('width', 800)
    height = kargs.get('height', 640)
    space = kargs.get('space', 20)

    pygame.init()

    screen = pygame.display.set_mode([width,height])

    screen.fill(WHITE)

    pygame.display.set_caption("Dots Game")

    clock = pygame.time.Clock()

    while (True):
        screen.fill(WHITE)
        #pygame.draw.line(screen,BLUE,[0,0],[width,height],3)
        for y in range(int(space/2),int(height-(space/4)),space):
            for x in range(int(space/2),int(width-(space/4)),space):
                #pygame.draw.line(screen,RED,[x,y],[x+1,y+1])
                draw_dot(RED,x,y)

        
        check_quit()
        
        pygame.display.flip()