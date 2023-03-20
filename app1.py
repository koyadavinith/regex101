from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        pattern = request.form['pattern']
        text = request.form['text']
        matches = re.findall(pattern, text)
        return render_template('regex1.html', pattern=pattern, text=text, matches=matches)
    else:
        # This else block handles GET requests (i.e. when the page is first loaded)
        # We need to pass in default values for pattern, text, and matches to avoid errors
        return render_template('regex1.html', pattern='', text='', matches=[])

if __name__ == '__main__':
    app.run(debug=True)
