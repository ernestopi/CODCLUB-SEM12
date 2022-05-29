# desafio: modificando o programa para o usuário entrar com sua própria chave:
alfabeto = 'abcdefghijklmnopqrstuvwxyz'
# chave = 3

letra = input('Entre com uma letra para criptografar: ').strip().lower()
chave = int(input('Agora, entre com sua chave: ').strip())
posicao = alfabeto.find(letra)
nova_posicao = (posicao + chave) % 26

letra_criptografada = alfabeto[nova_posicao]
print('Sua letra criptografada é: {}'.format(letra_criptografada))