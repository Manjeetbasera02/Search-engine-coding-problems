from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
# from query.query import get_sorted_order_documents

import math

# fetch documents
def fetch_documents() : 
    documents = []
    with open('preprocessing/documents.txt', 'r', encoding='utf-8', errors='replace') as d_file :
        for document in d_file :
            documents.append(document.strip().split())

    return documents

# fetch vocab_idf 
def fetch_vocb_idf() :
    vocab_idf = {}
    with open('preprocessing/vocab.txt', 'r') as v_file, open('preprocessing/idf.txt', 'r') as idf_file :
        for vocab, idf in zip(v_file, idf_file) :
            vocab_idf[vocab.strip()] = int(idf.strip())

    return vocab_idf

# fetch term_index 
def fetch_term_index() :
    term_index = {}

    lines = []
    
    with open('preprocessing/word_index.txt', 'r') as index_file :
        lines = index_file.readlines()

    for index in range(0, len(lines), 2) :
        term_index[lines[index].strip()] = lines[index+1].strip().split()

    return term_index

# fetch document links
def fetch_document_links() :
    links = []
    
    with open('problems.txt', 'r') as pr_file :
        for link in pr_file :
            links.append(link.strip())

    return links

documents = []
vocab_idf = {}
term_index = {}
document_links = []

#  calculate tf_dictionary = {document, value} for a term
def calculate_tf_dictionary(term) :
    tf_values = {}

    #  tf means = term frequency 

    for document in term_index[term] :
        if document in tf_values :
            tf_values[document] += 1

        else :
            tf_values[document] = 1

    #        tf   /     length of document

    for document in tf_values :
        tf_values[document] /= len(documents[int(document)])

    return tf_values

# calculate idf value for term

def calculate_idf_value(term) :
    return math.log(len(documents) / vocab_idf[term])


# function to get sorted order of documents for query 
def get_sorted_order_documents(query_terms) :
    global documents
    documents = fetch_documents()

    return ["problem 1", "problem 2"]

    global vocab_idf
    vocab_idf = fetch_vocb_idf()

    global term_index
    term_index = fetch_term_index()

    global document_links
    document_links = fetch_document_links()

    # {document, value}
    total_tf_idf = {}

    # iterate for each term in query and caluclate total tf_idf value for each document 

    for term in query_terms :
        # check , is term a part of vocab ?

        if term not in vocab_idf :
            continue

        tf_values = calculate_tf_dictionary(term)
        idf_value = calculate_idf_value(term)

        for document in tf_values :
            if document in total_tf_idf :
                total_tf_idf[document] += tf_values[document]*idf_value
            
            else :
                total_tf_idf[document] = tf_values[document]*idf_value

    
    # sort total_tf_idf in order of decreasing  values
    total_tf_idf = dict(sorted(total_tf_idf.items(), key=lambda item: item[1], reverse=True))

    # store links for documents in ans list 

    ans = []

    for document in total_tf_idf :
        ans.append(document_links[int(document)])

    return ans

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for CSRF protection

class SearchForm(FlaskForm):
    search = StringField('Enter your search terms')
    submit = SubmitField('Search')

# Route for testing
@app.route('/<query>')
def return_links(query):
    q_terms = [term.lower() for term in query.strip().split()]
    return jsonify(get_sorted_order_documents(q_terms))

# Main route for rendering the form and showing results
@app.route('/', methods=['GET', 'POST'])
def home():
    form = SearchForm()  # Instantiate the form here

    if form.validate_on_submit():  # Validate the form when submitted
        query = form.search.data
        q_terms = [term.lower() for term in query.strip().split()]
        results = get_sorted_order_documents(q_terms)[:20]
        return render_template('index.html', form=form, results=results)

    return render_template('index.html', form=form, results=None)