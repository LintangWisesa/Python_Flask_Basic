from flask import Flask, jsonify, json, render_template

app = Flask(__name__)

Students = [
    {
        'id': 1,
        'name': 'Andi',
        'age': 21
    },
    {
        'id': 2,
        'name': 'Budi',
        'age': 22
    },
    {
        'id': 1,
        'name': 'Caca',
        'age': 23
    }
]

@app.route('/')
def index():
    return render_template('home.html')
    # render html file from templates dir

@app.route('/about')
def about():
    return render_template('about.html')
    # render html file from templates dir

@app.route('/data')
def data():
    jsonData = json.dumps(Students) 
    return jsonify(Students = jsonData)

if __name__ == '__main__':
    app.run(debug = True)
    # automatically restart when there is a change
