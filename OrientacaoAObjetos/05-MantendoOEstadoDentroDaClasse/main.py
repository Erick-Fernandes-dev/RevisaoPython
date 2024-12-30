class Camera:

    def __init__(self, nome, filmando=False):
        self.nome = nome
        self.filmando = filmando
    
    def filmar(self):

        if self.filmando:
            print(f"{self.nome} ja esta filmando")
            return


        print(f"{self.nome} esta filmando")
        self.filmando = True
    
    def parar_filmar(self):
        if not self.filmando:
            print(f"{self.nome} não está filmando")
            return
        
        print(f"{self.nome} parou de filmar")
        self.filmando = False
    
    def fotografar(self):
        if self.filmando:
            print(f"{self.nome} não pode fotografar enquanto esta filmando")
            return

        print(f"{self.nome} esta fotografando")


c1 = Camera("Canon")
c2 = Camera("Sony")


c1.filmar()
c1.filmar()
c1.fotografar()
c1.parar_filmar()
c1.parar_filmar()
c1.fotografar()

print("\n")

c2.filmar()
c2.filmar()
c2.fotografar()
c2.parar_filmar()
c2.parar_filmar()
c2.fotografar()
