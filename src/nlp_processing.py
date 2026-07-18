import spacy
import nltk
from nltk.tokenize import word_tokenize

# Load NLP model
nlp = spacy.load("en_core_web_sm")

# Sample banking text
text = "A savings account customer can withdraw money using an ATM card."

# -------------------------------
# 1. Tokenization
# -------------------------------
tokens = word_tokenize(text)
print("\nTokens:")
print(tokens)

# -------------------------------
# 2. POS Tagging
# -------------------------------
doc = nlp(text)
print("\nPOS Tags:")
for token in doc:
    print(token.text, "->", token.pos_)

# -------------------------------
# 3. Entity Extraction (Rule-based for banking)
# -------------------------------
entities = []
banking_terms = ["customer", "account", "atm", "card", "money", "savings"]

for token in doc:
    if token.text.lower() in banking_terms:
        entities.append(token.text.capitalize())

print("\nExtracted Banking Entities:")
print(list(set(entities)))

# -------------------------------
# 4. Relationship Extraction (Simple Verb-based)
# -------------------------------
relations = []
for token in doc:
    if token.pos_ == "VERB":
        relations.append(token.lemma_)

print("\nExtracted Relations:")
print(relations)