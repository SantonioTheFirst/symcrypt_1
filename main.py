from math import log2 as log

def calculate_count_of_symbols(string):
    symbols = []
    counts = []
    for i in range(0,len(string)):
        if symbols.count(string[i]) == 0:
            symbols.append(string[i])
            counts.append(string.count(string[i]))
    print(symbols)
    return counts

def calculate_count_of_bigramms(string):
    bigramms = []
    counts = []
    for i in range(0,len(string)-1):
        if bigramms.count(string[i : i+2]) == 0:
            bigramms.append(string[i : i+2])
            counts.append(string.count(string[i : i+2]))
    # print(bigramms)
    return counts

def H(counts, n):
    count_of_gramms = len(counts)
    print(count_of_gramms)
    entropy = 0
    for i in range(0,count_of_gramms):
        entropy += (counts[i] / count_of_gramms) * log(counts[i] / count_of_gramms)
        # print(counts[i]/count_of_gramms)
    entropy = -entropy/n
    return entropy, log(38**n)

def remove_symbols(string):
    remove_symbols = [',', '.', '!', '\"', '-', ' ', ';', ':', '?', '–']
    for symbol in remove_symbols:
        string = string.replace(symbol, '')
    return string

string = "Выезжаю за город. Съезжаю в лес. Поляна. Выхожу из машины и дышу полной грудью. Вот она – чистота и свобода. На краю поляны большой муравейник. Раздеваюсь и иду к нему. Ступням холодно, а на душе спокойно. Я – часть природы. Только она и я. В мире больше ничего нет. Встаю на колени перед муравейником, осторожно кладу на ладонь одного муравья. Мы с ним чем-то похожи. Он работает, и я тоже. Кладу его на землю: -Беги, брат! И он бежит. К муравейнику, к своему дому. В этом то и вся разница между нами: он туда, а я оттуда. Надрачиваю хуй и засовываю его в чужой дом. Чувствую, как возмущенные жители разбегаются по моему телу. Путаются в волосах, кусают залупу а ничего сделать не могут. Мой хуй в их доме. Не в силах больше сдерживаться ложусь грудью на муравейник и обнимаю его. Я счастлив."
string = string.lower()
# string = remove_symbols(string)
print(string)

print(H(calculate_count_of_symbols(string), 1))
print(H(calculate_count_of_bigramms(string), 2))
