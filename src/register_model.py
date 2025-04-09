import mlflow
from mlflow.tracking import MlflowClient
import json
from loguru import logger
from dotenv import load_dotenv
import os
import sys
load_dotenv()

def load_model_information(file_path):
    with open(file_path) as f:
        run_info = json.load(f)

    return run_info

def main():
    # mlflow server setup
    logger.info(f"mlflow tracking setup")
    DAGSHUB_USERNAME = os.getenv("DAGSHUB_USERNAME")
    DAGSHUB_PASSWORD = os.getenv("DAGSHUB_PASSWORD")
    url = f"https://{DAGSHUB_USERNAME}:{DAGSHUB_PASSWORD}@dagshub.com/spynom/my-first-repo.mlflow"
    mlflow.set_tracking_uri(url)

    run_info_path ="run_information.json"
    # register the model
    run_info = load_model_information(run_info_path)

    # get the run id
    run_id = run_info["run_id"]
    model_name = run_info["model_name"]
    # model to register path
    model_registry_path = f"runs:/{run_id}/{model_name}"

    # register the model
    model_version = mlflow.register_model(model_uri=model_registry_path,
                                          name=model_name)
    # get the model version
    registered_model_version = model_version.version
    registered_model_name = model_version.name
    logger.info(f"The latest model version in model registry is {registered_model_version}")

    # update the stage of the model to staging
    client = MlflowClient()
    client.transition_model_version_stage(
        name=registered_model_name,
        version=registered_model_version,
        stage="Staging"
    )

    logger.info("Model pushed to Staging stage")

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