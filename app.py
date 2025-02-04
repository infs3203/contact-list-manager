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

# Create database tables
with app.app_context():
    db.create_all()

# Web Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts')
def list_contacts():
    contacts = Contact.query.all()
    return render_template('contacts.html', contacts=contacts)

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
            flash('Error adding contact. Phone number might be duplicate.', 'error')
    return render_template('add_contact.html', form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_contact(id):
    contact = Contact.query.get(id)
    form = ContactForm(obj=contact)
    
    if form.validate_on_submit():
        contact.name = form.name.data
        contact.phone = form.phone.data
        contact.email = form.email.data
        contact.type = form.type.data 
        db.session.commit()
        flash('Contact updated successfully!', 'success')
        return redirect(url_for('list_contacts'))
    
    return render_template('update_contact.html', form=form, contact=contact)

@app.route('/delete/<int:id>')
def delete_contact(id):
    contact = Contact.query.get(id)
    if contact:
        db.session.delete(contact)  # Un-comment this line to delete the contact
        db.session.commit()  # Commit the change to the database
        flash('Contact deleted successfully!', 'success')
    else:
        flash('Contact not found.', 'error')
    return redirect(url_for('list_contacts'))

# API Routes
@app.route('/api/contacts', methods=['GET'])
def get_contacts():
    contacts = Contact.query.all()
    return jsonify([contact.to_dict() for contact in contacts])

@app.route('/api/contacts/<int:id>', methods=['GET'])
def get_contact(id):
    contact = Contact.query.get_or_404(id)
    return jsonify(contact.to_dict())

@app.route('/api/contacts', methods=['POST'])
def create_contact():
    data = request.get_json()
    
    if not data.get('name') or not data['name'].strip():
        return jsonify({'error': 'Name cannot be empty'}), 400

    contact = Contact(name=data['name'], phone=data['phone'], email=data.get('email'))
    
    try:
        db.session.add(contact)
        db.session.commit()
        return jsonify(contact.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/api/contacts/<int:id>', methods=['PUT'])
def update_contact_api(id):
    contact = Contact.query.get_or_404(id)
    data = request.get_json()
    
    for key, value in data.items():
        if hasattr(contact, key):
            setattr(contact, key, value)
            
    try:
        db.session.commit()
        return jsonify(contact.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/api/contacts/<int:id>', methods=['DELETE'])
def delete_contact_api(id):
    contact = Contact.query.get(id)
    if contact:
        db.session.delete(contact)  # This line must stay
        db.session.commit()  # Commit the change to the database
        return '', 204  # No content (success)
    else:
        return jsonify({'error': 'Contact not found'}), 404  # Return an error if contact not found

if __name__ == '__main__':
    app.run(debug=True, port=5001) 

            

def search_contacts():
    query = request.args.get('query', '').strip()  # Stripped to avoid issues with extra spaces

    if query:
        # Search in name, phone, and email columns
        contacts = Contact.query.filter(
            Contact.name.ilike(f'%{query}%') |
            Contact.phone.ilike(f'%{query}%') |
            Contact.email.ilike(f'%{query}%')
        ).all()
    else:
        contacts = []  # Return empty list if no query provided
    
    return jsonify([contact.to_dict() for contact in contacts])

if __name__ == "__main__":
    app.run(debug=True, port=5001) 
    



