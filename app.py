# from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
# from models import db, Contact
# from forms import ContactForm
# import os

# app = Flask(__name__)
# app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key')
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Initialize the database
# db.init_app(app)

# # Create database tables
# with app.app_context():
#     db.create_all()

# # Web Routes
# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/contacts')
# def list_contacts():
#     contacts = Contact.query.all()
#     return render_template('contacts.html', contacts=contacts)

# @app.route('/add', methods=['GET', 'POST'])
# def add_contact():
#     form = ContactForm()
#     if form.validate_on_submit():
#         contact = Contact(
#             name=form.name.data,
#             phone=form.phone.data,
#             email=form.email.data,
#             type=form.type.data
#         )
#         try:
#             db.session.add(contact)
#             db.session.commit()
#             flash('Contact added successfully!', 'success')
#             return redirect(url_for('list_contacts'))
#         except Exception as e:
#             db.session.rollback()
#             flash('Error adding contact. Phone number might be duplicate.', 'error')
#     return render_template('add_contact.html', form=form)

# @app.route('/update/<int:id>', methods=['GET', 'POST'])
# def update_contact(id):
#     contact = Contact.query.get(id)
#     form = ContactForm(obj=contact)
    
#     if form.validate_on_submit():
#         contact.name = form.name.data
#         contact.phone = form.phone.data
#         contact.email = form.email.data
#         db.session.commit()
#         return redirect(url_for('list_contacts'))
    
#     return render_template('update_contact.html', form=form, contact=contact)

# @app.route('/delete/<int:id>')
# def delete_contact(id):
#     contact = Contact.query.get(id)
#     # Bug: Not actually deleting the contact but returning success
#     # db.session.delete(contact)
#     db.session.commit()
#     return redirect(url_for('list_contacts'))

# # API Routes
# @app.route('/api/contacts', methods=['GET'])
# def get_contacts():
#     contacts = Contact.query.all()
#     return jsonify([contact.to_dict() for contact in contacts])

# @app.route('/api/contacts/<int:id>', methods=['GET'])
# def get_contact(id):
#     contact = Contact.query.get_or_404(id)
#     return jsonify(contact.to_dict())

# @app.route('/api/contacts', methods=['POST'])
# def create_contact():
#     data = request.get_json()
    
#     if not all(k in data for k in ('name', 'phone', 'type')):
#         return jsonify({'error': 'Missing required fields'}), 400
        
#     contact = Contact(**data)
#     try:
#         db.session.add(contact)
#         db.session.commit()
#         return jsonify(contact.to_dict()), 201
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 400

# @app.route('/api/contacts/<int:id>', methods=['PUT'])
# def update_contact_api(id):
#     contact = Contact.query.get_or_404(id)
#     data = request.get_json()
    
#     for key, value in data.items():
#         if hasattr(contact, key):
#             setattr(contact, key, value)
            
#     try:
#         db.session.commit()
#         return jsonify(contact.to_dict())
#     except Exception as e:
#         db.session.rollback()
#         return jsonify({'error': str(e)}), 400

# @app.route('/api/contacts/<int:id>', methods=['DELETE'])
# def delete_contact_api(id):
#     contact = Contact.query.get(id)
#     if contact:
#         # Bug: Same issue in API - not actually deleting
#         # db.session.delete(contact)
#         db.session.commit()
#     return '', 204  # Returns success even though nothing was deleted

# if __name__ == '__main__':
#     app.run(debug=True, port=5001) 






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
            flash(f'Error adding contact: {str(e)}', 'error')
    else:
        for fieldName, errorMessages in form.errors.items():
            for err in errorMessages:
                flash(f'Error in {fieldName}: {err}', 'error')
    return render_template('add_contact.html', form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_contact(id):
    contact = Contact.query.get_or_404(id)
    form = ContactForm(obj=contact)
    if form.validate_on_submit():
        contact.name = form.name.data
        contact.phone = form.phone.data
        contact.email = form.email.data
        db.session.commit()
        flash('Contact updated successfully!', 'success')
        return redirect(url_for('list_contacts'))
    return render_template('update_contact.html', form=form, contact=contact)

@app.route('/delete/<int:id>')
def delete_contact(id):
    contact = Contact.query.get_or_404(id)
    try:
        db.session.delete(contact)
        db.session.commit()
        flash('Contact deleted successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error deleting contact: {str(e)}', 'error')
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
    if not all(k in data for k in ('name', 'phone', 'type')):
        return jsonify({'error': 'Missing required fields'}), 400
    contact = Contact(**data)
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
    try:
        for key, value in data.items():
            if hasattr(contact, key):
                setattr(contact, key, value)
        db.session.commit()
        return jsonify(contact.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@app.route('/api/contacts/<int:id>', methods=['DELETE'])
def delete_contact_api(id):
    contact = Contact.query.get(id)
    if contact:
        try:
            db.session.delete(contact)
            db.session.commit()
            return '', 204  # Success, no content to return
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 400
    return jsonify({'error': 'Contact not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5001) 
