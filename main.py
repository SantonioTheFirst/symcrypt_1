from math import log2

def calculate_count_of_symbols(string):
    symbols = []
    counts = []
    count_of_symbols = len(string)
    for i in range(0,count_of_symbols):
        if symbols.count(string[i]) == 0:
            symbols.append(string[i])
            counts.append(string.count(string[i]))
    # print(len(symbols))
    return counts, count_of_symbols

def calculate_count_of_bigramms(string):
    bigramms = []
    counts = []
    count_of_bigramms = len(string) - 1
    for i in range(0, count_of_bigramms):
        if bigramms.count(string[i : i + 2]) == 0:
            bigramms.append(string[i : i + 2])
            counts.append(string.count(string[i : i + 2]))
    # print(len(bigramms))
    return counts, count_of_bigramms

def Hn(counts, count_of_gramms, n):
    print('Количество грамм: ', count_of_gramms)
    entropy = 0
    # print(entropy)
    probabilities = []
    for value in counts:
        probabilities.append(value / count_of_gramms)
    for probability in probabilities:
        entropy -= (probability * log2(probability))
        print(probability, log2(probability), entropy)
    return entropy / n, log2(38**n)

def remove_symbols(string):
    remove_symbols = [',', '.', '!', '\"', '-', ' ', ';', ':', '?', '–']
    for symbol in remove_symbols:
        string = string.replace(symbol, '')
    return string

string = """Выезжаю за город. Съезжаю в лес. Поляна. Выхожу из машины и дышу полной грудью. Вот она – чистота и свобода. На краю поляны большой муравейник. Раздеваюсь и иду к нему. Ступням холодно, а на душе спокойно. Я – часть природы. Только она и я. В мире больше ничего нет. Встаю на колени перед муравейником, осторожно кладу на ладонь одного муравья. Мы с ним чем-то похожи. Он работает, и я тоже. Кладу его на землю:
- Беги брат!
И он бежит. К муравейнику, к своему дому. В этом то и вся разница между нами: он туда, а я оттуда. Надрачиваю хуй и засовываю его в чужой дом. Чувствую, как возмущенные жители разбегаются по моему телу. Путаются в волосах, кусают залупу а ничего сделать не могут. Мой хуй в их доме. Не в силах больше сдерживаться ложусь грудью на муравейник и обнимаю его. Я счастлив."""
string = string.lower()
# string = remove_symbols(string)
string = string.replace('\n', '')
# print(string)

# counts, count_of_gramms = calculate_count_of_symbols(string)
# print(len(counts))
counts, count_of_gramms = calculate_count_of_bigramms(string)
print(Hn(counts, count_of_gramms, 2))
