# Codigo do twitter, com limitaçao de 140 6caracteres 
# vamos lá

# Primeiro ele pede um comentario atravez do input, ou seja uma string
texto = input("Escreva aqui seu comentario: ") 

# O len lê a quantidade de caracteres e armazena em uma variavel 
quantidade_caracteres = len(texto)

# Ele usa o if para saber se o comentario armazenado em quantidade_caracteres é
# menor ou igual a 140 e depois verifica se ele é maior que zero,
# se ele for, o comentario é postado.
if quantidade_caracteres <= 140 and quantidade_caracteres > 0:
    print("TWEET")
    print(f'Comentário:\n #{texto}#')
    print("Seu comentario foi postado!")

# Se o comentario for igual a zero caracteres ele não será postado.
elif quantidade_caracteres == 0:
    print("MUTE")
    print("Quantidade de caracteres insuficiente!")

# Caso não seja nenhuma das opções acima, o comentario não será postado.
else:
    print("MUTE")
    print(f"""Você digitou {quantidade_caracteres} caracteres,
diminua a quantidade de caracteres para que o comentario
seja publicado.""") 