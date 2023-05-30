def destroy_castle(test_cases):
    for _ in range(test_cases):
        n = int(input())
        tiro = []
        for _ in range(n):
            x, y = map(int, input().split())
            tiro.append((x, y))
        k = int(input())
        r = int(input())

        dp = [-1] * (k + 1)
        dp[0] = 0

        for pro in range(n):
            patual = tiro[pro][1]
            vatual = tiro[pro][0]
            for i in range(1, k + 1):
                if dp[i] != -1:
                    if i >= patual:
                        atual = dp[i - patual]
                        dp[i - patual] = max(atual, dp[i] + vatual)
            if patual <= k:
                atual = dp[k - patual]
                dp[k - patual] = max(atual, vatual)

        ok = False
        for i in range(k):
            if dp[i] >= r:
                ok = True
                break

        if ok:
            print("Missao completada com sucesso")
        else:
            print("Falha na missao")


numeros = int(input())


destroy_castle(numeros)
