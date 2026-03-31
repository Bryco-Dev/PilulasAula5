def validarSenha(senha):
    if len(senha) < 8: 
# pass ignora função
# 'len' serve pra ler quanos numeros tem uma letra
        return 'Senha invalida, muito curto '
    temNumero = False
    temMaiuscula = False
    
    for c in senha:
        if c == ' ' :
            return "senha invalida, n pode conter espaço."
        
        if c >= '0' and c <= '9':
            temNumero = True
            
        if c >= 'A' and c <= 'Z':
            temMaiuscula = True
  
    if not temNumero:
        return 'Senha inválida, não tem número.'
        
    if not temMaiuscula:
        return 'Senha inválida, não tem maiuscula'
    return 'Senha válida'
  
#main
senha = input('Digite sua senha: ')
print(validarSenha(senha))