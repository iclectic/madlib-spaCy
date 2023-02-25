import spacy

nlp = spacy.load("en_core_web_sm")

# Define a function to get the first token with an acceptable part of speech tag for a given Doc object
def get_pos(doc):
    for token in doc:
        if token.pos_ == "ADJ" or token.pos_ == "NOUN" or token.pos_ == "VERB":
            return token
    return "#blank#"

adjective1 = get_pos(nlp(input("Enter an adjective: "))).text
adjective2 = get_pos(nlp(input("Enter an adjective: "))).text
noun1 = get_pos(nlp(input("Enter a noun: "))).text
adjective3 = get_pos(nlp(input("Enter an adjective: "))).text
verb1 = get_pos(nlp(input("Enter a verb: "))).text
noun2 = get_pos(nlp(input("Enter a noun: "))).text

# Construct the madlib string with the input words
madlib = f"Computer science (Msc) is a {adjective1} programme. It can be {adjective2} sometimes but the pros outweigh the cons. Studying computer science is not the only {noun1} to becoming a software engineer considering that a {adjective3} of software engineers did not {verb1} through {noun2} education."

print(madlib)



