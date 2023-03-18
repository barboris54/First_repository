from flask import Flask, render_template, url_for, request, flash, session, redirect, abort
import sqlite3
import os

# конфигурация
DATABASE = '/tmp/flsk.db'
DEBUG = True
SECRET_KEY = 'sdfenfsdfhsnkdf2hy32grfwj'

app = Flask(__name__)
app.config.from_object(__name__)

app.config.update(DATABASE=os.path.join(app.root_path, 'flsk.db'))


def connect_db():
    con = sqlite3.connect(app.config['DATABASE'])
    con.row_factory = sqlite3.Row
    return con

def create_db():
    db = connect_db()
    with app.open_resource('sq_db.sql','r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


menu = [{'name':'Главная', 'url':'index'},
    {'name':'О нас', 'url':'about'},
    {'name':'Обратный связь', 'url':'contact'},]


@app.route('/')
@app.route('/index')
def index():
    print(url_for('index'))
    return render_template('index.html', title='Главная', menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title='О нас', menu=menu)

@app.route('/contact', methods=['POST','GET'])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отпралено успешно', category='success')
        else:
            flash('Ошибка отправки', category='error')
        # context = {
        #     'username': request.form['username'],
        #     'email': request.form['email'],
        #     'message': request.form['message']
        # }
        return render_template('contacts.html', title='Обратная связь', menu=menu)

    return render_template('contacts.html', title='Обратная связь', menu=menu)


@app.route('/login', methods=['POST','GET'])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == 'admin' and request.form['psw'] == '123456':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title='Авторизация', menu=menu)

@app.route('/profile/<username>')
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)
    return f'Пользователь {username}'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title='Страница не найдена', menu = menu)



if __name__ == '__main__':
    app.run(debug=True)
