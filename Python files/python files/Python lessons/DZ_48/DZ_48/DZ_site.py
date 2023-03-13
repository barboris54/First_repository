from flask import Flask, render_template, url_for, request

app = Flask(__name__)

menu = [{'name':'page1', 'url':'page1'},
    {'name':'page2', 'url':'page2'},
    {'name':'page3', 'url':'page3'},]


@app.route('/')
@app.route('/page1')
def page1():
    return render_template('page_1.html', title='Page№1', menu=menu)

@app.route('/page2')
def page2():
    return render_template('page_2.html', title='Page№2', menu=menu)

@app.route('/page3')
def page3():
    return render_template('page_3.html', title='Page№3', menu=menu)


if __name__ == '__main__':
    app.run(debug=True)