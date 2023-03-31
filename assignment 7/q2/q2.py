# JTMS-14
# a7 p2.py
# Abdullah Rafique
# arafique@jacobs-university.de

# python dictionary
dict = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott",
        "new": "nytt", "year": "˚ar"}
# creating a function and translating word by word


def translate(list_en):
    swedish_words_list = []
    for x in list_en:
        swedish_words_list.append(dict[x])

    return swedish_words_list


# list to be translated
list_en = ['merry', 'christmas', 'and', 'happy', 'new', 'year']
# calling function and printing
swedish_words_list = translate(list_en)
print("The equivalent swedish words are:", swedish_words_list)
