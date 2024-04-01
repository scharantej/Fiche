
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

examples = [
    {
        'title': 'Example 1',
        'description': 'This is an example of a simple Flask application.',
        'html': 'index.html',
    },
    {
        'title': 'Example 2',
        'description': 'This is an example of a more complex Flask application.',
        'html': 'example.html',
    },
]

@app.route('/')
def home():
    return render_template('index.html', examples=examples)

@app.route('/example/<int:example_id>')
def example(example_id):
    example = examples[example_id]
    return render_template(example['html'], example=example)

if __name__ == '__main__':
    app.run(debug=True)
