import pygame
import os

def previous_music(k):
    num = k
    if num == 1 or num == 2:
        return num-1
    else:
        return 2

def next_music(l):
    num = l
    if num == 0 or num == 1:
        return num+1
    else:
        return 0
    

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Music player")

font = pygame.font.Font(None, 32)
button_font = pygame.font.Font(None, 30)

songs = ['Baseke.mp3', 'Despacito.mp3', 'Tere_Neina.mp3']
music_path = 'sounds/'
i = 0

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

start_button_rect = pygame.Rect(300, 400, 200, 50)
start_button_clicked = False

screen.fill(WHITE)

label = pygame.font.Font(None, 32)  # Use a standard font for rendering text

# Use standard font for rendering text
welcome_label = label.render('Welcome to the music player', True, (193, 196, 199))
start_label = label.render('Start', True, (115, 132, 148))
start_label_rect = start_label.get_rect(topleft=(250, 300))

play_button_rect = pygame.Rect(100, 300, 125, 50)
pause_button_rect = pygame.Rect(225, 300, 125, 50)
previous_button_rect = pygame.Rect(100, 350, 125, 50)
next_button_rect = pygame.Rect(225, 350, 125, 50)

play_label = button_font.render('Play', True, BLACK)
pause_label = button_font.render('Pause', True, BLACK)
previous_label = button_font.render('Previous', True, BLACK)
next_label = button_font.render('Next', True, BLACK)

music_label = button_font.render('Musics:',True,BLACK)

first_music_label=button_font.render('1.Baseke', True,BLACK)
second_music_label=button_font.render('2.Despacito', True,BLACK)
third_music_label=button_font.render('3.Tere Naina', True,BLACK)

first_music_rect=pygame.Rect(150,100,200,50)
second_music_rect=pygame.Rect(150,150,200,50)
third_music_rect=pygame.Rect(150,200,200,50)


gameplay = False
play = False
current_track = None
is_playing = False

while not play:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = True
        #if not gameplay:


    if not gameplay:
        screen.fill((87, 88, 89))
        screen.blit(welcome_label, (100, 200))  # Adjust position for welcome label
        screen.blit(start_label, start_label_rect)  # Pass the rect directly to blit
        mouse = pygame.mouse.get_pos()
        if start_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:  # Use [0] to check left mouse button
            gameplay = True
    else:
        screen.fill((0,153,0))
        screen.blit(music_label, (150,50))

        mouse = pygame.mouse.get_pos()

        pygame.draw.rect(screen, GRAY, play_button_rect)
        pygame.draw.rect(screen, GRAY, pause_button_rect)
        pygame.draw.rect(screen, GRAY, previous_button_rect)
        pygame.draw.rect(screen, GRAY, next_button_rect)

        screen.blit(play_label, (play_button_rect.centerx - play_label.get_width() // 2, play_button_rect.centery - play_label.get_height() // 2))
        screen.blit(pause_label, (pause_button_rect.centerx - pause_label.get_width() // 2, pause_button_rect.centery - pause_label.get_height() // 2))
        screen.blit(previous_label, (previous_button_rect.centerx - previous_label.get_width() // 2, previous_button_rect.centery - previous_label.get_height() // 2))
        screen.blit(next_label, (next_button_rect.centerx - next_label.get_width() // 2, next_button_rect.centery - next_label.get_height() // 2))

        pygame.draw.rect(screen, GRAY, first_music_rect)
        pygame.draw.rect(screen, GRAY, second_music_rect)
        pygame.draw.rect(screen, GRAY, third_music_rect)

        screen.blit(first_music_label, (first_music_rect.centerx - first_music_label.get_width() // 2, first_music_rect.centery - first_music_label.get_height() // 2))
        screen.blit(second_music_label, (second_music_rect.centerx - second_music_label.get_width() // 2, second_music_rect.centery - second_music_label.get_height() // 2))
        screen.blit(third_music_label, (third_music_rect.centerx - third_music_label.get_width() // 2, third_music_rect.centery - third_music_label.get_height() // 2))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                play = True
            elif first_music_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(os.path.join(music_path, songs[0]))
                pygame.mixer.music.play()
                i=0
                is_playing=True
            elif second_music_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(os.path.join(music_path, songs[1]))
                pygame.mixer.music.play()
                i=1
                is_playing=True
            elif third_music_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                pygame.mixer.music.stop()
                pygame.mixer.music.load(os.path.join(music_path, songs[2]))
                pygame.mixer.music.play()
                i=2
                is_playing=True
            if is_playing:
                pause=False
                if pause_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    pygame.mixer.music.pause()
                    #pause=True
                if play_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                        pygame.mixer.music.unpause()
                if previous_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    pygame.mixer.music.stop()
                    i=previous_music(i)
                    pygame.mixer.music.load(os.path.join(music_path, songs[i]))
                    pygame.mixer.music.play()
                if next_button_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
                    pygame.mixer.music.stop()
                    i = next_music(i)
                    pygame.mixer.music.load(os.path.join(music_path, songs[i]))
                    pygame.mixer.music.play()
                    


        #саған енді кнопканы басқандағы кодты істеу керек сонымен почти болған сияқты   
    pygame.display.flip()
        

pygame.quit()
