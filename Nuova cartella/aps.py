from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Variabili globali per il conteggio delle votazioni
votes = {'tick': 0, 'x': 0}
pin = "9120"  # PIN di esempio

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/vote', methods=['POST'])
def vote():
    choice = request.form['vote']
    if choice in votes:
        votes[choice] += 1
    return ('', 204)

@app.route('/validate', methods=['POST'])
def validate():
    data = request.json
    if data['pin'] == pin:
        results = f"Tick: {votes['tick']}, X: {votes['x']}"
        return jsonify(valid=True, results=results)
    return jsonify(valid=False)

@app.route('/reset', methods=['POST'])
def reset():
    global votes
    votes = {'tick': 0, 'x': 0}
    return ('', 204)

if __name__ == '__main__':
    app.run(debug=True)
