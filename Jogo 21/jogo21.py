import random

def comprar_carta():
    return random.randint(1, 11)

def calcular_pontuacao(mao):
    soma = sum(mao)
    if soma > 21 and 11 in mao:
        mao[mao.index(11)] = 11 
        soma = sum(mao)
    return soma

def jogar_21():
    print("\nBem-vindo ao jogo 21!")
    jogador = [comprar_carta(), comprar_carta()]
    maquina = [comprar_carta(), comprar_carta()]
    
    while True:
        print(f"Sua mão: {jogador}, Pontuação: {calcular_pontuacao(jogador)}")
        if calcular_pontuacao(jogador) > 21:
            print("Você estourou! A máquina venceu.")
            return
        
        acao = input(f"""Deseja comprar mais uma carta? (s/n): """).lower()
        if acao == 's':
        
            jogador.append(comprar_carta())
        else:
         break
    
    while calcular_pontuacao(maquina) < 17:
        maquina.append(comprar_carta())

    print("Mão da máquina: {maquina}, Pontuação: {calcular_pontuacao(maquina)}")
    
    pontuacao_jogador = calcular_pontuacao(jogador)
    pontuacao_maquina = calcular_pontuacao(maquina)
    
    if pontuacao_maquina > 21 or pontuacao_jogador > pontuacao_maquina:
        print("Você venceu!")
    elif pontuacao_jogador < pontuacao_maquina:
        print("A máquina venceu!")
    else:
        print("Empate!")

if __name__ == "__main__":
    jogar_21()
