import tkinter as tk
from PIL import Image, ImageTk
import time

class KronometreUygulamasi:
    def __init__(self, ana_pencere):

        self.ana_pencere = ana_pencere
        self.ana_pencere.title("Kronometre")

        self.calisiyor = False
        self.baslangic_zamani = 0
        self.gecen_zaman = 0

        self.zaman_etiketi = tk.Label(ana_pencere, text="00:00:00", font=("Helvetica", 48))
        self.zaman_etiketi.pack(pady=20)

        self.baslat_butonu = tk.Button(ana_pencere, text="Başlat", font=("Helvetica", 16), command=self.baslat)
        self.baslat_butonu.pack(side=tk.LEFT, padx=20)

        self.durdur_butonu = tk.Button(ana_pencere, text="Durdur", font=("Helvetica", 16), command=self.durdur)
        self.durdur_butonu.pack(side=tk.LEFT, padx=20)

        self.sifirla_butonu = tk.Button(ana_pencere, text="Sıfırla", font=("Helvetica", 16), command=self.sifirla)
        self.sifirla_butonu.pack(side=tk.LEFT, padx=20)

        self.tuval = tk.Canvas(ana_pencere, width=200, height=200)
        self.tuval.pack(pady=20)

        self.resim_yukle()

    def saati_guncelle(self):
        if self.calisiyor:

            self.gecen_zaman = time.time() - self.baslangic_zamani
            dakika = int(self.gecen_zaman // 60)
            saniye = int(self.gecen_zaman % 60)
            milisaniye = int((self.gecen_zaman - int(self.gecen_zaman)) * 100)

            self.zaman_etiketi.config(text=f"{dakika:02}:{saniye:02}:{milisaniye:02}")
            self.ana_pencere.after(50, self.saati_guncelle)

    def baslat(self):

        if not self.calisiyor:
            self.calisiyor = True
            self.baslangic_zamani = time.time() - self.gecen_zaman
            self.saati_guncelle()

    def durdur(self):

        if self.calisiyor:
            self.calisiyor = False

    def sifirla(self):

        self.calisiyor = False
        self.gecen_zaman = 0
        self.zaman_etiketi.config(text="00:00:00")

    def resim_yukle(self):
        try:
            resim = Image.open("kronometre_image.png")
            resim = resim.resize((200, 200), Image.ANTIALIAS)
            self.foto = ImageTk.PhotoImage(resim)
            self.tuval.create_image(0, 0, anchor=tk.NW, image=self.foto)

        except FileNotFoundError:
            print("Görüntü dosyası bulunamadı.")


ana_pencere = tk.Tk()
uygulama = KronometreUygulamasi(ana_pencere)
ana_pencere.mainloop()
