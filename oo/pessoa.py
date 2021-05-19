class Pessoa:
    def __init__(self, nome=None, idade=20):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return f' Olá'


if __name__ == '__main__':
    p = Pessoa('Rafa')
   # print(Pessoa.cumprimentar(p))
    print(p.cumprimentar())

    # usando __init__

    print(p.nome)
    print(p.idade)
    p.nome = 'Rafael'
    print(p.nome)
