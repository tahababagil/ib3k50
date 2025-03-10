from flask import Flask, render_template, request
from regression import predict_price 
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    predicted_price = None
    quality = None
    if request.method == "POST":
        try:
            wineType = request.form.get("wineType", "red").lower()
            fixedAcidity = float(request.form.get("fixedAcidity", 0))
            volatileAcidity = float(request.form.get("volatileAcidity", 0))
            citricAcid = float(request.form.get("citricAcid", 0))
            residualSugar = float(request.form.get("residualSugar", 0))
            chlorides = float(request.form.get("chlorides", 0))
            freeSulfurDioxide = float(request.form.get("freeSulfurDioxide", 0))
            totalSulfurDioxide = float(request.form.get("totalSulfurDioxide", 0))
            density = float(request.form.get("density", 0))
            pH = float(request.form.get("pH", 0))
            sulphates = float(request.form.get("sulphates", 0))
            alcohol = float(request.form.get("alcohol", 0))
            predicted_price, quality = predict_price(wineType, fixedAcidity, volatileAcidity, citricAcid, residualSugar, chlorides, freeSulfurDioxide, totalSulfurDioxide, density, pH, sulphates, alcohol)
            quality = round(quality,1)
            predicted_price = round(predicted_price,2)
        except Exception as e:
            predicted_price = "Error: invalid input"
    return render_template("index.html", price=predicted_price, quality=quality)

if __name__ == "__main__":
    app.run(debug=True)
