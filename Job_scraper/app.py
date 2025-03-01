from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

jobs = []  # Store jobs in-memory (Temporary)

@app.route('/')
def home():
    return render_template('index.html')  # Loads the frontend

@app.route('/jobs', methods=['GET', 'POST'])
def job_list():
    if request.method == 'POST':
        data = request.json
        jobs.append({
            "title": data["title"],
            "company": data["company"],
            "location": data["location"]
        })
        return jsonify({"message": "Job added successfully"}), 201
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)
