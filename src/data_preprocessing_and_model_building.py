from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, PowerTransformer, OrdinalEncoder
from pathlib import Path
from sklearn.compose import TransformedTargetRegressor
from sklearn.pipeline import Pipeline
from lightgbm import LGBMRegressor
import yaml
from loguru import logger
import sys
import pandas as pd
from joblib import dump


def read_params(file_path):
    with open(file_path, "r") as f:
        params_file = yaml.safe_load(f)

    return params_file

def load_data(data_path: Path) -> pd.DataFrame:
    try:
        df = pd.read_csv(data_path)
        return df.dropna()

    except FileNotFoundError:
        logger.error("The file to load does not exist")



def train_model(model, df):
    X = df.drop(columns='time_taken')
    y = df['time_taken']

    model.fit(X, y)
    return model


def model_pipeline(n_estimators: int = 100, learning_rate: float = 0.02, max_depth: int = 3):
    # do basic preprocessing

    num_cols = ["age", "ratings", "pickup_time_minutes", "distance"]

    nominal_cat_cols = ['weather', 'type_of_order',
                        'type_of_vehicle', "festival",
                        "city_type",
                        "is_weekend",
                        "order_time_of_day"]

    ordinal_cat_cols = ["traffic", "distance_type"]

    # generate order for ordinal encoding

    traffic_order = ["low", "medium", "high", "jam"]

    distance_type_order = ["short", "medium", "long", "very_long"]

    # build a preprocessor

    preprocessor = ColumnTransformer(transformers=[
        ("scale", MinMaxScaler(), num_cols),
        ("nominal_encode", OneHotEncoder(drop="first", handle_unknown="ignore", sparse_output=False), nominal_cat_cols),
        ("ordinal_encode", OrdinalEncoder(categories=[traffic_order, distance_type_order]), ordinal_cat_cols)
    ], remainder="passthrough", n_jobs=-1, force_int_remainder_cols=False, verbose_feature_names_out=False)

    model = TransformedTargetRegressor(
        regressor=LGBMRegressor(
            n_estimators=n_estimators,
            learning_rate=learning_rate,
            max_depth=max_depth,
        ),
        transformer=PowerTransformer(),
    )
    return Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", model)
    ])

def save_model(model: TransformedTargetRegressor, file_path: Path):
    dump(model, file_path)

def main():
    # parameters file
    params_file_path = "params.yaml"
    # read the parameters
    parameters = read_params(params_file_path)['Data_preprocess_and_model_training']
    logger.info("parameters read successfully")

    # data file
    file_path = Path("data") / "interim" / "train.csv"
    logger.info("loading data from: {}".format(file_path))
    loaded_df = load_data(file_path)
    logger.info("loaded data successfully")

    # model
    logger.info("loading and training model piepline")
    model = model_pipeline(n_estimators=parameters['n_estimators'],
                           learning_rate=parameters['learning_rate'],
                           max_depth=parameters['max_depth'])


    trained_model = train_model(model, loaded_df)
    logger.info("trained model successfully")

    # save_path of model
    save_path =Path("models")/"model.joblib"
    save_model(trained_model, save_path)
    logger.info("model saved successfully")

if __name__ == "__main__":
    # Remove default logger to apply custom format
    logger.remove()

    # Log to the console (terminal)
    logger.add(
        sys.stderr,  # Standard output (console)
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level:<8} | data_preprocessing_and_model_building:{function}:{line} - {message}",
        level="INFO",
        colorize=True
    )
    main()