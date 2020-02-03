def create_encoding_tree(text):
    char_frequency = {}
    for symbol in text:
        if symbol not in char_frequency:
            char_frequency.update({symbol: 1})
        else:
            char_frequency[symbol] += 1

    char_frequency = sorted(char_frequency.items(), key=lambda value: value[1])

    tree = char_frequency
    while len(tree) != 1:
        a, b = tree.pop(0), tree.pop(0)
        tree.append(((a[0], b[0]), a[1] + b[1]))
        tree = sorted(tree, key=lambda value: value[1])

    return tree[0][0]

def create_individual_values(tree):
    encode = {}
    q = [[tree, ""]]
    while q:
        current = q.pop(0)
        stem, code = current[0], current[1]
        for index, branch in enumerate(stem):
            if not isinstance(branch, str):
                q.append([branch, code + str(index)])
            else:
                encode.update({branch: code + str(index)})
    
    return encode

def encode(text, codes):
    output = ""
    for symbol in text:
        output += codes[symbol]
    
    return output

def decode(encoded_text, tree):
    output = ""
    current_branch = tree
    for number in encoded_text:
        current_branch = current_branch[int(number)]

        if isinstance(current_branch, str):
            output += current_branch
            current_branch = tree
    
    return output