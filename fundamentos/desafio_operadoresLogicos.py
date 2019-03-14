# Se os dois trabalhos derem certo:
# vai comprar a TV de 50 pol
# e tomar sorvete
# e ser menos saudavel

# Se somente um dos dois trabalhos derem certo,
# vai comprar uma tv de 42 pol
# vai tomar sorvete
# e ser menos saudavel

# se nenhum dos dois trabalhos derem certo,
# não vai comprar nenhuma TV
# nem tomar sorvete
# e ser mais saudavel

trabalho_terca = False
trabalho_quinta = False

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print("Tv50={} Tv32={} Sorvete={} Saudavel={}"
      .format(tv_50, tv_32, sorvete, mais_saudavel))
