minhaLista = [34, 7, 22, 107, 89]

'''for i in range(len(minhaLista)):
    chave = minhaLista[i]
    j = i - 1
    while j >= 0 and chave < minhaLista[j]:
        minhaLista[j + 1] = minhaLista[j]
        j -= 1
    minhaLista[j + 1] = chave

print("Lista ordenada por inserção:", minhaLista)'''


lista = sorted(minhaLista)

print(lista)

#minhaLista.sort()

#print("A ordem é", minhaLista)