import turtle
t = turtle.Turtle()
import turtle  # importa o módulo de desenho

# Classe geral para qualquer figura
class Figura:
    def __init__(self, cor, tamanho, x, y):
        self.cor = cor
        self.tamanho = tamanho
        self.x = x
        self.y = y
        self.t = turtle.Turtle()  # cria a tartaruguinha

    def posicionar(self):
        """Leva a tartaruga para a posição antes de desenhar"""
        self.t.penup()
        self.t.goto(self.x, self.y)
        self.t.pendown()
        self.t.color(self.cor)

# Quadrado herda de Figura
class Quadrado(Figura):
    def desenhar(self):
        self.posicionar()
        for _ in range(4):  # repete 4 vezes
            self.t.forward(self.tamanho)
            self.t.right(90)


# Triângulo herda de Figura
class Triangulo(Figura):
    def desenhar(self):
        self.posicionar()
        for _ in range(3):  # repete 3 vezes
            self.t.forward(self.tamanho)
            self.t.left(120)


# Círculo herda de Figura
class Circulo(Figura):
    def desenhar(self):
        self.posicionar()
        self.t.circle(self.tamanho)


# Função principal do programa
def main():
    # Fundo rosa claro
    turtle.bgcolor("lightpink")

    # Criando cada forma
    q = Quadrado("red", 100, -200, 100)
    t = Triangulo("green", 100, 0, 100)
    c = Circulo("blue", 50, 200, 100)

    # Desenhando cada uma
    q.desenhar()
    t.desenhar()
    c.desenhar()

    # Finaliza o desenho
    turtle.done()

if __name__ == "__main__":
    main()

