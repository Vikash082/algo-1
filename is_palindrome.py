def is_pal(string):
    i, j = 0, len(string) - 1
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1
    return True


if __name__ == '__main__':
    is_pal("abcdcba")
    is_pal("abcdefghihgfedcba")
    is_pal("abcdefghihgfeddcba")
