import spacy  # importing spacy

nlp = spacy.load('en_core_web_md')  # specifying the model we want to use.

target = """Will he save their world or destroy it? 
When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle 
and launch him into space to a planet where the Hulk can live in peace. 
Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."""

# For code reviewer, I have already written the function 'find_most_similar' that 
#    return the most similar movie in first assignment submission, please see the below comment before the function coding.
#    Thank you.
#
# A general function to find the most similar string by given the strings list and the string to be compare
# Two input parameters:
#    1. The list contains strings that to be compare the similarity (list of movies that to be compare)
#    2. The string that for the comparison (the target to be watch)
# Output parameter is the string that is the most similar (the most similar movie)
# UserWarning: [W008] Evaluating Doc.similarity based on empty vectors.
def find_most_similar(sentences, sentence_to_compare):
    high_similarity = 0  # store the highest similarity value
    high_similar_sentence = ' ' # store the highest similarity sentence
    model_sentence = nlp(sentence_to_compare)
    for sentence in sentences:
        similarity = nlp(sentence).similarity(model_sentence)
        # print(sentence + " - ", similarity)
        if similarity > high_similarity:
            high_similarity = similarity
            high_similar_sentence = sentence
    return high_similar_sentence

# Program entry
# opening the movies file in read mode
my_file = open("movies.txt", "r")
  
# reading the file
data = my_file.read()
  
# splitting the text when newline ('\n') is seen and put in movie list
movies = data.split("\n")
my_file.close()

# find the most similar movie by given the movie list and target watch
result = find_most_similar(movies, target)

# print the result 
print("The most similar movie is " + result)