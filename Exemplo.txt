# Caso Base
1 : 2,3
2 : 1
3 : 2,1

# Matriz/Sistema
Linha(n): chance de N contar fofoca para cada M (coluna)
Coluna(m): chance de M receber fofoca de cada N (linha)
Descontando 0.1 (10%) de cada velinha:
       A    B    C
A   -1.00 +0.45 +0.45 = 0
B   +0.90 -1.00 +0.00 = 0
C   +0.45 +0.45 -1.00 = 0

0.9 de B: reduz 0.1 do esquecimento da memória
0.45:  chance de 50% * a -chance de 10% -> 50%*0.9
       (Pode ser 0.5 - 0.1 também = 0.4)

Realiza Gauss-Jacobi sob a matriz e os termos independentes
