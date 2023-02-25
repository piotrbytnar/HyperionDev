#T38 - TASK #1

import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
print('\n\n')

tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print('\n\n')

sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)

print('\n\n')


# Comment Part 1
'''
Interesting difference between the same cathegories where animals similarity is lower than that of fruits, and banana monkey pair more similar than banana monkey.
'''

# Comment Part 2
'''
'en_core_web_md' - allows breakdown of written work into its particles
'en_core_web_md' - allows checks of similarities of meanings of written work.
'''