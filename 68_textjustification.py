def jystrfi(words, maxWidth):
    lines = []
    current_line = []
    current_length = 0

    for word in words:
        if current_length + len(word) + len(current_line) > maxWidth:
            for i in range(maxWidth - current_length):
                current_line[i % (len(current_line) - 1 or 1)] += ' '
            lines.append(''.join(current_line))

            current_line = []
            current_length = 0

        current_line.append(word)
        current_length += len(word)

    lines.append(' '.join(current_line).ljust(maxWidth))

    return lines


val = jystrfi(["this", "is", "an", "example"], 16)
print(val)