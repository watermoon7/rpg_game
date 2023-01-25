import pygame
import random
import Levels
import Utils

pygame.init()
scale = 4

def load_level(level):
    block_list = []
    x = y = 0
    for row in level:
        for col in row:
            if col == "#":
                block = {
                    "rect": pygame.Rect(x, y, 16*scale, 16*scale),
                    "type": "forest",
                    "can_move": True,
                    "rand": random.random()
                    }
            else:
                block = {
                    "rect": pygame.Rect(x, y, 16*scale, 16*scale),
                    "type": "grass",
                    "can_move": True,
                    "rand": random.random()
                    }
            block_list.append(block)
            x = x + 16*scale
        y = y + 16*scale
        
        x = 0
        
    return block_list

screen = pygame.display.set_mode((320*scale,180*scale))

##########################################################################
# This is where the tilesheet gets loaded, this uses the Utils file
tiny_town_tilesheet = pygame.image.load("tilemap_packed_town.png").convert_alpha()
town_tiles = Utils.unpack_tilemap(tiny_town_tilesheet, tiny_town_tilesheet.get_width(), tiny_town_tilesheet.get_height(), 16, scale)

dungeon_tilesheet = pygame.image.load("tilemap_packed_dungeon.png").convert_alpha()
dungeon_tiles = Utils.unpack_tilemap(dungeon_tilesheet, dungeon_tilesheet.get_width(), dungeon_tilesheet.get_height(), 16, scale)

game_state = "GAME"

player = {
    "rect": pygame.Rect(128,128,16*scale,16*scale),
    "speed": 2*scale
    }

blocks = load_level(Levels.level01)
showtext_box = True

clock = pygame.time.Clock()
game_running = True
while game_running:
    ##################################################################################
    # This code runs every frame don't move or change this
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    dt = clock.tick(40)
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        game_state = "QUIT"

    ##################################################################################
    # QUIT state, setting the game state to this will close the game window
    if game_state == "QUIT":
        game_running = False
        
    ##################################################################################
    # GAME state, this is where we control the main game
    if game_state == "GAME":
        
        ##################################################################################
        # INPUT CODE
        targetX = pygame.Rect(player["rect"])
        targetY = pygame.Rect(player["rect"])
        
        if keys[pygame.K_a]:
            targetX.x -= player["speed"]
        if keys[pygame.K_d]:
            targetX.x += player["speed"]
        if keys[pygame.K_w]:
            targetY.y -= player["speed"]
        if keys[pygame.K_s]:
            targetY.y += player["speed"]

        for block in blocks:
            if block["can_move"] == False:
                if targetX.colliderect(block["rect"]):
                    if targetX.x < block["rect"].x:
                        targetX.right = block["rect"].left
                    else:
                        targetX.left = block["rect"].right
                if targetY.colliderect(block["rect"]):
                    if targetY.y < block["rect"].y:
                        targetY.bottom = block["rect"].top
                    else:
                        targetY.top = block["rect"].bottom
        
        player["rect"].x = targetX.x
        player["rect"].y = targetY.y

        ##################################################################################
        # DRAWING CODE
        # Background fill
        screen.fill((222,125,87))
        # Background tiles        
        for block in blocks:
            if block["type"] == "forest":
                screen.blit(town_tiles[19], block["rect"])
            if block["type"] == "grass":
                screen.blit(town_tiles[0], block["rect"])

                
        text = 'oooooooooooooooo oooooooooooooooo'
        a = ['1']
        b = ['1', '1']
        c = ['1', '1', '1']
        d = ['1', '1', '1', '1']
        e = ['1', '1', '1', '1', '1']
        
        if showtext_box == True:
            if Utils.textbox(screen, 'ConsumeCons umeConsumeConsumeCo nsumeConsumeCons umeConsumeConsum eConsume this item?', 600, 200, scale, e) == 1:
                showtext_box = False
            

        


        # Main layer - sprites here will appear on top of the forest and grass            
        
        
        # Player layer
        screen.blit(dungeon_tiles[45], player["rect"])
        
        # Top layer - we will use this later

        
    pygame.display.flip()

pygame.quit()
