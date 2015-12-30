from flask import Flask, request, render_template, url_for
from flask.ext.mongoengine import MongoEngine
from flask.ext.mongoengine.wtf import model_form
from flask_wtf import Form


app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'
app.config['MONGODB_SETTINGS'] = {
    # 'replicaset': '',
    'db': 'example',
    # 'host': '',
    # 'username': '',
    # 'password': ''
}
db = MongoEngine(app)


class Customer(db.Document):
    name = db.StringField()
    birthday = db.DateTimeField()
    def __unicode__(self):
        return u'employee %s' % self.name

CustomerForm = model_form(Customer, base_class=Form, field_args={
    'birthday': {
        # we want to use date format, not datetime
        'format': '%Y-%m-%d'
    }
})


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        do_the_login()
    else:
        error = 'Invalid User/Pass'
    return render_template('login.html', error=error)




def do_the_login():
    pass


def show_the_login_form():
    pass


if __name__ == '__main__':
    app.run(debug=True)


