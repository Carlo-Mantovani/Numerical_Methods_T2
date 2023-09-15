import numpy as np

#TODO: verificar convergencia do metodo de gauss-jacobi aplicando coeficientes as equacoes e verificando proximidade com termos independentes

def verifica_convergencia_gauss_jacobi(matriz, coeficientes, termos_independentes):
    n = len(matriz)
    x_proximo = np.zeros(n)
    # creates equations and apply coeficients to equations to verify convergence by checking proximity to independent terms
    for i in range(n):
        soma = 0
        for j in range(n):
            if j != i:
                soma += matriz[i, j] * coeficientes[j]
        x_proximo[i] = (termos_independentes[i] - soma) / matriz[i, i]

    if np.allclose(x_proximo, coeficientes, rtol=1e-6, atol=1e-6):
        return False
    return True

def gauss_jacobi(matriz_coeficientes, vetor_termos_independentes, max_iteracoes=100, tolerancia=1e-6):
    n = len(matriz_coeficientes)
    #chute inicial 2, 3, 2, 6 = np.array([2, 3, 2, 6])
    x_atual = np.ones(n)
    x_proximo = np.zeros(n)

    for iteracao in range(max_iteracoes):
        # alcance do numero de equacoes
        for i in range(n):
            soma = 0
            for j in range(n):
                if j != i:
                    soma += matriz_coeficientes[i, j] * x_atual[j]
            x_proximo[i] = (vetor_termos_independentes[i] - soma) / matriz_coeficientes[i, i]
        x_atual[:] = x_proximo
        #apply coeficients to equations to verify convergence
        if not verifica_convergencia_gauss_jacobi(matriz_coeficientes, x_atual, vetor_termos_independentes):
            return x_atual, iteracao + 1
        
      
        print (x_proximo)

    return None, max_iteracoes  # Retorna None se a convergência não for alcançada

# Exemplo de uso
if __name__ == "__main__":
    #matriz_coeficientes = np.array([[6, 2, 3, -1],
    #                                [4, 2, 4, 7],
    #                                [8, 3, 5 , -9],
    #                                [-4, 2, 5, 6]])
    matriz_coeficientes = np.array([[9,6,5],[6,8,4],[2,1,7]])

    vetor_termos_independentes = np.array([-1,6,5])


    solucao, iteracoes = gauss_jacobi(matriz_coeficientes, vetor_termos_independentes)
    if solucao is not None:
        print("Solução encontrada após", iteracoes, "iterações:")
        print(solucao)
    else:
        print("O método de Gauss-Jacobi não convergiu após", iteracoes, "iterações.")
    