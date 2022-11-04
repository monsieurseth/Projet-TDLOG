
def factorielle(n):
        fact = 1
        if n== 0:
            return f"{n}! = 1"
        else:
            for i in range(1,n+1):
                fact *=i
            return f"{n}! = {fact}"

resultat =factorielle(4)
print(resultat)

# Nous pouvons le faire de façon recursive aussi  


def factorielle(n):
    if n==0:
        return 1
    else:
        n = n*factorielle(n-1)
        return n

res = factorielle(4)

print(res)

