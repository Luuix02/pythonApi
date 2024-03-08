from flask import request
from config.mongodb import mongo 



def create_recipe_service():
    data = request.get_json()
    nombre = data.get('nombre', None)
    ingredientes = data.get('ingredientes', None)
    instrucciones = data.get('instrucciones', None)
    if nombre:
        response = mongo.db.recipesKitchen.insert_one({
           'nombre': nombre,
           'ingredientes': ingredientes,
           'instrucciones': instrucciones, 
        })
        result = {
            'id' : str(response.inserted_id),
            'nombre': nombre,
            'ingredientes': ingredientes,
            'instrucciones': instrucciones,
        }
        return result
    else:
        return 'Invalid errror', 400

    