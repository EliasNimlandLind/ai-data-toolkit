import argparse

import pandas as pd

from ai_data_toolkit import statistics_type
from ai_data_toolkit.statistics import (
    get_descriptive_statistics,
    get_categorical_statistics,
    get_bar_chart,
    get_value_counts
)

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Calculate statistics for a dataset."
    )

    subparsers = parser.add_subparsers(
        dest="type",
        required=True
    )

    descriptive_parser = subparsers.add_parser(
        statistics_type.StatisticsType.DESCRIPTIVE.value,
        description=get_descriptive_statistics.__doc__
    )

    descriptive_parser.add_argument(
        "-f",
        "--file",
        required=True,
        description="The path to the file containing the dataset."
    )

    categorical_parser = subparsers.add_parser(
        statistics_type.StatisticsType.CATEGORICAL.value,
        description=get_categorical_statistics.__doc__
    )

    categorical_parser.add_argument(
        "-f",
        "--file",
        required=True,
        description="The path to the file containing the dataset."
    )

    value_counts_parser = subparsers.add_parser(
        statistics_type.StatisticsType.VALUE_COUNTS.value,
        description=get_value_counts.__doc__
    )

    value_counts_parser.add_argument(
        "-f",
        "--file",
        required=True,
        description="The path to the file containing the dataset."
    )

    value_counts_parser.add_argument(
        "-c",
        "--column",
        required=True,
        description="The name of the column to calculate value counts for."
    )

    value_counts_parser.add_argument(
        "-b",
        "--bar-chart",
        action="store_true",
        description=get_bar_chart.__doc__
    )

    all_parser = subparsers.add_parser(
        statistics_type.StatisticsType.ALL.value,
        description="Calculate all dataset-level statistics."
    )

    all_parser.add_argument(
        "-f",
        "--file",
        required=True,
        description="The path to the file containing the dataset."
    )

    return parser.parse_args()

def main():
    arguments = parse_arguments()

    dataframe = pd.read_csv(arguments.file)

    if arguments.type == statistics_type.StatisticsType.DESCRIPTIVE.value:
        statistics = get_descriptive_statistics(dataframe)

    elif arguments.type == statistics_type.StatisticsType.CATEGORICAL.value:
        statistics = get_categorical_statistics(dataframe)

    elif arguments.type == statistics_type.StatisticsType.VALUE_COUNTS.value:
        if arguments.bar_chart:
            statistics = get_bar_chart(
                dataframe,
                arguments.column
            )
        else:
            statistics = get_value_counts(
                dataframe,
                arguments.column
            )

    elif arguments.type == statistics_type.StatisticsType.ALL.value:
        statistics = (
            f"\n=== Descriptive Statistics ===\n"
            f"{get_descriptive_statistics(dataframe)}\n\n"
            f"=== Categorical Statistics ===\n"
            f"{get_categorical_statistics(dataframe)}"
        )

    print(statistics)

if __name__ == "__main__":
    main()