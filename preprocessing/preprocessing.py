import os 
import time

def remove_leading_num(text) :
    x = text.split()
    # convert to lowercase 
    x = [word.lower() for word in x]
    return " ".join(x[1:])

# remove exisitng document.txt file 
if os.path.exists('preprocessing/documents.txt') :
    os.remove('preprocessing/documents.txt')

# get documents form heading.txt file 

with open('preprocessing/documents.txt', 'a') as d_file :
    with open('heading.txt', 'r') as h_file :
        for heading in h_file :
            d_file.write(remove_leading_num(heading) + '\n')


# create vocab dictionary from documents.txt file and calculate idf value 

vocab = {}

def create_vocab(document) :
    # make document unique 
    words = document.split()
    words = list(set(words))

    # iterate over document 
    for word in words :
        if word in vocab :
            vocab[word] += 1

        else :
            vocab[word] = 1

with open('preprocessing/documents.txt', 'r') as d_file :
    for document in d_file :
        create_vocab(document)

# sort vocab in descending order of values

vocab = dict(sorted(vocab.items(), key=lambda item: item[1], reverse=True))

# add vocab in vocab.txt and idf value in idf.txt
if os.path.exists('preprocessing/vocab.txt') :
    os.remove('preprocessing/vocab.txt')

if os.path.exists('preprocessing/idf.txt') :
    os.remove('preprocessing/idf.txt')

with open('preprocessing/vocab.txt', 'a') as v_file, open('preprocessing/idf.txt', 'a') as idf_file :
    for word in vocab :
        v_file.write(word + '\n')
        idf_file.write(str(vocab[word]) + '\n')

# find documents's index containing word and store it in word_index.txt file 

word_index = {}

index = 0
with open('preprocessing/documents.txt', 'r') as d_file :
    for document in d_file :
        for word in document.split() :
            if word in word_index :
                word_index[word].append(index)

            else :
                word_index[word] = [index]
        
        index += 1

if os.path.exists('preprocessing/word_index.txt') :
    os.remove('preprocessing/word_index.txt')

with open('preprocessing/word_index.txt', 'a') as index_file :
    for word in word_index :
        index_file.write(word + '\n')
        index_file.write(' '.join(map(str, word_index[word])) + '\n')

