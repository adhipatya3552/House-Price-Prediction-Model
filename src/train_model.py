import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor


def train_model(df):
    X = df.drop("MEDV", axis=1)
    y = df["MEDV"]

    feature_columns = X.columns

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model 1: Linear Regression
    lr = LinearRegression()
    lr.fit(X_train, y_train)

    # Model 2: Random Forest
    rf = RandomForestRegressor(n_estimators=100)
    rf.fit(X_train, y_train)

    # Choose Random Forest (better usually)
    best_model = rf

    # Save model
    with open("models/model.pkl", "wb") as f:
        pickle.dump((best_model, feature_columns), f)
        
    return best_model, X_test, y_test