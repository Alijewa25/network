from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
import models

app = Flask(__name__)
CORS(app)

# Ensure database and schema exist
models.init_db()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        if name and post:
            models.create_post(name.strip(), post.strip())
        return redirect(url_for('index'))

    posts = models.get_posts()
    return render_template('index.html', posts=posts)

if __name__ == "__main__":
    app.run(debug=True)