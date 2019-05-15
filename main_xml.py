from pprint import pprint
import xml.etree.ElementTree as ET
from collections import defaultdict


def sortByLength(inputStr):
    return len(inputStr)


def count_repetitions(words_list):
    word_count_dict = defaultdict(int)
    number_words = {}
    for word in words_list:
        number_words.setdefault(word, word_count_dict[word])
        number_words[word] = word_count_dict[word]
        word_count_dict[word] += 1
    return number_words


def top_ten_words(count_repetitions_dict):
    words_set = set()
    for i in count_repetitions_dict.values():
        words_set.add(i)
    for_sort_words = list(words_set)
    for_sort_words.sort(reverse=True)

    top10words = []
    for _ in range(10):
        for k, v in count_repetitions_dict.items():
            if for_sort_words[_] == v:
                top10words.append([k, v])
    return top10words[:10]


tree = ET.parse('files/newsafr.xml')

items = tree.findall('channel/item/description')
words_list = []
for description in items:
    for word in description.text.split():
        if len(word) > 6:
            words_list.append(word.lower())
words_list.sort(key=sortByLength, reverse=True)

number_words = count_repetitions(words_list)
top10words = top_ten_words(number_words)
for i in top10words:
    print(f'Слово "{i[0]}" встречается в новостях {i[1]} раз.')
