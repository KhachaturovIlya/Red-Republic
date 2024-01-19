import pygame


#Стартовая инициализация
pygame.init()
screen = pygame.display.set_mode((1920, 1080), 0, 32)
pygame.display.set_caption("Commy Republic")
clock = pygame.time.Clock()
channel1 = pygame.mixer.Channel(0)
channel2 = pygame.mixer.Channel(1)
check = True

#Текст
game_name = 'Communist Republic'
start_space = 'Нажмите пробел, чтобы начать'
p1_s1 = 'Меня зовут Иван Романов.'
p1_s2 = 'Сразу после выпуска из универстита меня назначили на должность управляющего в'
p1_s3 = 'небольшом городке на севере страны. Тогда, я ещё был рад своей новой работе...'
p1_s4 = 'Лишь только я увидел приказ, как сразу рванул к ближайшему аэропорту.'
p1_s5 = 'Вскоре я уже пересекал всю свою огромную и необъятную Родину.'
p1_s6 = 'Я надеялся на то, что новая обстановка позволит мне расширить мой кругозор.'
p1_s7 = 'Но к моему удивлению, цель моего назначения представляла жалкое зрелище.'
p1_s8 = 'Огромное количество заводов, разрушенные дороги, однотипные многоэтажки.'
p1_s9 = 'Мне явно предстояла большая работа!'
p1_s10 = 'Мне оставалось только лишь направиться в сторону управдома.'

p2_s1 = 'Кажется, у меня звонит телефон.'

p2_s2 = 'Поздравляю вас с назначением, товарищ управгор!'
p2_s3 = 'Спасибо, конечно, но кто вы такой?'

#Подгрузка фоток
start_image = pygame.image.load('images/image11.png')
kabinet_image = pygame.image.load('images/kabinet.png')
right_image = pygame.image.load('images/right.png')
left_image = pygame.image.load('images/left.png')

#Музыка
radio = []
effect = []
radio.append(pygame.mixer.Sound('music/International.mp3'))
radio.append(pygame.mixer.Sound('music/Yablochko.mp3'))
effect.append(pygame.mixer.Sound('music/phone.mp3'))


def screen_print_run(word, x, y, font, color, fps):
    txt_b = []
    myfont = pygame.font.Font('Fonts/Minecraft Seven_2.ttf', font)
    for pos in range(0, len(word)):
        for some_event in pygame.event.get():
            if some_event.type == pygame.KEYUP and some_event.key == pygame.K_SPACE:
                screen.blit(myfont.render(word, False, color), (x, y))
                pygame.display.update()
                return 0
        txt_a = ''
        txt_b.append(word[pos])
        for c in txt_b:
            txt_a += c

        screen.blit(myfont.render(txt_a, False, color), (x, y))
        pygame.display.update()
        clock.tick(fps)


def screen_print_stay(word, x, y, font, color):
    myfont = pygame.font.Font('Fonts/Minecraft Seven_2.ttf', font)
    screen.blit(myfont.render(word, False, color), (x, y))
    pygame.display.update()


def button_check(position, button):
    while 1:
        for some_event in pygame.event.get():
            if some_event.type == position and some_event.key == button:
                return 0


def txt_tab():
    pygame.draw.rect(screen, [244, 252, 212], (0, 900, 1920, 180))
    pygame.draw.rect(screen, 'Black', (0, 880, 1920, 20))
    pygame.draw.rect(screen, [244, 252, 212], (0, 800, 200, 80))
    pygame.draw.rect(screen, 'Black', (0, 790, 200, 10))
    pygame.draw.rect(screen, 'Black', (200, 790, 10, 100))
    up()


def print_name(x):
    screen_print_stay(x, 16, 790, 60, 'Black')
    up()


def up():
    pygame.display.update()


def music_play(song, volume, channel):
    pygame.mixer.music.set_volume(volume)
    if channel == 1:
        channel1.play(song, loops=-1)
    elif channel == 2:
        channel2.play(song, loops=-1)


def music_pause(channel):
    if channel == 1:
        channel1.pause()
    elif channel == 2:
        channel2.pause()


music_play(radio[0], 0.005, 1)
screen.blit(start_image, (0, 0))
screen_print_stay(game_name, 625, 60, 60, 'Black')
screen_print_run(start_space, 400, 900, 60, 'Black', 45)
button_check(pygame.KEYUP, pygame.K_SPACE)
music_pause(1)

screen.fill([0, 0, 0])
screen_print_run(p1_s1, 20, 10, 32, 'White', 40)
screen_print_run(p1_s2, 20, 70, 32, 'White', 40)
screen_print_run(p1_s3, 20, 130, 32, 'White', 40)
screen_print_run(p1_s4, 20, 190, 32, 'White', 40)
screen_print_run(p1_s5, 20, 250, 32, 'White', 40)
screen_print_run(p1_s6, 20, 310, 32, 'White', 40)
screen_print_run(p1_s7, 20, 370, 32, 'White', 40)
screen_print_run(p1_s8, 20, 430, 32, 'White', 40)
screen_print_run(p1_s9, 20, 490, 32, 'White', 40)
screen_print_run(p1_s10, 20, 550, 32, 'White', 40)
button_check(pygame.KEYUP, pygame.K_SPACE)

music_play(radio[1], 0.01, 1)
screen.blit(kabinet_image, (0, 0))
up()
pygame.time.delay(5000)
txt_tab()
print_name('Я')
screen_print_run(p2_s1, 20, 920, 32, 'Black', 28)
pygame.time.delay(3000)
music_play(effect[0], 0.2, 2)

while check:
    screen.blit(left_image, (0, 0))
    up()
    for i in range(0, 500):
        for klav in pygame.event.get():
            if klav.type == pygame.MOUSEBUTTONDOWN:
                check = False
                break
        pygame.time.delay(1)
    screen.blit(right_image, (0, 0))
    up()
    for i in range(0, 500):
        for klav in pygame.event.get():
            if klav.type == pygame.MOUSEBUTTONDOWN:
               check = False
        pygame.time.delay(1)

music_pause(2)
screen.blit(kabinet_image, (0, 0))
txt_tab()
print_name('???')
screen_print_run(p2_s2, 20, 900, 32, 'Black', 40)
button_check(pygame.KEYUP, pygame.K_SPACE)
txt_tab()
print_name('Я')
screen_print_run(p2_s3, 20, 900, 32, 'Black', 40)
button_check(pygame.KEYUP, pygame.K_SPACE)