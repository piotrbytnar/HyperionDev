#T38 - TASK #2
'''
This program calculates vectors of movie descripiton contained within the folder and compares is with the vector of the HULK movie descripiton using .similarity method
The highest similarity vector index is than used to print out the appropiate movie from the movie list.
'''


#SPACY LIBRARY IMPORT

import spacy

#READ FROM THE FILE
with open('movies.txt', 'r') as movies:
    movies = movies.readlines()

#TEXT ANALYSIS MODEL and VECTORS COMPARISON
nlp = spacy.load("en_core_web_md")

#
descritpion =   ''' Planet Hulk with the description “Will he save
                    their world or destroy it? When the Hulk becomes too dangerous for the
                    Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a
                    planet where the Hulk can live in peace. Unfortunately, Hulk land on the
                    planet Sakaar where he is sold into slavery and trained as a gladiator. 
                '''
description = nlp(descritpion)

similarity_list =[]
for pos in movies:
    pos = nlp(pos)
    similarity = description.similarity(pos)
    similarity_list.append(similarity)

#LIST POSITION IDENTIFICATION
max_similarity = max(similarity_list)
max_index = similarity_list.index(max_similarity)

#INFORMATION PRINTOUT
print(  f'''YOU SHOULD LIKE THIS MOVIE:
{movies[max_index]}     
''')     