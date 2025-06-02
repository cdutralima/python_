def ler_vetor(nome_vetor: str) -> list[int]:
    vetor: list[int] = []
    print(f"\n--- Insira os elementos para o {nome_vetor} ---")
    print("(Digite um número negativo para finalizar a entrada deste vetor)")
    
    while True:
        try:
            entrada_str = input(f"Digite um número para o {nome_vetor}: ")
            elemento = int(entrada_str)
            
            if elemento < 0:
                break  
            vetor.append(elemento)
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")
    return vetor

def calcular_intersecao_de_vetores():
    vetor1: list[int] = []
    vetor2: list[int] = []
    intersecao: list[int] = []
    vetor1 = ler_vetor("Vetor 1")
    vetor2 = ler_vetor("Vetor 2")
    for elemento_do_vetor1 in vetor1:
        if elemento_do_vetor1 in vetor2:
            if elemento_do_vetor1 not in intersecao:
                intersecao.append(elemento_do_vetor1)
    
    
    print("\n--- Resultado Final ---")
    print(f"Vetor 1: {vetor1}")
    print(f"Vetor 2: {vetor2}")
    print(f"Interseção dos vetores: {intersecao}")
calcular_intersecao_de_vetores()