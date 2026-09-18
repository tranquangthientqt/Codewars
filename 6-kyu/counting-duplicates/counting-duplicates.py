def duplicate_count(text):
    chars = sorted(text.lower())
    count = 0
    for i in range(1, len(chars)):
        if chars[i] == chars[i - 1] and (i + 1 == len(chars) or chars[i] != chars[i + 1]):
            count += 1
    return count