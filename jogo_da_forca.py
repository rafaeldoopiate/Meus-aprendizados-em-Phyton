import random

def escolher_palavra():
    palavras = ['python', 'engenharia', 'software', 'computador', 'programa', 'desenvolvedor', 'tecnologia']
    return random.choice(palavras).upper()

def jogar():
    palavra = escolher_palavra()
    letras_acertadas = ['_' for _ in palavra]
    letras_usadas = set()
    tentativas_max = 6
    tentativas_restantes = tentativas_max

    print("=== JOGO DA FORCA ===")

    while tentativas_restantes > 0 and '_' in letras_acertadas:
        print(f"\nPalavra: {' '.join(letras_acertadas)}")
        print(f"Letras usadas: {', '.join(sorted(letras_usadas)) if letras_usadas else 'Nenhuma'}")
        print(f"Tentativas restantes: {tentativas_restantes}")

        palpite = input('Digite uma letra: ').upper()

        if not palpite.isalpha() or len(palpite) != 1:
            print("Digite apenas uma letra válida.")
            continue

        if palpite in letras_usadas:
            print("Você já tentou essa letra. Tente outra.")
            continue

        letras_usadas.add(palpite)

        if palpite in palavra:
            print(f"Boa! A letra '{palpite}' está na palavra.")
            for i, letra in enumerate(palavra):
                if letra == palpite:
                    letras_acertadas[i] = palpite
        else:
            print(f"Ops! A letra '{palpite}' não está na palavra.")
            tentativas_restantes -= 1

    if '_' not in letras_acertadas:
        print(f"\nPARABÉNS! Você acertou a palavra: {palavra}")
    else:
        print(f"\nVocê perdeu! A palavra era: {palavra}")

if __name__ == '__main__':
    jogar()
