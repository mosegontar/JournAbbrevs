# -*- coding: utf-8 -*-
import shelve
from flask import Flask, session, render_template, request, redirect, url_for, flash
app = Flask(__name__)

SECRET_KEY = 'secretkey'
app.config.from_object(__name__)

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('base.html')


@app.route('/result', methods=['GET', 'POST'])
def get_results():
    """Gets user query and returns all matches"""

    query = request.form['query']
    session['results'] = []

    if query != '':

        # Make list of individual query terms, ignoring words shorter than 
        # 4 characters (e.g., 'for', 'and', 'in', etc)
        keywords = [x.lower() for x in query.split() if len(x) > 3]

        # journal_dict data taken from https://github.com/JabRef/reference-abbreviations
        journal_dict = shelve.open('journal_dict')

       
        entries = []
        # for every key (full length journal name), check if keywords are subset of key and add to entries
        for k, v in journal_dict.items():
            if set(keywords).issubset(set(k.split())):
                k = k.decode('latin-1')
                v = v.decode('latin-1')
                entries.append((k, v))

        # sort entries alphabetically and add them to session['results']        
        for index, item in enumerate(sorted(entries)):
            session['results'].append((item[0].title(), item[1].title()))

    else:
        flash("You didn't search for anything!")
        return redirect(url_for('index'))
        

    return render_template('results.html', results=session['results'])


if __name__ == '__main__':
    app.run(debug=True)