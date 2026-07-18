import nltk
import networkx as nx
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.chunk import RegexpParser

# -----------------------------------
# Banking Text Input
# -----------------------------------

text = "A savings account customer can withdraw money using an ATM card."

print("\nInput Text:")
print(text)

# -----------------------------------
# NLP PROCESSING
# -----------------------------------

# Tokenization
tokens = word_tokenize(text)

# POS Tagging
pos_tags = pos_tag(tokens)

# Noun Phrase Extraction
grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
chunk_parser = RegexpParser(grammar)
tree = chunk_parser.parse(pos_tags)

entities = []

for subtree in tree.subtrees():
    if subtree.label() == "NP":
        entity = " ".join(word for word, tag in subtree.leaves())
        entities.append(entity)

entities = list(set(entities))

print("\nExtracted Entities:")
print(entities)

# -----------------------------------
# Relation Extraction
# -----------------------------------

relations = []

for word, tag in pos_tags:
    if tag.startswith("VB"):
        relations.append(word)

print("\nExtracted Relations:")
print(relations)

# -----------------------------------
# SEMANTIC NETWORK CREATION
# -----------------------------------

G = nx.DiGraph()

# Add nodes
for entity in entities:
    G.add_node(entity)

# Simple relation connection
if len(entities) >= 2 and len(relations) > 0:
    G.add_edge(entities[0], entities[1], label=relations[0])

# Graph Layout
pos = nx.spring_layout(G)

nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=3000)

edge_labels = nx.get_edge_attributes(G, 'label')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

plt.title("NLP Generated Banking Semantic Network")
plt.show()