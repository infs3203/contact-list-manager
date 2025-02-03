# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from models import db, Contact
from forms import ContactForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts')
def list_contacts():
    search = request.args.get('search', default='', type=str)
    group = request.args.get('group', default='', type=str)

    query = Contact.query
    if search:
        query = query.filter(Contact.name.ilike(f"%{search}%"))
    if group:
        query = query.filter(Contact.type == group)

    contacts = query.all()
    return render_template('contacts.html', contacts=contacts)

@app.route('/api/contacts', methods=['GET'])
def api_contacts():
    search = request.args.get('search', default='', type=str)
    group = request.args.get('group', default='', type=str)

    query = Contact.query
    if search:
        query = query.filter(Contact.name.ilike(f"%{search}%"))
    if group:
        query = query.filter(Contact.type == group)

    contacts = query.all()
    return jsonify([contact.to_dict() for contact in contacts])

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    form = ContactForm()
    if form.validate_on_submit():
        contact = Contact(
            name=form.name.data,
            phone=form.phone.data,
            email=form.email.data,
            type=form.type.data
        )
        try:
            db.session.add(contact)
            db.session.commit()
            flash('Contact added successfully!', 'success')
            return redirect(url_for('list_contacts'))
        except Exception as e:
            db.session.rollback()
            flash('Error adding contact.', 'danger')
    return render_template('add_contact.html', form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_contact(id):
    contact = Contact.query.get_or_404(id)
    form = ContactForm(obj=contact)
    if form.validate_on_submit():
        contact.name = form.name.data
        contact.phone = form.phone.data
        contact.email = form.email.data
        contact.type = form.type.data
        try:
            db.session.commit()
            flash('Contact updated successfully!', 'success')
            return redirect(url_for('list_contacts'))
        except Exception as e:
            db.session.rollback()
            flash('Error updating contact.', 'danger')
    return render_template('update_contact.html', form=form, contact=contact)

@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    try:
        db.session.delete(contact)
        db.session.commit()
        flash('Contact deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash('Error deleting contact.', 'danger')
    return redirect(url_for('list_contacts'))

if __name__ == '__main__':
    app.run(debug=True)