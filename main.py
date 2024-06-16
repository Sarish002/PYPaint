
if __name__ == '__main__':

    import random

    import pygame
    from ttkbootstrap import *
    def change():
        listcount = 10
        pygame.init()
        screen = pygame.display.set_mode((1000, 800))
        pygame.display.set_caption("Draw 'n' Erase")
        clock = pygame.time.Clock()
        dt = 0
        running = True
        ox = 'Fill in the window!'
        player_pos = pygame.Vector2(400, 250)

        pygame.mixer.music.load('Daisy.mp3')
        pygame.mixer.music.play(-1, 0.0)
        Hello = pygame.mixer.Sound('AI.wav')
        screen.fill('#ffffff')
        pygame.display.flip()
        z = Scale_1.get()

        DIS = (Scale_1.get(), Scale_1.get())
        i = 0
        for j in Labellist.keys():
            if Labellist[j] == Combo_1.get():
                i = j

        root.destroy()


        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            Keys = pygame.key.get_pressed()



            if i != 'All1':
                Paintbrush = pygame.image.load(i)
                Paintbrush = pygame.transform.scale(Paintbrush, DIS)
                Paint = Paintbrush.get_rect()
                Paint.topright = player_pos
                pygame.display.update()

                screen.blit(Paintbrush, Paint)

            else:
                i = random.choice(list(Labellist.keys()))
                Paintbrush = pygame.image.load(random.choice(list(Labellist.keys())))
                Paintbrush = pygame.transform.scale(Paintbrush, DIS)
                Paint = Paintbrush.get_rect()
                Paint.topright = player_pos
                pygame.display.update()

                screen.blit(Paintbrush, Paint)

            show = True
            if show == True:
                down_font = pygame.font.Font('LucyTheCatRegular-Bg9x.ttf', 80)
                down_text = down_font.render(ox, True, 'black')
                down_rect = down_text.get_rect()
                down_rect.center = (500, 400)
                screen.blit(down_text, down_rect)

            if Keys[pygame.K_UP] and player_pos.y > 1:
                player_pos.y -= 10

            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pos())

            elif Keys[pygame.K_DOWN] and player_pos.y < 801 - int(z):
                player_pos.y += 10

            elif Keys[pygame.K_RIGHT] and player_pos.x < 1000 - (int(z) / (z * 7.75)):
                player_pos.x += 10

            elif Keys[pygame.K_LEFT] and player_pos.x > int(z) + 1:
                player_pos.x -= 10

            elif Keys[pygame.K_d]:
                listlabel = []
                H = pygame.mixer.Sound('mixkit-arcade-bonus-alert-767.wav')
                H.play()

            elif listcount == 0:
                running = False
                print('You Lost')
                listtup = 0
                for a in range(801):
                    for b in range(601):
                        pxarray = pygame.pixelarray.PixelArray(screen)
                        if pxarray[ 0, 0 ] == screen.map_rgb(255, 255, 255):
                            listtup += 1

                down_fonta = pygame.font.Font('ThisCafe-j9VqO.ttf', 90)
                down_texta = down_fonta.render('You win!', True, 'black')
                down_recta = down_texta.get_rect()
                down_recta.center = (400, 200)
                screen.blit(down_texta, down_recta)



            dt = clock.tick(100) / 1000




    Labellist = {'My first design 7.png': 'Light Pink', 'My first design 8.png': 'Wine', 'My first design 8 (1).png': 'Electric Blue', 'My first design 8 (2).png': 'Minty Green', 'My first design 8 (3).png': 'Lemon Yellow', 'My first design 8 (4).png':  'Flavescent', 'My first design 8 (5).png': 'Fusion Coral Red', 'My first design 8 (6).png': 'Sailing Tangerine Orange', 'My first design 8 (7).png': 'Widowmaker Blue', 'My first design 8 (8).png':'Cyan', 'All1':'All'}
    listlab = list(Labellist.values())
    root = Window(themename='minty')
    root.geometry('800x600')
    Frame_1 = Frame(master = root)
    Label_1 = Label(Frame_1, bootstyle = 'danger', text='Brush Size: ', font=('Franklin Gothic Heavy', 18))
    Label_1.pack()
    Label_2 = Label(Frame_1, bootstyle = 'danger', text='Brush Color: ', font=('Comic Sans MS', 18))

    Scale_1 = Scale(Frame_1, bootstyle = 'danger', value=63, to=257, length=200, from_=62)
    Scale_1.pack(pady = 20)
    Combo_1 = Combobox(Frame_1, bootstyle = 'danger')
    Label_2.pack(pady = 20)

    Combo_1['values'] = list(Labellist.values())
    Combo_1.pack()

    Buton = Button(master=root, text = 'OK!', command = change)
    Buton.place(relx = 0.5, rely = 0.75, anchor = 's')
    Frame_1.place(relx = 0.5, rely = 0.25, anchor = 'n')
    pygame.quit()
    root.mainloop()

