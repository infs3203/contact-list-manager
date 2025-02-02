from flask import Flask, request, jsonify
from models import db, Contact

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contacts.db'  # Ensure the database path is correct
db.init_app(app)

@app.route('/search', methods=['GET'])
def search_contacts():
    query = request.args.get('q', '')  # Get the search query from the URL
    if not query:
        return jsonify({"error": "No search query provided"}), 400

    results = Contact.query.filter(Contact.name.ilike(f"%{query}%")).all()  # Case-insensitive search
    return jsonify([contact.to_dict() for contact in results])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Ensure the database tables exist
    app.run(debug=True)

