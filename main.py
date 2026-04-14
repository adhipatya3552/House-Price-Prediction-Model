from src.data_processing import preprocess_data
from src.feature_engineering import feature_engineering
from src.train_model import train_model
from src.evaluate_model import evaluate


def main():
    data_path = "data/boston.csv"

    df = preprocess_data(data_path)
    df = feature_engineering(df)

    model, X_test, y_test = train_model(df)
    evaluate(model, X_test, y_test)


if __name__ == "__main__":
    main()