import pandas as pd

def predict_price(wineType : str, fixedAcidity, volatileAcidity, citricAcid, residualSugar, chlorides, freeSulfurDioxide, totalSulfurDioxide, density, pH, sulphates, alcohol):
    
    data = {
        'fixed acidity': fixedAcidity,
        'volatile acidity': volatileAcidity,
        'citric acid': citricAcid,
        'residual sugar': residualSugar,
        'chlorides': chlorides,
        'free sulfur dioxide': freeSulfurDioxide,
        'total sulfur dioxide': totalSulfurDioxide,
        'density': density,
        'pH': pH,
        'sulphates': sulphates,
        'alcohol': alcohol
    }

    df = pd.DataFrame([data])

    if wineType.strip() == "red":
        model = pd.read_pickle("red_tree_quality.pkl")
        rating = model.predict(df)[0]
        # prices = pd.read_pickle("red_price.pkl")
        fit_red = pd.read_pickle("red_pred.pkl")
        price = fit_red[0] * rating + fit_red[1]
        price = price if price >= 3 else 3
        return price, rating
    else:
        model = pd.read_pickle("white_tree_quality.pkl")
        rating = model.predict(df)[0]
        # prices = pd.read_pickle("white_price.pkl")
        fit_white = pd.read_pickle("white_pred.pkl")
        price = fit_white[0] * rating + fit_white[1]
        price = price if price >= 3 else 3
        return price, rating
        # print(prices.loc[(prices['Rating'] > rating - 0.5) & (prices['Rating'] < rating + 0.5)]['Price'])
        return prices.loc[(prices['Rating'] > rating - 0.5) & (prices['Rating'] < rating + 0.5)]['Price'].mean(), rating


# predict_price('white',0,0,0,0,0,0,0,0,0,0,0)