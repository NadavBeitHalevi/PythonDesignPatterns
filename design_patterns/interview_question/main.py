from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy import text

# /Users/nadav/Projects/PythonDesignPatterns/design_patterns/interview_question/main.py


app = Flask(__name__)
app.engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
# db = SQLAlchemy(app)

# # Model definition
# class Item(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), nullable=False)
#     description = db.Column(db.String(200), nullable=False)

# Create the database
def create_db():
    with app.app_context():
        with app.engine.connect() as connection:
            result = connection.execute(text("select 'hello world'"))
            print(result.all())
            connection.execute(text("CREATE TABLE items (x int, y int)"))
#             connection.execute(text(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
# ...         [{"x": 1, "y": 1}, {"x": 2, "y": 4}],))
            connection.commit()
            result = connection.execute("SELECT * FROM items")
            print(result.fetchall())


# API endpoint with pagination
@app.route('/items', methods=['GET'])
def get_items():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 2, type=int)
    items = Item.query.paginate(page, per_page, False)
    
    return jsonify({
        'items': [{'id': item.id, 'name': item.name, 'description': item.description} for item in items.items],
        'total': items.total,
        'pages': items.pages,
        'current_page': items.page
    })

@app.route('/helloworld', methods=['GET'])
def hello_world():
    return "Hello, World!"

# String manipulation example
def reverse_string(s):
    return s[::-1]

# List comprehension example
def square_numbers(numbers):
    return [x**2 for x in numbers]

# Dictionary comprehension example
def create_dict_from_list(keys, values):
    return {k: v for k, v in zip(keys, values)}

# Lambda expression example
def sort_items_by_name(items):
    return sorted(items, key=lambda x: x['name'])

if __name__ == '__main__':
    # create_db()
    # app.run(debug=True)
    
    print(create_dict_from_list([1, 2, 3], ['a', 'b', 'c']))
    print(sort_items_by_name([{'name': 'Item3'}, {'name': 'Item1'}, {'name': 'Item2'}]))
    print(reverse_string('hello'))
    print(square_numbers([1, 2, 3, 4, 5]))
    print("Hello, World!")
