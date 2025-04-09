import pandas as pd
from pathlib import Path
from loguru import logger
from joblib import load
from sklearn.model_selection import cross_val_score
from sklearn.compose import TransformedTargetRegressor
import mlflow
import json
import os
import sys
from dotenv import load_dotenv
from sklearn.metrics import mean_absolute_error,r2_score
load_dotenv()

def load_data(data_path: Path) -> pd.DataFrame|None:
    try:
        df = pd.read_csv(data_path)
        return df.dropna()

    except FileNotFoundError:
        logger.error("The file to load does not exist")
        return None

    except Exception as e:
        logger.error(f"error raised: {e}")
        return None

def advance_map(function, series):
    return[
        function(*tup) for tup in series
    ]

def load_model(model_path: Path):
    try:
        model = load(model_path)
        return model

    except FileNotFoundError:
        logger.error("The file to load does not exist")
        return None

    except Exception as e:
        logger.error(f"error raised: {e}")
        return None

def split_data(df: pd.DataFrame) -> tuple[pd.DataFrame,pd.Series]:
    return(
    df.drop(columns='time_taken'),
    df['time_taken']
    )

def cv_score(X_train,y_train,model):
    # calculate cross val scores
    cv_scores = cross_val_score(model,
                                X_train,
                                y_train,
                                cv=5,
                                scoring="neg_mean_absolute_error",
                                n_jobs=-1)
    logger.info("cross validation complete")

    # mean cross val score
    mean = -(cv_scores.mean())
    std = cv_scores.std()
    return mean,std

def save_model_info(save_json_path,run_id, artifact_path, model_name):
    info_dict = {
        "run_id": run_id,
        "artifact_path": artifact_path,
        "model_name": model_name
    }
    with open(save_json_path,"w") as f:
        json.dump(info_dict,f,indent=4)

def evaluate(train_df:pd.DataFrame,test_df:pd.DataFrame,model:TransformedTargetRegressor)->None:

    (X_train,y_train),(X_test,y_test) = map(split_data,[train_df,test_df])

    y_train_pred = model.predict(X_train)
    y_test_pred = model.predict(X_test)

    train_mae,test_mae = advance_map(mean_absolute_error,([y_train,y_train_pred],([y_test,y_test_pred])))
    train_r2_score, test_r2_score = advance_map(r2_score, ([y_train, y_train_pred], ([y_test, y_test_pred])))
    cv_mean_score, cv_std = cv_score(X_train,y_train,model)






    # mlflow tracking setup
    logger.info(f"mlflow tracking setup")
    DAGSHUB_USERNAME = os.getenv("DAGSHUB_USERNAME")
    DAGSHUB_PASSWORD = os.getenv("DAGSHUB_PASSWORD")
    url = f"https://{DAGSHUB_USERNAME}:{DAGSHUB_PASSWORD}@dagshub.com/spynom/my-first-repo.mlflow"
    # mlflow server setup
    mlflow.set_tracking_uri(url)
    mlflow.set_experiment("dvc Pipeline")

    with mlflow.start_run() as run:
        mlflow.log_params(model.get_params())
        mlflow.log_metric("train_mae", train_mae)
        mlflow.log_metric("test_mae", test_mae)
        mlflow.log_metric("train_r2_score", train_r2_score)
        mlflow.log_metric("test_r2_score", test_r2_score)
        mlflow.log_metric("cv_mean_score", cv_mean_score)
        mlflow.log_metric("cv_std", cv_std)

        # model signature
        model_signature = mlflow.models.infer_signature(model_input=X_train.sample(20, random_state=42),
                                                        model_output=model.predict(X_train.sample(20, random_state=42)))

        # log the final model
        mlflow.sklearn.log_model(model, "delivery_time_pred_model", signature=model_signature)

        # get the current run artifact uri
        artifact_uri = mlflow.get_artifact_uri()

        logger.info("Mlflow logging complete and model logged")

        # get the run id
        run_id = run.info.run_id
        model_name = "delivery_time_pred_model"

        # save the model info
        save_json_path =  "run_information.json"
        save_model_info(save_json_path=save_json_path,
                        run_id=run_id,
                        artifact_path=artifact_uri,
                        model_name=model_name)
        logger.info("Model Information saved")



def main():
    logger.info(f"loading data")
    data_path = Path("data")/"interim"/"test.csv",Path("data")/"interim"/"test.csv"
    train_data,test_data = map(load_data,data_path)
    logger.info(f"data loaded")

    logger.info(f"loading model")
    model_path = Path("models")/"model.joblib"
    model = load_model(model_path)
    logger.info(f"model loaded")

    logger.info(f"evaluating model")
    evaluate(train_data,test_data,model)

if __name__ == "__main__":
    # Remove default logger to apply custom format
    logger.remove()

    # Log to the console (terminal)
    logger.add(
        sys.stderr,  # Standard output (console)
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level:<8} | model_evaluation:{function}:{line} - {message}",
        level="INFO",
        colorize=True
    )
    main()