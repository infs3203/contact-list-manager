from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Contact
from forms import ContactForm
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

# Initialize the database
db.init_app(app)

# Create database tables
with app.app_context():
    db.create_all()

# Helper function to check allowed file types
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']

# Routes
@app.route('/')
def index():
    return render_template('index.html')
#fixed contacts duplication
@app.route('/contacts', methods=['GET', 'POST'])
def list_contacts():
    search_query = request.args.get('search', '')
    
    if search_query:
        contacts = Contact.query.filter(Contact.name.ilike(f"%{search_query}%") | 
                                        Contact.phone.ilike(f"%{search_query}%") |
                                        Contact.email.ilike(f"%{search_query}%")).all()
    else:
        contacts = Contact.query.all()
        
    return render_template('contacts.html', contacts=contacts, search_query=search_query)

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    form = ContactForm()
    
    if form.validate_on_submit():
        # Check if a contact with the same name, phone, or email already exists
        existing_contact = Contact.query.filter(
            (Contact.name == form.name.data) |
            (Contact.phone == form.phone.data) |
            (Contact.email == form.email.data)
        ).first()

        if existing_contact:
            flash('A contact with the same name, phone number, or email already exists!', 'error')
            return redirect(url_for('add_contact'))
        
        profile_picture = None
        if form.profile_picture.data:
            picture = form.profile_picture.data
            if allowed_file(picture.filename):
                picture_filename = f"{form.name.data}_{picture.filename}"  # Use name as part of filename to avoid conflict
                picture_path = os.path.join(app.config['UPLOAD_FOLDER'], picture_filename)
                picture.save(picture_path)
                profile_picture = picture_filename
        
        contact = Contact(
            name=form.name.data,
            phone=form.phone.data,
            email=form.email.data,
            type=form.type.data,
            profile_picture=profile_picture,
            address=form.address.data,
            birthday=form.birthday.data
        )
        
        try:
            db.session.add(contact)
            db.session.commit()
            flash('Contact added successfully!', 'success')
            return redirect(url_for('list_contacts'))
        except Exception as e:
            db.session.rollback()
            flash('Error adding contact. Please try again.', 'error')
    
    return render_template('add_contact.html', form=form)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update_contact(id):
    contact = Contact.query.get(id)
    form = ContactForm(obj=contact)
    
    if form.validate_on_submit():
        contact.name = form.name.data
        contact.phone = form.phone.data
        contact.email = form.email.data
        contact.address = form.address.data
        contact.birthday = form.birthday.data
        
        # Handle profile picture update
        if form.profile_picture.data:
            picture = form.profile_picture.data
            if allowed_file(picture.filename):
                picture_filename = f"{contact.id}_{picture.filename}"  # Use unique filenames to avoid conflicts
                picture_path = os.path.join(app.config['UPLOAD_FOLDER'], picture_filename)
                picture.save(picture_path)
                contact.profile_picture = picture_filename
        
        try:
            db.session.commit()
            flash('Contact updated successfully!', 'success')
            return redirect(url_for('list_contacts'))
        except Exception as e:
            db.session.rollback()
            flash('Error updating contact. Please try again.', 'error')
    
    return render_template('update_contact.html', form=form, contact=contact)

#fix deletation for contacts
@app.route('/delete/<int:id>')
def delete_contact(id):
    contact = Contact.query.get(id)
    if contact:
        db.session.delete(contact)
        db.session.commit()
        flash('Contact deleted successfully!', 'success')
    else:
        flash('Contact not found.', 'error')
    return redirect(url_for('list_contacts'))

if __name__ == '__main__':
    app.run(debug=True, port=5001)
