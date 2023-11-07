#Run Length
#Have the function RunLength(str) take the str parameter being passed and return a compressed version of 
#the string using the Run-length encoding algorithm. This algorithm works by taking the occurrence of each repeating 
#character and outputting that number along with a single character of the repeating sequence. For example: "wwwggopp" would 
#return 3w2g1o2p. The string will not contain any numbers, punctuation, or symbols.

def RunLength(strParam):

  cont = {}

  listaParam = list(strParam)

  for caractere in listaParam:
    if caractere in cont:
      cont[caractere] +=1
    else:
      cont[caractere] = 1

  resultado = ""

  for caractere, quantidade in cont.items():
    resultado += str(quantidade)+caractere

  return resultado

# keep this function call here 
print(RunLength(input()))