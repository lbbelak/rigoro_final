from typing import Set


def word_chain(words: Set[str]):
    biggest = 0
    for word in words:
        to_match = words.copy()
        if len(to_match) != 1:
            to_match.remove(word)
        candidate = words_rec(word, to_match, 1)
        if candidate > biggest:
            biggest = candidate
        if biggest == len(words):
            break
    return biggest


def words_rec(actual: str, words: Set[str], biggest_all) -> int:
    biggest = biggest_all
    for word in words:
        if word[0] == actual[-1]:
            if len(words) != 1:
                to_match = words.copy()
                to_match.remove(word)
                candidate = words_rec(word, to_match, biggest_all + 1)
                if candidate > biggest:
                    biggest = candidate
            else:
                biggest += 1
    return biggest


assert word_chain({"goose", "dog", "ethanol"}) == 3       # dog – goose – ethanol
assert word_chain({"why", "new", "neural", "moon"}) == 3  # (moon – new – why)
