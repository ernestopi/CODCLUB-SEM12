# calculadora do amor
nome1 = input('Digite o nome da primeira pessoa: ').strip().lower()
nome2 = input('Digite o nome da segunda pessoa: ').strip().lower()
placar = 0
for carac in nome1 + nome2:
    if carac in 'aeiou':
        placar += 5
    if carac in 'amor':
        placar += 10

if  80 < placar <= 100:
    print('vocês serão almas gêmeas para sempre!')
elif 60 < placar <= 80:
    print('vocês serão mais que amigos!')
elif 40 < placar <= 60:
    print('vocês serão só amigos')
else:
    print('esqueça essa pessoa, nunca vai rolar!')