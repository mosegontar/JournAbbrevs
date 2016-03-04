import shelve
from flask import Flask, session, render_template, request, redirect
app_lulu = Flask(__name__)

SECRET_KEY = 'alexgontar'
app_lulu.config.from_object(__name__)

@app_lulu.route('/', methods=['GET', 'POST'])
def index_lulu():
    return render_template('query.html')



@app_lulu.route('/result', methods=['GET', 'POST'])
def get_results():
        
    query = request.form['query']
    keyword = [x.lower() for x in query.split() if x > 3]
    journal_dict = shelve.open('journal_dict')

   
    entries = []
    for k, v in journal_dict.items():
        if set(keyword).issubset(set(k.split())):
            entries.append((k, v))

    session['results'] = []
    for index, item in enumerate(sorted(entries)):
        session['results'].append(item[0].title() + ' = ' + item[1].title())

    return render_template('results.html', results=session['results'])





if __name__ == '__main__':
    app_lulu.run(debug=True)