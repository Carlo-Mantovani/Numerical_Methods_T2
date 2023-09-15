import random

# Função para criar o grafo de amizades com base no arquivo de entrada
def criar_grafo_amizades(arquivo):
    grafo = {}
    with open(arquivo, 'r') as f:
        for linha in f:
            partes = linha.strip().split(':')
            velhinha = int(partes[0].strip())
            amigas = [int(amiga) for amiga in partes[1].strip().split()]
            grafo[velhinha] = amigas
    return grafo

# Função para simular o processo de migração de informações
def simular_migracao_informacoes(grafo):
    num_velhinhas = len(grafo)
    fofocas = [0] * (num_velhinhas + 1)

    for velhinha in grafo:
        for amiga in grafo[velhinha]:
            if random.random() <= 0.1:
                continue  # A velhinha esqueceu de contar a fofoca
            fofocas[amiga] += 1

    return fofocas

# Função para encontrar a velhinha que recebeu mais fofocas
def encontrar_velhinha_mais_fofocas(fofocas):
    max_fofocas = max(fofocas)
    velhinha = fofocas.index(max_fofocas)
    return velhinha, max_fofocas

# Função principal
def main():
    arquivo = "exemplo.txt"  # Substitua pelo nome do seu arquivo de entrada
    grafo_amizades = criar_grafo_amizades(arquivo)
    fofocas = simular_migracao_informacoes(grafo_amizades)
    velhinha_mais_fofocas, num_fofocas = encontrar_velhinha_mais_fofocas(fofocas)

    print(f"A velhinha que recebeu mais fofocas foi a número {velhinha_mais_fofocas} com {num_fofocas} fofocas.")

if __name__ == "__main__":
    main()
