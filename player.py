# Libs
from tkinter import *
from PIL import Image, ImageTk
import pygame
from pygame import mixer
import os

# As imagens que utilizei foram para ilustrar os botões, você pode personalizar seu reprodutor do jeito que quiser.

# Colors
cinza = "#f0f3f5"
branca = "#feffff"
vermelho = "#7A0505"
black = '#000000'
preto = "#2e2d2c"
preto_2 = "#403d3d"
azul = "#4a88e8"

# Janela do aplicativo
j = Tk()
j.title('Music Player')
j.geometry('352x255')
j.configure(background = branca)
j.resizable(width=FALSE, height=FALSE)

# Frames
frame_esquerda = Frame(j, width = 150, height = 150, bg = vermelho)
frame_esquerda.grid(row = 0, column = 0, pady = 1, padx = 1, sticky = NSEW)

frame_direita = Frame(j, width = 250, height = 150, bg = black)
frame_direita.grid(row = 0, column = 1, pady = 1, padx = 0, sticky = NSEW)

frame_baixo = Frame(j, width = 404, height = 100, bg = vermelho)
frame_baixo.grid(row = 1, column = 0, columnspan = 3, pady = 1, padx = 0, sticky = NSEW)

# Configurando o frame esquerda
imagem_1 = Image.open("spotify.png")
imagem_1 = imagem_1.resize((130,130))
imagem_1 = ImageTk.PhotoImage(imagem_1)

label_logo  = Label(
    frame_esquerda,  
    height = 130,
    image = imagem_1,
    compound = LEFT,
    padx = 0,
    anchor = "nw",
    font = ('ivy 16 bold'),
    bg = vermelho,
    fg = vermelho)
label_logo.place(x = 20, y = 20)

# Function para reproduzir música
def  play_musica():
    rodando = listbox.get(ACTIVE)
    label_rodando['text'] = rodando
    mixer.music.load(rodando)
    mixer.music.play()

# Pausar Música
def  pause_musica():
    mixer.music.pause()

# Continuar Música
def despausar_musica():
    mixer.music.unpause()

# Parar Música
def stop_music():
    mixer.music.stop()

# Proxima Música
def proxima_musica():
    tocando = label_rodando['text']
    index = musicas.index(tocando)
    novo_index = index + 1
    tocando = musicas[novo_index]

    mixer.music.load(tocando)
    mixer.music.play()

    # Deletando os elementos na Playlist
    listbox.delete(0, END)

    mostrar()

    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    label_rodando['text'] = tocando

# Música Anterior
def musica_anterior():
    tocando = label_rodando['text']
    index = musicas.index(tocando)
    novo_index = index -1
    tocando = musicas[novo_index]

    mixer.music.load(tocando)
    mixer.music.play()

    # Deletando os elementos na Playlist
    listbox.delete(0, END)

    mostrar()

    listbox.select_set(novo_index)
    listbox.config(selectmode=SINGLE)
    label_rodando['text'] = tocando
    

# Configurando o frame direita
listbox = Listbox(
    frame_direita,
    width=22,
    height=10,
    selectmode=SINGLE,
    font = ('arial 9 bold'),
    bg=black,
    fg=branca)
listbox.grid(row=0, column=0)

s = Scrollbar(frame_direita)
s.grid(row=0, column=1, sticky=NSEW)

listbox.config(yscrollcommand=s.set)
s.config(command=listbox.yview)

# Configurando o frame baixo -------------------------------------------
label_rodando  = Label(
    frame_baixo,
    text = 'CHOOSE MUSIC FROM THE LIST',
    width=44,
    justify=LEFT,
    anchor = "nw",
    font = ('ivy 10 bold'),
    bg = black,
    fg = branca)
label_rodando.place(x = 0, y = 1)

imagem_2 = Image.open("retroceder.png")
imagem_2 = imagem_2.resize((30,30))
imagem_2 = ImageTk.PhotoImage(imagem_2)
botao_anterior = Button(
    frame_baixo,
    command=musica_anterior,
    width=40,
    height=40,
    image=imagem_2,
    font = ('ivy 10 bold'),
    relief=RAISED,
    overrelief=RIDGE,
    bg =vermelho,
    fg = black)
botao_anterior.place(x = 38, y = 35)

imagem_3 = Image.open("play.png")
imagem_3 = imagem_3.resize((30,30))
imagem_3 = ImageTk.PhotoImage(imagem_3)
botao_play = Button(
    frame_baixo,
    command= play_musica,
    width=40,
    height=40,
    image=imagem_3,
    font = ('ivy 10 bold'),
    relief=RAISED,
    overrelief=RIDGE,
    bg =vermelho,
    fg = black)
botao_play.place(x = 84, y = 35)

imagem_4 = Image.open("fast.png")
imagem_4 = imagem_4.resize((30,30))
imagem_4 = ImageTk.PhotoImage(imagem_4)
botao_next = Button(
    frame_baixo,
    command=proxima_musica, 
    width=40,
    height=40,
    image=imagem_4,
    font = ('ivy 10 bold'),
    relief=RAISED,
    overrelief=RIDGE,
    bg =vermelho,
    fg = black)
botao_next.place(x = 130, y = 35)

imagem_5 = Image.open("pause.png")
imagem_5 = imagem_5.resize((30,30))
imagem_5 = ImageTk.PhotoImage(imagem_5)
botao_pause = Button(
    frame_baixo,
    command=pause_musica,
    width=40,
    height=40,
    image=imagem_5,
    font = ('ivy 10 bold'),
    relief=RAISED,
    overrelief=RIDGE,
    bg =vermelho,
    fg = black)
botao_pause.place(x = 176, y = 35)

imagem_6 = Image.open("end.png")
imagem_6 = imagem_6.resize((30,30))
imagem_6 = ImageTk.PhotoImage(imagem_6)
botao_continuar = Button(
    frame_baixo,
    command=despausar_musica,
    width=40,
    height=40,
    image=imagem_6,
    font = ('ivy 10 bold'),
    relief=RAISED,
    overrelief=RIDGE,
    bg =vermelho,
    fg = black)
botao_continuar.place(x = 222, y = 35)

imagem_7 = Image.open("stop.png")
imagem_7 = imagem_7.resize((30,30))
imagem_7 = ImageTk.PhotoImage(imagem_7)
botao_stop = Button(
    frame_baixo,
    command=stop_music,
    width=40,
    height=40,
    image=imagem_7,
    font = ('ivy 10 bold'),
    relief=RAISED, overrelief=RIDGE,
    bg =vermelho,
    fg = black)
botao_stop.place(x = 268, y = 35)

# Aqui você deve inserir o caminho da pasta onde tem as músicas que você quer que tenha no seu reprodutor
os.chdir(r"C:\Users\rycha\OneDrive\Programação\Music Player\Musicas")
musicas = os.listdir()

def mostrar():
    for i in musicas:
        listbox.insert(END, i)

mostrar()

# Inicializando o Mixer
mixer.init()

j.mainloop()
