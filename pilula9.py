def calcular_media(prod, quali, pont):
    return (prod + quali + pont)/3

def classificar(Media):
    if Media >= 8:
        return 'Excelente'
    if Media >= 6:
        return 'Bom'
    else:
        return'Crítico'
    
def avaliar_funcionarios():
    total = 0
    exc = 0
    bom = 0
    cri = 0
    melhorNome = ''
    melhorMedia = -1
    while True:
        nome = input ('Now: ')
        if nome == 'fim':
            break
        prod = float(input('Produtividade: '))
        qual = float(input('Qualidade:'  ))
        pont = float(input('Pontualidade: '))
        
        media = calcular_media(prod, qual, pont)
        categoria = classificar (media)
        print(f"{nome}, média {media}, {categoria} ")
        
        total += 1
        if categoria == 'Excelente':
            exc += 1
        elif categoria == 'Bom':
            bom += 1
        else:
            crit +=1
        if media > melhorMedia:
            melhorMedia = media
            melhorNome = nome
    if total == 0:
        print('Nada para calcular')
        return
    
    
    print('-'*50)  
    print('Relatório')
    print('-'+50)
    print(f'Total de func: {total}')
    print(f'Execelente: {exc}')
    print(f'Bom: {bom}')
    print(f'Crítico {crit}')
    print(f'Melhor func: {melhorNome}')
    print(f'Melhor func media: {melhorMedia}')
    
avaliar_funcionarios()