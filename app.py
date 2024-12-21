from flask import Flask, jsonify
from db import db
from resources.item import ItemResource
from resources.store import StoreResource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'  # Використовуємо SQLite для простоти
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Створення таблиць при запуску програми
@app.before_request
def create_tables():
    db.create_all()

@app.route('/item/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    resource = ItemResource()
    return resource.delete(item_id)

@app.route('/store/<int:store_id>', methods=['DELETE'])
def delete_store(store_id):
    resource = StoreResource()
    return resource.delete(store_id)

if __name__ == '__main__':
    app.run(debug=True)
