import re
from math import log2
from datetime import datetime
import numpy as np
import pandas as pd

file = open('karenina_result.txt', 'r', encoding='utf8')
source = file.read()
file.close()

def filter(source):
    source = source.lower()
    look_for = r"[а-я]+"
    allresults = re.findall(look_for, source)
    string =''
    for i in range(0, len(allresults)):
        if i == len(allresults) - 1:
            string += allresults[i]
        else:
            string += allresults[i] + ' '
    return string

def calculate_count_of_symbols(string):
    symbols = {}
    count_of_symbols = len(string)
    for i in range(0,count_of_symbols):
        symbol = string[i]
        if symbols.get(symbol, 0) == 0:
            symbols[symbol] = string.count(symbol)
    print('Всего символов:', count_of_symbols)
    print('Уникальных:', len(symbols))
    return symbols, count_of_symbols

def calculate_count_of_bigramms_without_collisions(string):
    bigramms = {}
    count_of_bigramms = len(string) / 2
    for i in range(0, len(string), 2):
        bigramm = string[i : i + 2]
        if bigramms.get(bigramm, 0) == 0:
            bigramms[bigramm] = string.count(bigramm)
    print('Всего биграмм:', count_of_bigramms)
    print('Уникальных:', len(bigramms))
    return bigramms, len(string) - 1

def get_bigramms_count(string, index, bigramm):
    length_of_string = len(string)
    count = 0
    for i in range(index, length_of_string - 1):
        if string[i : i + 2] == bigramm:
            count += 1
    return count

def calculate_count_of_bigramms_with_collisions(string):
    bigramms = {}
    count_of_bigramms = len(string) - 1
    temp_bigramms = []
    for i in range(0, count_of_bigramms):
        temp_bigramms.append(string[i : i + 2])
    for i in range(0, count_of_bigramms):
        bigramm = string[i : i + 2]
        if bigramms.get(bigramm, 0) == 0:
            # start = datetime.now()
            bigramms[bigramm] = temp_bigramms.count(bigramm)
            # print('Время на добавление количества нового элемента', bigramm, str(datetime.now() - start))
    print('Биграмм всего:', count_of_bigramms)
    print('Уникальных:', len(bigramms))
    return bigramms, len(string) - 1

def sort_dict(unsorted_dict):
    sorted_dict = {}
    for i in sorted(unsorted_dict, key = unsorted_dict.get, reverse=True):
        sorted_dict[i] = unsorted_dict[i]
    return sorted_dict

def Hn(dictionary, count_of_gramms, n):
    entropy = 0
    # print(entropy)
    probabilities = []
    for key in dictionary:
        probabilities.append(dictionary[key] / count_of_gramms)
    for probability in probabilities:
        entropy -= (probability * log2(probability))
        # print(probability, log2(probability), entropy)
    return 'Энтропия фактическая и максимальная:', entropy / n, log2(len(dictionary)**n)

def compare(a, b):
    result_different_count = {}
    result_new_elements = {}
    if len(a) > len(b):
        for key in a:
            if a.get(key ,0) != 0 and b.get(key, 0) == 0:
                result_new_elements[key] = a[key]
            elif a.get(key, 0) == 0 and b.get(key, 0) != 0:
                result_new_elements[key] = b[key]
            elif a.get(key, 0) != 0 and b.get(key, 0) != 0:
                if a[key] > b[key]:
                    result_different_count[key] = a[key] - b[key]
            # else:
                # print('Error1')
    elif len(b) > len(a):
        for key in b:
            if a.get(key ,0) != 0 and b.get(key, 0) == 0:
                result_new_elements[key] = a[key]
            elif a.get(key, 0) == 0 and b.get(key, 0) != 0:
                result_new_elements[key] = b[key]
            elif a.get(key, 0) != 0 and b.get(key, 0) != 0:
                if b[key] > a[key]:
                    result_different_count[key] = b[key] - a[key]
            # else:
                # print('Error2')
    else:
        for key in a:
            if a.get(key ,0) != 0 and b.get(key, 0) == 0:
                result_new_elements[key] = a[key]
            elif a.get(key, 0) == 0 and b.get(key, 0) != 0:
                result_new_elements[key] = b[key]
            elif a.get(key, 0) != 0 and b.get(key, 0) != 0:
                if a[key] > b[key]:
                    result_different_count[key] = a[key] - b[key]
                elif b[key] > a[key]:
                    result_different_count[key] = b[key] - a[key]
            # else:
                # print('Error3')
    return result_different_count, result_new_elements

def get_bigramms_matrix(bigramms_d): #, flag):
    a = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ы', 'ь', 'э', 'ю', 'я', ' ']
    dict = {'' : a, 'а' : [], 'б' : [], 'в' : [], 'г' : [], 'д' : [], 'е' : [], 'ж' : [], 'з' : [], 'и' : [], 'й' : [], 'к' : [], 'л' : [], 'м' : [], 'н' : [], 'о' : [], 'п' : [], 'р' : [], 'с' : [], 'т' : [], 'у' : [], 'ф' : [], 'х' : [], 'ц' : [], 'ч' : [], 'ш' : [], 'щ' : [], 'ы' : [], 'ь' : [], 'э' : [], 'ю' : [], 'я' : [], ' ' : []}
    for i in range(0, len(a)):
        row = []
        # row.append(a[i])
        for j in range(0, len(a)):
            if a[i] + a[j] in bigramms_d.keys():
                row.append(bigramms_d[a[i] + a[j]])
            else:
                row.append(0)
        dict[a[i]] = row
    df = pd.DataFrame.from_dict(dict, orient='index')
    return df

def do_all(string):
    start = datetime.now()
    print('\nСимволы:')
    symbols_unsorted, count_of_symbols = calculate_count_of_symbols(string)
    symbols_sorted = sort_dict(symbols_unsorted)
    print(symbols_sorted)
    print(Hn(symbols_sorted, count_of_symbols, 1))
    print(datetime.now() - start)

    start = datetime.now()
    print('\nБиграммы без пересечений:')
    bigramms_unsorted, count_of_bigramms = calculate_count_of_bigramms_without_collisions(string)
    bigramms_sorted_without_collisions = sort_dict(bigramms_unsorted)
    # print(get_bigramms_matrix(bigramms_sorted_without_collisions))
    print(Hn(bigramms_sorted_without_collisions, count_of_bigramms, 2))
    print(datetime.now() - start)

    start = datetime.now()
    print('\nБиграммы с пересечениями:')
    bigramms_unsorted, count_of_bigramms = calculate_count_of_bigramms_with_collisions(string)
    bigramms_sorted_with_collisions = sort_dict(bigramms_unsorted)
    # print(get_bigramms_matrix(bigramms_sorted_with_collisions))
    print(Hn(bigramms_sorted_with_collisions, count_of_bigramms, 2))
    print(datetime.now() - start)
    different_count, new_elements = compare(bigramms_sorted_without_collisions, bigramms_sorted_with_collisions)
    print('\nРазное количество таких биграмм:', different_count, '\nНовые биграммы:', new_elements)

def main():
    string = filter(source)
    # string = 'ааабббабабаббббааабабаба'
    # print(string)
    do_all(string)
    print('\n############################################ Без пробелов ############################################')
    string.replace(' ', '')
    do_all(string)

main()
