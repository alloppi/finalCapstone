'''
Command "python -m spacy download en_core_web_md" to install which is able to find similarities
Command "python -m spacy download en_core_web_sm" 

Difference between en_core_web_md and en_core_web_sm
To make them compact and fast, spaCy’s small pipeline packages (all packages that end in sm) don’t ship with word vectors, 
and only include context-sensitive tensors. This means you can still use the similarity() methods to compare documents, 
spans and tokens – but the result won’t be as good, and individual tokens won’t have any vectors assigned. 
So in order to use real word vectors, you need to download a larger pipeline package.
'''

import spacy  # importing spacy

nlp_md = spacy.load('en_core_web_md')  # specifying the model to us
nlp_sm = spacy.load('en_core_web_sm')  # specifying the small pipeline model to use

# Comparing cat, monkey and banana and give their similarity
print("---Use em_core_web_md to show similarity between cat monkey banana ---")
tokens = nlp_md('cat monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print('----------------------')

'''
Note about what you found interesting about the similarities between cat, monkey and banana:
The result of similarity:
    cat monkey 0.39452385902404785
    cat banana 0.23343780636787415
    monkey banana 0.3741353750228882
cat and monkey is the most similar because they are both animals
monkey and banana is the 2nd most similar because monkey eat banana and put them closer together
cat and banana is the least similar because cat is animal and banana is fruit and they are in less association
'''

# Comparing bus, tyres and man and give their similarity
print("---Use em_core_web_md to show similarity between bus tyres man---")
tokens = nlp_md('bus tyres man')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print('----------------------')

'''
Note about what you found interesting about the similarities between bus tyres man:
The result of similarity:
    bus tyres 0.1658991128206253
    bus man 0.43344375491142273
    tyres man 0.078106589615345
bus and man is the most similar because man takes bus and has most relation 
bus and tyres is the 2nd most similar because bus always has 4 tyres. I expect they should most close together 
  but the result is out of my expectation
tyres and man is the least similar because they are in different types
'''

# Comparing cat, monkey and banana again but using em_core_web_sm model 
print("---em_core_web_sm---")
tokens = nlp_sm('cat monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))
print('----------------------')

'''
note on different from the model 'en_core_web_md' and 'em_core_web_sm'
The result of similarity using em_core_web_sm and em_core_web_md:
                  em_core_web_sm        en_core_web_md
   cat monkey     0.7434066534042358    0.39452385902404785
   cat banana     0.45747023820877075   0.23343780636787415
   monkey banana  0.4953974783420563    0.3741353750228882

In this case, the overall result is quite similar, even em_core_web_sm give a little bit clear result.
When compare cat and monkey, because cat and monkey using em_core_web_sm shows higher similarity.
When compare cat and banana, monkey and banana, em_core_web_md give better result. It is easy to find that 
monkey and banana give clear closer relation, cat and banana give less relation.

Although the document of spaCy said that the result of em_core_web_sm is not good as em_core_web_md
because em_core_web_sm lack of word vectors and smaller pipeline packages. I consider may be 
for this case, I just compare the nouns but not a complete sentence. As a result, the result between 
em_core_web_sm and em_core_web_md gives not too much difference.
'''