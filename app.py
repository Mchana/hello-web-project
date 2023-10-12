import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/count_vowels', methods = ['POST'])
def count_vowels():
    text = request.form['text']
    vowel = 0
    for t in text:
        if t.lower() in "aeiou":
            vowel = vowel + 1

    return f'There are {vowel} vowels in "{text}"'

@app.route('/sort-names', methods = ['POST'])
def sort_names():
    names = request.form['names']
    names_list = names.split(",")
    names_list.sort()
    return ','.join(names_list)

# == Example Code Below ==

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name']

    return f"Hello {name}!"

@app.route('/goodbye', methods=['POST'])

def goodbye():
    name = request.form['name']

    return f"Goodbye {name}!"

@app.route('/submit', methods = ['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']

    return f"Thanks {name}, you sent this message: {message}"

@app.route('/wave', methods = ['GET'])
def wave():
    name = request.args['name']

    return f"I am waving at {name}"

# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

