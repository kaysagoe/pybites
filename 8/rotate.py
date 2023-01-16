def rotate(string, n):
    """Rotate characters in a string.
    Expects string and n (int) for number of characters to move.
    """
    string_list = list(string)
    if n < 0:
        string_list.reverse()

    for _ in range(abs(n)):
        string_list.append(string_list.pop(0))

    if n < 0:
        string_list.reverse()
    return "".join(string_list)
