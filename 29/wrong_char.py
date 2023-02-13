from typing import List


def get_index_different_char(chars: List[str]):
    is_alphanum = _is_alphanum_seq(chars)

    for index, char in enumerate(chars):
        char_str: str = str(char)
        if is_alphanum and not char_str.isalnum():
            return index
        elif not is_alphanum and char_str.isalnum():
            return index


def _is_alphanum_seq(chars: List[str]) -> bool:
    alphanum_count = 0
    non_alphanum_count = 0
    for char in chars[:3]:
        char = str(char)
        if char.isalnum():
            alphanum_count += 1
        else:
            non_alphanum_count += 1

    return alphanum_count > non_alphanum_count
