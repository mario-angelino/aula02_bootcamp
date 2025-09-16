

try:
    numero_01 = int(input("Digite o primeiro número: "))
    numero_02 = int(input("Digite o primeiro segundo: "))
    resultado = numero_01 / numero_02
    print(resultado)
except ZeroDivisionError:
    print("O segundo número não pode ser 0")
except ValueError:
    print("Digite somente números válidos")
