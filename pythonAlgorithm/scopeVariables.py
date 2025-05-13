num1, num2, num3 = 1.5, 2.5, 3.5

def ler_numeros():
    print(f"Number 1 = {num1:.2f}, Number 2 = {num2:.2f}, Number 3 = {num2:.2f}")
    return

def calcula_soma():
    soma = num1 + num2 + num3
    print(f"Soma = {soma:.2f}")
    return

def calcula_media():
    media = (num1 + num2 + num3) / 3
    print(f"Media = {media:.2f}")

if __name__ == "__main__":
    print("Lendo Numeros:")
    ler_numeros()
    
    print("\nCalcula Soma:")
    calcula_soma()
    
    print("\nCalcula media:")
    calcula_media()