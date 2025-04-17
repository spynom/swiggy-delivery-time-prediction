from dotenv import load_dotenv
import os
import mlflow
load_dotenv()

def load_model():
    # mlflow server setup
    DAGSHUB_USERNAME = os.getenv("DAGSHUB_USERNAME")
    DAGSHUB_PASSWORD = os.getenv("DAGSHUB_PASSWORD")
    url = f"https://{DAGSHUB_USERNAME}:{DAGSHUB_PASSWORD}@dagshub.com/spynom/my-first-repo.mlflow"
    mlflow.set_tracking_uri(url)

    model_path = "models:/delivery_time_pred_model/Staging"
    # load the latest model from model registry
    return mlflow.sklearn.load_model(model_path)