import math

def calcular_estatisticas(nome_turma: str, notas: list[float]):
    print(f"\n--- Estatísticas para {nome_turma} ---")
    
    if not notas:
        print("A lista de notas está vazia. Não é possível calcular as estatísticas.")
        return   
    max_nota = max(notas)
    print(f"Nota Máxima: {max_nota:.2f}") 
    min_nota = min(notas)
    print(f"Nota Mínima: {min_nota:.2f}")   
    num_notas = len(notas)
    soma_notas = sum(notas)
    media = soma_notas / num_notas
    print(f"Média das Notas: {media:.2f}")  
    soma_diferencas_quadradas = 0
    for nota in notas:
        soma_diferencas_quadradas += (nota - media) ** 2
    
    
    variancia = soma_diferencas_quadradas / num_notas
    
    
    desvio_padrao = math.sqrt(variancia)
    print(f"Desvio Padrão das Notas: {desvio_padrao:.2f}")


turma1 = [1.1, 7.5, 0.8, 1.8, 1.5, 1.9, 10.0, 10.0, 9.3, 10.0, 7.7, 0.6, 0.5, 8.7, 5.6, 7.0, 8.3, 7.0, 9.1, 7.4, 8.1, 7.0, 6.3, 0.6, 7.4, 2.8, 5.0, 1.4, 1.5, 0.5, 8.3, 7.0, 2.9, 7.6, 10.0, 3.3, 1.9, 5.1, 7.0]
turma2 = [10.0, 8.2, 8.7, 5.5, 6.8, 8.6, 8.5, 6.1, 6.2, 8.5, 7.7, 10.0, 10.0, 6.1, 8.4, 5.4, 5.6, 9.8, 2.1, 8.5, 3.3, 8.7, 8.5, 9.1, 9.7]
calcular_estatisticas("Turma 1", turma1)
calcular_estatisticas("Turma 2", turma2)