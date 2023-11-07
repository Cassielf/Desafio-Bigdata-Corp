strParam = "abracadabra"

def encontrar_palindromo_em_string(strParam):
   
    tamanho = len(strParam)

    for i in range(tamanho):
        for j in range(i + 2, tamanho + 1):
            substring = strParam[i:j]
            if substring == substring[::-1]:
                return substring

    return "none"