senha = input("Digite uma senha:  ")

tem_maiuscula = False
tem_minuscula = False
tem_numero = False
tem_especial = False

caracteres_especiais = "!@#$%¨&*()+=_-{}[]?/:><^~"

for caracter in senha:
    if caracter.isupper():
      tem_maiuscula = True
      
erros = []
if not tem_maiuscula:
    erros.append("Falta caracter maiusculo!")


if len(erros) == 0:
    print("Senha forte!")
else:
    print("Senha inválida!")
    print("Requisitos ausente")
    
    for erro in erros:
        print("- " + erro)