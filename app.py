from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models import db, Contact
import os

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    try:
        db.create_all()
        print("✅ Database connected successfully")
    except Exception as e:
        print(f"⚠️ Database connection error: {e}")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name    = request.form['name']
        email   = request.form['email']
        contact = request.form['contact']

        new_contact = Contact(name=name, email=email, contact=contact)
        db.session.add(new_contact)
        db.session.commit()
        flash('Record inserted successfully!', 'success')
        return redirect(url_for('index'))

    contacts = Contact.query.all()
    return render_template('index.html', contacts=contacts)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
