# есть зашифрованное сообщение

secret_message = [
    'квевтфпп6щ3стмзалтнмаршгб5длгуча',
    'дьсеы6лц2бане4т64ь4б3ущея6втщл6б',
    'т3пплвце1н3и2кд4лы12чф1ап3бкычаь',
    'ьд5фму3ежородт9г686буиимыкучшсал',
    'бсц59мегщ2лятьаьгенедыв9фк9ехб1а',
]

# ключ к расшифровке:
#   первое слово - 4-я буква
#   второе слово - буквы с 10 по 13, включительно
#   третье слово - буквы с 6 по 15, включительно, через одну
#   четвертое слово - буквы с 8 по 13, включительно, в обратном порядке
#   пятое слово - буквы с 17 по 21, включительно, в обратном порядке
#
# Требуется задать конкретные индексы, например secret_message[3][12:23:4]
# Если нужны вычисления и разные пробы - делайте это в консоли пайтона, тут нужен только результат

word_1 = secret_message[0][3]
word_2 = secret_message[1][9] + secret_message[1][10] + secret_message[1][11] + secret_message[1][12]
word_3 = secret_message[2][5] + secret_message[2][7] + secret_message[2][9] + secret_message[2][11] + secret_message[2][13]
word_4 = secret_message[3][12] + secret_message[3][11] + secret_message[3][10] + secret_message[3][9] + secret_message[3][8] + secret_message[3][7]
word_5 = secret_message[4][20] + secret_message[4][19] + secret_message[4][18] + secret_message[4][17]  + secret_message[4][16]
print(word_1, word_2, word_3, word_4, word_5)