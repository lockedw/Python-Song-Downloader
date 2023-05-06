from pytube import YouTube
import customtkinter
import tkinter
import os 
# https://www.youtube.com/watch?v=pdYJtRBPlTw
# Mp3 Fonksiyon
def Download():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink)
        video = ytObject.streams.filter(only_audio=True).first()
        destination = '.'
        out_file = video.download(output_path=destination)
        base, ext = os.path.split(out_file)
        new_file = video.title + '.mp3'
        os.rename(out_file,new_file)
        finishLabel.configure(text="Mp3 Başarılı Bir Şekilde İndirildi")
        title.configure(text=video.title,text_color="white")
    except:
        finishLabel.configure(text="Programda Bir Hata Oluştu", text_color="red")    


# Uygulama
app = customtkinter.CTk()
app.geometry("720x480")
app.title("Youtube Mp3 İndirici")

# Uygulama Tema
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")


# Uygulama Başlık
title = customtkinter.CTkLabel(app, text="Youtube Mp3 İndirici")
title.pack(padx=10,pady=10)

# Link Girme
url_var = customtkinter.StringVar()
link = customtkinter.CTkEntry(app,width=400)
link.pack(padx=10,pady=10)

# Bildirim
finishLabel = customtkinter.CTkLabel(app,text="")
finishLabel.pack()

# İndirme Butonu
button = customtkinter.CTkButton(app,text="İndir!",command=Download)
button.pack(padx=10,pady=10)

# Uygulama Başlat
app.mainloop()