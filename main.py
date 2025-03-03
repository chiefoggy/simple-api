from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# GET request to fetch a random useless fact
@app.route('/random-fact', methods=['GET'])
def get_random_fact():
    url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
    response = requests.get(url)

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch fact"}), response.status_code
    
# GET request to fetch particulars of a random user data
@app.route('/random-user', methods=['GET'])
def get_random_user():
    url = "https://randomuser.me/api/"
    response = requests.get(url)
    
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch random user data"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
