#!C:\Users\felipe\AppData\Local\Programs\Python\Python37-32\python

class HtmlToStringMixin:
    def __str__(self):
        html = super().__str__() \
            .replace('(', '<strong>(') \
            .replace(')', ')</strong>')
        return f'<span>{html}</span>'


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return self.nome

class Animal:
    def __init__(self, nome, pet=True):
        self.nome = nome
        self.pet = pet

    def __str__(self):
        return self.nome + ' (pet)' if self.pet else ''

class PessoaHtml(HtmlToStringMixin, Pessoa):
    pass

class AnimalHtml(HtmlToStringMixin, Animal):
    pass

if __name__ == "__main__":
    felipe = Pessoa('Felipe Romao')
    marina = PessoaHtml('Marina Lacerda')
    print(felipe)
    print(marina)

    dog = Animal('Mike', True)
    toto = AnimalHtml('Toto')
    print(dog)
    print(toto)