from sys import argv
from os.path import basename


def count(target_file):
    if target_file:
        file = open(target_file)
        filename = basename(target_file)
        charcount = 0
        charcount_nospace = 0
        wordcount = 0
        for line in file:
            charcount += len(line)
            charcount_nospace += len(''.join(line.split()))
            wordcount += len(line.split())
        pagecount_char = round(charcount / 1800, 2)
        pagecount_char_nospace = round(charcount_nospace / 1800, 2)
        pagecount_word = round(wordcount / 250, 2)
        result = {
            'Name:':                                                     filename,
            'Number of characters:':                                    charcount,
            'Number of characters without spaces:':             charcount_nospace,
            'Number of words:':                                         wordcount,
            'Number of pages (1800 chars):':                       pagecount_char,
            'Number of pages (1800 chars without spaces:': pagecount_char_nospace,
            'Number of pages (250 words):':                        pagecount_word
        }
        return result
    else:
        return None


if __name__ == '__main__':
    if len(argv) > 1:
        data = count(argv[1])
    for item in data:
        print(item, data[item])
    input('Press any key to exit')
