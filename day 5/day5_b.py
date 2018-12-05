import string


def part1(unreacted):
    reaction = True
    while reaction:
        for i in range(len(unreacted) - 1):
            reaction = False
            if unreacted[i].swapcase() == unreacted[i + 1]:
                unreacted = unreacted[:i] + unreacted[i + 2:]
                reaction = True
                break
    reacted = len(unreacted)
    return reacted


def part2():
    smallest = 50000
    with open("reacted_input.txt", "r") as f:
        data = f.read()
    for lowercase, uppercase in zip(string.ascii_lowercase, string.ascii_uppercase):
        new_data = data.replace(lowercase, "").replace(uppercase, "")
        reacted = part1(new_data)
        if reacted < smallest:
            smallest = reacted
    return smallest

print(part2())