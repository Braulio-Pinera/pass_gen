import sys
from generator.password_generator import generate_password

def main():

    if len(sys.argv) != 2 :
        print("Formato: python main.py [longitud]")
        return 1

    try:
        length = int(sys.argv[1])
    except:
        print("Error: la longitud debe ser un número entero")
        return 2

    if length < 4:
        print("Error: la longitud debe ser de 4 caracteres por lo menos")
        return 3

    password = generate_password(length)

    print("Contraseña generada: ", password)

if __name__ == "__main__":
    main()