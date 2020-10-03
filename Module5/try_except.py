def character_frequency(filename):
    """ Calculate Frequency of Characters of the given file """
    try:
        f = open(filename)
    except OSError:
        return None

    characters = {}
    for line in f:
        for character in line.lower():
            # if character not in characters:
            #     characters[character] = 1
            # characters[character] += 1
            """ Gets the character from dictionary using .get method, if not found, assigns 0 or adds 1 to  it's value """
            characters[character] = characters.get(character, 0) + 1

    f.close()

    return characters

print(character_frequency("no_such_file.txt"))
