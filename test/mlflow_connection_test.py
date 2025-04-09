import pytest
import mlflow
import os
import warnings
from dotenv import load_dotenv
from loguru import logger
import sys

# Suppress Pydantic deprecation warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

load_dotenv()
DAGSHUB_USERNAME = os.getenv("DAGSHUB_USERNAME")
DAGSHUB_PASSWORD = os.getenv("DAGSHUB_PASSWORD")

# Remove default logger to apply custom format
logger.remove()

# Log to the console (terminal)
logger.add(
    sys.stderr,  # Standard output (console)
    format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level:<8} | model_evaluation:{function}:{line} - {message}",
    level="INFO",
    colorize=True
)
def test_mlflow_connection():
    """Test DAGsHub MLflow tracking server connection."""
    try:
        # Authenticate with DAGsHub (if necessary)
        mlflow.set_tracking_uri(f"https://{DAGSHUB_USERNAME}:{DAGSHUB_PASSWORD}@dagshub.com/spynom/my-first-repo.mlflow")

        experiment_name = "test_experiment_dagshub"
        mlflow.set_experiment(experiment_name)

        with mlflow.start_run():
            mlflow.log_param("param1", 10)
            mlflow.log_metric("metric1", 0.95)
            run_id = mlflow.active_run().info.run_id
            assert run_id is not None, "Run ID should not be None"

        # Ensure the experiment exists
        experiment = mlflow.get_experiment_by_name(experiment_name)
        assert experiment is not None, "Experiment should exist in MLflow"

    except Exception as e:
        pytest.fail(f"MLflow connection test failed: {e}")
