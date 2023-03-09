def count_combinations(x):
    if (1<=x and x<=100):
        # Inicialização do vetor de DP com zero
        dp = [0] * (x + 1)
        
        # Inicialização da base da recursão
        dp[0] = 1
        
        # Preenchimento do vetor de DP
        for i in range(1, x + 1):
            #altere o vetor com os numeros que deseja usar na combinação 
            for j in [1, 2, 3,4]:
                if i >= j:
                    dp[i] += dp[i-j]
                    
        # Retorna o resultado
        return dp[x]
    else :
        print("Valor invalido, apenas valores maiores que 0 e menores  ou iguais a 100")

while True:
    try:
        num = int(input())
        func =count_combinations(num)
        print(func)
    except:
        break

