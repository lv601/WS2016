from flask import Flask, url_for, request
from flask import render_template


app = Flask(__name__)

# Routes are defined by Flask Decorators
@app.route("/")  # http://localhost:5678
def start():
    return "Hello World!"


@app.route('/post/<int:post_id>')  # http://localhost:5678/post/10
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post {}'.format(post_id)


@app.route('/post/<string:post_id>')  # http://localhost:5678/post/10
def show_post_by_name(post_name):
    # show the post with the given id, the id is an integer
    return 'Post by name{}'.format(post_name)


# Routes rendering html with jinja template
@app.route('/hello/')  # http://localhost:5678/hello
@app.route('/hello/<name>')  # http://localhost:5678/hello/Susi
def hello(name=None):
    return render_template('hello.html', name=name)

# Building urls
@app.route('/build-url/<name>')
def build_url(name=None):
    return url_for("hello", name=name)  # use function name to build


@app.route('/data', methods=['POST', 'GET'])
def data():
    name=request.form['yourname']
    email=request.form['youremail']

    return render_template('form_action.html', name=name, email=email)

@app.route('/form_submit')
def form():
    return render_template('form_submit.html')

if __name__ == "__main__":
    # Start flask application on port 5678 - http://localhost:5678
    app.run(host="0.0.0.0", port=5678)