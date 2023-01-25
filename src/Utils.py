import pygame
pygame.init()

# cached assets
img = pygame.image.load('MENU_PNG/panel_blue.png')
normal = pygame.image.load('MENU_PNG/buttonLong_brown.png')
pressed = pygame.image.load('MENU_PNG/buttonLong_brown_pressed.png')


def unpack_tilemap(tilesheet, width, height, size=4, scale=4):
    list_of_tile_images = []
    x_range = (int)(width / size)
    y_range = (int)(height / size)
    for y in range(y_range):
        for x in range(x_range):
            sprite = tilesheet.subsurface(x*size, y*size, size, size)
            sprite = pygame.transform.scale(sprite, (size*scale, size*scale))
            list_of_tile_images.append(sprite)
    return list_of_tile_images

def adjacent_coord(rect, size, x, y):
    coord = (rect.x + (x * size), rect.y - (y * size))
    return coord

def parse_text(text):
    lines = []
    linelength = 20

    line = ''
    for i in text.split():
        if len(i) + len(line) <= linelength:
            line += i + ' '
        else:
            lines.append(line.strip())
            line = i + ' '
    if line != '':
        lines.append(line.strip())
    return lines

def button(screen, x, y, text):
    pass

def textbox(screen, text, x, y, scale, options = [], textcolour = (50, 50, 50)):
    font = pygame.font.Font('FONTS/Kenney Pixel.ttf', 8*scale)
    position = (x, y)
    keys, pos = pygame.key.get_pressed(), pygame.mouse.get_pos()
    rtn = 0
    
    # seperating text into lines without cutting off words
    lines = parse_text(text)
    
    # height and width of the textbox depends on the number of lines and clickable options
    width = 65*scale
    height = 15*scale*len(options) + 8*scale*len(lines) + 5*scale
    
    # drawing background textbox
    textbox = pygame.Surface((width, height))
    textbox.blit(pygame.transform.scale(img, (width, height)), (0, 0))

    # displaying the buttons 
    for i, option in enumerate(options):
        option_surface = font.render(option, True, textcolour)
        option_rect = option_surface.get_rect(center=(width/2, scale*(i*15+8+len(lines)*8)))
        option_pos = (2*scale, scale*(i*15+3+len(lines)*8))
        
        # actual position of the button on the screen rather than within the textbox surface
        real_rect = pygame.Rect((option_pos[0]+x, option_pos[1]+y, width-4*scale, scale*13)) 

        # if the curser hovers over the button, display a different image
        # if the button is pressed, change the return value to the button pressed
        if real_rect.collidepoint(pos):
            textbox.blit(pygame.transform.scale(pressed, (width-4*scale, scale*13)), option_pos)
            if any(e.type == pygame.MOUSEBUTTONDOWN for e in pygame.event.get()):
                rtn = i+1
        else:
            textbox.blit(pygame.transform.scale(normal, (width-4*scale, scale*13)), option_pos)
            
        textbox.blit(option_surface, option_rect)
    
    # writing each line of text
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, textcolour)
        text_rect = text_surface.get_rect(center=(width/2, scale*(i*8+6)))
        textbox.blit(text_surface, text_rect)

    # colorkey removes background efficiently
    textbox.set_colorkey((0, 0, 0))
    screen.blit(textbox, position)
    
    return int(rtn)    
