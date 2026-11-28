from flask import Flask
from src.models import Base,engine
from src.models.Categories import Categories
from src.models.Inventories import Inventories

app = Flask (__name__)

Base.metadata.create_all(engine)

@app.route('/')
def hello_world():
    return 'Hello, World!'



if __name__ == '__main__':
    app.run(debug=True)