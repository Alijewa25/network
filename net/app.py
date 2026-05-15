from flask import Flask, render_template, request, redirect, url_for
import os
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
    port = int(os.environ.get('PORT', '5000'))
    debug = os.environ.get('FLASK_DEBUG', '0') not in ('0', 'false', 'False')
    app.run(host='0.0.0.0', port=port, debug=debug)