import tkinter, tkVideoPlayer

Tela = tkinter.Tk()
Tela.title("MiniPlayer")
Tela.geometry("300x300")
Tela.config(background="black")
Tela.resizable(0,0)



def play():
    video.play()

def pause():
    video.pause()


btPLay = tkinter.Button(Tela,text='play', relief='flat', width=10, borderwidth=2, command=play).grid(row=1, column=0, padx=10, pady=10)
btPause = tkinter.Button(Tela,text='pause', relief='flat', width=10, borderwidth=2, command=pause).grid(row=1, column=1, padx=10, pady=10)

video = tkVideoPlayer.TkinterVideo(Tela,scaled=True)
video.load('YOUR-VIDEO.mp4')
video.grid(row=0, columnspan=3, padx=75, pady=50, sticky="we" )

Tela.mainloop()
