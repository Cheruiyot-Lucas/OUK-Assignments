from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

def run_jac(text):
    # Run the Jac walker (Jac 0.8.8 syntax)
    cmd = [
        "jac",
        "run",
        "ai_calculator.jac",
        "--walk",
        "smart_calc.process",
        "--input",
        text
    ]
    try:
        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, text=True)
        return result.strip()
    except subprocess.CalledProcessError as e:
        return f"Error running Jac: {e.output}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    text = data.get('text', '')
    result = run_jac(text)
    return jsonify({'result': result})

# 🚀 Make sure Flask actually runs:
if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(host='127.0.0.1', port=5000, debug=True)
