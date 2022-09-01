from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/hello')
def index():
    return"halaman index"

@app.route('/user/<username>')
def show_user_profile(username):
    return f'user, {username}'

@app.route("/post/<int:post_id>")
def show_post(post_id):
    return f'post {post_id}'
    

if __name__== "__main__":
    app.run()