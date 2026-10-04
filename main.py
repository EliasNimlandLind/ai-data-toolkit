import argparse

import pandas as pd

from ai_data_toolkit.statistics import (
    get_descriptive_statistics,
    get_categorical_statistics,
)

def create_parser():
    parser = argparse.ArgumentParser(
        prog="ai-data-toolkit",
        description="Tools for dataset analysis and machine learning workflows.",
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        metavar="COMMAND",
    )

    descriptive_statistics_parser = subparsers.add_parser(
        "descriptive-statistics",
        help="Calculate descriptive statistics for the dataset.",
        description="Calculate descriptive statistics for numerical columns.",
    )

    descriptive_statistics_parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Path to the CSV dataset.",
    )

    descriptive_statistics_parser.set_defaults(function=run_statistics)

    categorical_statistics_parser = subparsers.add_parser(
        "categorical-statistics",
        help="Calculate descriptive statistics for categorical columns.",
        description="Calculate descriptive statistics for categorical columns.",
    )

    categorical_statistics_parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Path to the CSV dataset.",
    )

    categorical_statistics_parser.set_defaults(
        function=run_categorical_statistics
    )

    return parser


def run_statistics(arguments):
    dataframe = pd.read_csv(arguments.file)

    statistics = get_descriptive_statistics(dataframe)

    print(statistics)


def run_categorical_statistics(arguments):
    dataframe = pd.read_csv(arguments.file)

    statistics = get_categorical_statistics(dataframe)

    print(statistics)


def main():
    parser = create_parser()
    arguments = parser.parse_args()

    arguments.function(arguments)


if __name__ == "__main__":
    main()