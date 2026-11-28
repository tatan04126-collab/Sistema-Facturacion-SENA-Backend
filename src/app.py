from flask import Flask
from src.models import Base,engine
from src.models.Categories import Categories
from src.models.Inventories import Inventories
from src.routes.Categories_routes import Categories_bp

app = Flask (__name__)

app.register_blueprint(Categories_bp)

Base.metadata.create_all(engine)

@app.route('/')
def hello_world():
    return 'Hello, World!'



if __name__ == '__main__':
    app.run(debug=True)