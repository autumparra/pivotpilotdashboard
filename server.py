from flask import Flask, jsonify
from flask_cors import CORS
import json
from fetch_emails import fetch_recent_emails
from fetch_indeed import fetch_indeed_jobs

app = Flask(__name__)
CORS(app)

@app.route('/api/data')
def get_data():
    with open('data.json', 'r') as f:
        data = json.load(f)

    # Pull real Gmail emails
    real_emails = fetch_recent_emails(limit=8)
    data['realEmails'] = real_emails

    # Pull Indeed jobs
    indeed_jobs = fetch_indeed_jobs(query="entry level cybersecurity remote", limit=8)
    data['indeedJobs'] = indeed_jobs

    return jsonify(data)

if __name__ == '__main__':
    print("🚀 Pivot Pilot server running at http://127.0.0.1:5000")
    app.run(port=5000, debug=True)