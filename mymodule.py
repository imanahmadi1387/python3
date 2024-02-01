def power(lnumber : list) -> list:
    return list(map(lambda n : n ** 2, lnumber))
    

def vowel(word: str) -> set:
    return set(word).intersection(set('aeoiu'))


def count_(word: str, letter= 'a') -> int:
    return word.count(letter)



