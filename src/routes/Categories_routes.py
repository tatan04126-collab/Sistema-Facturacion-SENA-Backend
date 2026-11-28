from flask import Blueprint, jsonify, request
from src.models.Categories import Categories


Categories_bp = Blueprint('Categories', __name__)

@Categories_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Categories.get()
    return jsonify([{
        'id': category.id,
        'name': category.name
    } for category in categories]) 

@Categories_bp.route('/categories', methods=['POST'])
def post_category():
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    new_category = Categories(name=name)
    Categories.save(new_category)

    return jsonify({
        'id': new_category.id,
        'name': new_category.name
    }), 201