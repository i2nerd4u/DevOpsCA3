"""Flask web application for calorie counter."""
from flask import Flask, render_template, request, redirect, url_for, jsonify
from calorie_counter.calculator import CalorieCounter

app = Flask(__name__)
counter = CalorieCounter()

@app.route('/')
def index():
    return render_template('index.html', meals=counter.list_meals(), total=counter.total_calories())

@app.route('/add', methods=['POST'])
def add_food():
    food = request.form['food']
    calories = int(request.form['calories'])
    counter.add_food(food, calories)
    return redirect(url_for('index'))

@app.route('/reset', methods=['POST'])
def reset():
    counter.reset_day()
    return redirect(url_for('index'))

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "total_meals": len(counter.list_meals())})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=False)