def simulaerCrescimento(populacao, taxa, limite):
    anos = 0
    while populacao <= limite:
        populacao = populacao * (1 + taxa)
        anos += 1
    return anos 
#main
p = float(input('População inicial: '))
t = float(input('Taxa (%): '))/100
l = float(input('Limite: '))

print(f'Anos= {simulaerCrescimento (p,t,l)}')
