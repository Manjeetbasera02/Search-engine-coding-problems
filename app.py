from flask import Flask, render_template, request, jsonify
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from query.query import get_sorted_order_documents

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