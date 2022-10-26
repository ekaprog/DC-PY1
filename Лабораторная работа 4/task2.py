def get_count_char(str_):
    str_ = str_.lower()
    str_ = str_.replace(' ', '')
    dict_ = {}

    for char in str_:
        if char.isalpha():
            if char in dict_:
                dict_[char] += 1
            else:
                dict_[char] = 1

    return dict_


def get_proc_char(dict_):
    sum_of_chars = sum(dict_.values())
    for char, val in dict_.items():
        dict_[char] = (val * 100) / sum_of_chars

    return dict_


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
dictionary = get_count_char(main_str)
print(dictionary)
