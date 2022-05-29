# desafio: cifra melhorada
alfabeto = 'qwertyuiopadsfghjklzcvxbnm'

msg = input('Por favor, entre com a mensagem a ser criptografada: ').strip().lower()
msg_criptografada = ''
chave = int(input('Agora, entre com a chave: ').strip())

for carac in msg:
    if carac in alfabeto:
        posicao = alfabeto.find(carac)
        nova_posicao = (posicao + chave) % 26
        msg_criptografada = msg_criptografada + alfabeto[nova_posicao]
        chave += 1
    else:
        msg_criptografada = msg_criptografada + carac

print('Sua mensagem criptografada é: {}'.format(msg_criptografada))