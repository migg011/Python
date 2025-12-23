class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def latir():
        print("latiu papai")

class CachorroDiferenciado(Cachorro):
    def __init__(self, nome, idade, voa):
        super().__init__(nome, idade)
        self.voa = voa

    def latir():        
        print(f"o {self.nome}, que voa, latiu: RUF RUF")
    