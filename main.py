from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/main.py', methods=['POST'])
def predict_wine_price():
    # Get the JSON data from the request
    data = request.get_json()
    
    # For demonstration purposes, calculate a dummy price by summing all the provided feature values.
    # In a real scenario, you'd likely run a trained model here.
    try:
        features = [
            data.get("fixedAcidity", 0),
            data.get("volatileAcidity", 0),
            data.get("citricAcid", 0),
            data.get("residualSugar", 0),
            data.get("chlorides", 0),
            data.get("freeSulfurDioxide", 0),
            data.get("totalSulfurDioxide", 0),
            data.get("density", 0),
            data.get("pH", 0),
            data.get("sulphates", 0),
            data.get("alcohol", 0)
        ]
        # Sum the features and cast the result to an integer
        predicted_price = int(sum(features))
    except Exception as e:
        predicted_price = 0  # Fallback value in case of error

    # Return the predicted price in a JSON response
    return jsonify({"price": predicted_price})

if __name__ == '__main__':
    # Run the Flask app locally with debugging enabled
    app.run(debug=True)
