from pathlib import Path
import pandas as pd
import yaml
from loguru import logger
import sys
from sklearn.model_selection import train_test_split
import os

def load_data(data_path: Path) -> pd.DataFrame:
    try:
        df = pd.read_csv(data_path)

    except FileNotFoundError:
        logger.error("The file to load does not exist")

    return df


def split_data(data: pd.DataFrame, test_size: float, random_state: int):
    train_data, test_data = train_test_split(data,
                                             test_size=test_size,
                                             random_state=random_state)

    return train_data, test_data


def read_params(file_path):
    with open(file_path, "r") as f:
        params_file = yaml.safe_load(f)

    return params_file


def save_data(data: pd.DataFrame, save_path: Path) -> None:
    data.to_csv(save_path, index=False)


def main():
    # parameters file
    params_file_path = "params.yaml"
    # read the parameters
    parameters = read_params(params_file_path)['Data_Preparation']
    test_size = parameters['test_size']
    random_state = parameters['random_state']
    logger.info("parameters read successfully")

    # data file
    file_path = Path("data") / "cleaned" / "swiggy_cleaned.csv"
    logger.info("loading data from: {}".format(file_path))
    loaded_df = load_data(file_path)

    # split data
    train_data, test_data = split_data(loaded_df, test_size=test_size, random_state=random_state)
    logger.info("Dataset split into train and test data")

    # save train and test data
    save_data_dir = Path("data") / "interim"
    save_data_dir.mkdir(parents=True, exist_ok=True)
    # filenames
    train_filename = "train.csv"
    test_filename = "test.csv"
    # save path for train and test
    save_train_path = save_data_dir / train_filename
    save_test_path = save_data_dir / test_filename

    # save the train and test data
    data_subsets = [train_data, test_data]
    data_paths = [save_train_path, save_test_path]
    filename_list = [train_filename, test_filename]
    for filename, path, data in zip(filename_list, data_paths, data_subsets):
        save_data(data=data, save_path=path)
        logger.info(f"{filename.replace(".csv", "")} data saved to location")

if __name__ == "__main__":
    # Remove default logger to apply custom format
    logger.remove()

    # Log to the console (terminal)
    logger.add(
        sys.stderr,  # Standard output (console)
        format="{time:YYYY-MM-DD HH:mm:ss.SSS} | {level:<8} | data_preparation:{function}:{line} - {message}",
        level="INFO",
        colorize=True
    )
    main()