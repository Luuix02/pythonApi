from flask import Flask, render_template
from routes.recipesRoutes import recipes
from dotenv import load_dotenv
from config.mongodb import mongo
import os

load_dotenv()

#conectarDb:mongodb+srv://recipes:<password>@cluster0.15aqwie.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0
#punto de entrada de la app
app = Flask(__name__)

app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo.init_app(app)

@app.route('/')
def index():
    return render_template('index.html')

app.register_blueprint(recipes , url_prefix='/recipes')

if __name__ == '__main__':
    app.run(debug=True)
 
 