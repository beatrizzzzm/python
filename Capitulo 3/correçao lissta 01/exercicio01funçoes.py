def right_justify(palavra, tamanhoPalavra):
    espaco = " " * (70 - tamanhoPalavra)
    return espaco + palavra

palavra = str(input("digite uma palavra"))
tamanhoPalavra = len(palavra)
justificado = right_justify(palavra, tamanhoPalavra)

print(justificado)

