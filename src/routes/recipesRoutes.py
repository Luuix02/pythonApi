from flask import Blueprint
from services.recipes import create_recipe_service

recipes = Blueprint('recipes', __name__)

@recipes.route('/',  methods=['GET'])
def get_recipes():
    return 'get all recipes'

@recipes.route('/<id>', methods=['GET'])
def get_recipe(id):
    return 'get all recipes by Id'

@recipes.route('/', methods=['POST'])
def create_recipe():
    return create_recipe_service()


@recipes.route('/<id>', methods=['PUT'])
def update_recipe(id):
    return 'update recipe'

@recipes.route('/<id>', methods=['DELETE'])
def delete_recipe(id):
    return 'delete recipe'