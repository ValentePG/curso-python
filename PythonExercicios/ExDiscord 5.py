p1, pw = input('Digite o nome e o poder de ataque do personagem principal: ').split()
p2, l, pd, s = input(
    'Digite o nome, os pontos de vida, defesa e [s] se tiver um escudo ou [n] se não tiver: ').split()

l = float(l)
pw = int(pw)
pd = int(pd)

if pw > pd and s == "n":
    dmg = pw - pd
    l = l - dmg
    print(f'O {p2} levou {dmg} de dano')
elif pw > pd and s == "s":
    dmg = pw - pd
    esc = dmg / 2
    l = l - esc
    print(f'O {p2} levou {esc} de dano')
else:
    print(f'O {p2} não levou dano')
print(f'{p2} agora tem {l} de vida ')
