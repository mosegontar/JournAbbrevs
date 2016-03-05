# -*- coding: utf-8 -*-
import shelve
from flask import Flask, session, render_template, request, redirect, url_for, flash
app = Flask(__name__)

SECRET_KEY = 'alexgontar'
app.config.from_object(__name__)

@app.route('/index', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('base.html')


@app.route('/result', methods=['GET', 'POST'])
def get_results():
        
    query = request.form['query']
    session['results'] = []
    if query != '':

        keyword = [x.lower() for x in query.split() if x > 3]
        journal_dict = shelve.open('journal_dict')

       
        entries = []
        for k, v in journal_dict.items():
            if set(keyword).issubset(set(k.split())):
                k = k.decode('latin-1')
                v = v.decode('latin-1')
                entries.append((k, v))

        for index, item in enumerate(sorted(entries)):
            session['results'].append((item[0].title(), item[1].title()))
    else:
        flash("You didn't search for anything!")
        return redirect(url_for('index'))
        

    return render_template('results.html', results=session['results'])


if __name__ == '__main__':
    app.run(debug=True)