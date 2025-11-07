

def simple_poet(filename):

    lines = []
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            lines = [line.strip() for line in f]
    except FileNotFoundError:
        print("Error: The file '{}' was not found.".format(filename))
    
    return lines

