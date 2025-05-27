precocapalivro = 24.95
precocapalivrodesconto = precocapalivro - (precocapalivro * 0.40)
custodpfreteprimeiroexemplar = precocapalivrodesconto + 3.00
custodefreteparaorestanteexemplar = precocapalivrodesconto + 0.75
custototalatacado = custodpfreteprimeiroexemplar  + (custodefreteparaorestanteexemplar* 59)

print("o preco total de atacado para os exemplares e de: ", custototalatacado)