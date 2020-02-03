from function import create_encoding_tree, create_individual_values, encode
import json

f = open("text.txt", "r")
text = f.read()
f.close()

tree = create_encoding_tree(text)
codes = create_individual_values(tree)

encoded_text = encode(text, codes)
with open("encoded_text.json", "w") as f:
    json.dump([tree, encoded_text], f)