# БСБО-05-19 Салынь Даниил Леонидович
import copy

result = []
ignore_list = []
n = int(input())
words_list = []
sorted_words = []
for i in range(n):
    word = input()
    words_list.append(list(word.lower()))
    copy_word = list(copy.copy(word))
    copy_word.sort()
    sorted_words.append(list(copy_word))
for i in range(len(words_list)):
    for j in range(len(words_list)):
        if words_list[i] != words_list[j] and sorted_words[i] == sorted_words[j] and words_list[i] not in ignore_list:
            result.append("".join(words_list[i]) + " " + "".join(words_list[j]))
            ignore_list.append(words_list[j])
for i in range(1, len(result)):
    if "".join(result[i]).find(" ") > 0 and "".join(result[i - 1]).find(" ") > 0:
        if result[i - 1][:result[i - 1].index(" ")] == result[i][:result[i].index(" ")]:
            result[i - 1] += result[i][result[i].index(" "):]
            result.remove(result[i])
            result.append("")
result.remove('')
for i in result:
    print(i)
