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
        help=get_descriptive_statistics.__doc__,
        description=get_descriptive_statistics.__doc__
    )

    descriptive_parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="The path to the file containing the dataset."
    )

    categorical_parser = subparsers.add_parser(
        statistics_type.StatisticsType.CATEGORICAL.value,
        help=get_categorical_statistics.__doc__,
        description=get_categorical_statistics.__doc__
    )

    categorical_parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="The path to the file containing the dataset."
    )

    value_counts_parser = subparsers.add_parser(
        statistics_type.StatisticsType.VALUE_COUNTS.value,
        help=get_value_counts.__doc__,
        description=get_value_counts.__doc__
    )

    value_counts_parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="The path to the file containing the dataset."
    )

    value_counts_parser.add_argument(
        "-c",
        "--column",
        required=True,
        help="The name of the column to calculate value counts for."
    )

    value_counts_parser.add_argument(
        "-b",
        "--bar-chart",
        action="store_true",
        help=get_bar_chart.__doc__
    )

    all_statistical_types_parser = subparsers.add_parser(
        statistics_type.StatisticsType.ALL.value,
        description="Calculate all supported statistics."
    )

    all_statistical_types_parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="The path to the file containing the dataset."
    )

    all_statistical_types_parser.add_argument(
        "-c",
        "--column",
        required=True,
        help="The name of the column to calculate value counts for."
    )

    return parser.parse_args()


def main():
    arguments = parse_arguments()

    dataframe = pd.read_csv(arguments.file)

    statistics_to_print = ""

    match arguments.type:
        case statistics_type.StatisticsType.DESCRIPTIVE.value:
            statistics_to_print = get_descriptive_statistics(dataframe)

        case statistics_type.StatisticsType.CATEGORICAL.value:
            statistics_to_print = get_categorical_statistics(dataframe)

        case statistics_type.StatisticsType.VALUE_COUNTS.value:
            if arguments.bar_chart:
                statistics_to_print = get_bar_chart(
                    dataframe,
                    arguments.column
                )
            else:
                statistics_to_print = get_value_counts(
                    dataframe,
                    arguments.column
                )

        case statistics_type.StatisticsType.ALL.value:
            statistics_to_print = (
                f"\n=== Descriptive Statistics ===\n"
                f"\n{get_descriptive_statistics(dataframe)}\n\n"
                f"=== Categorical Statistics ===\n"
                f"\n{get_categorical_statistics(dataframe)}\n\n"
                f"=== Value Counts ===\n\n"
                f"{get_value_counts(dataframe, arguments.column)}\n\n"
                f"=== Value Counts Bar Chart ===\n"
                f"{get_bar_chart(dataframe, arguments.column)}"
            )

    print(statistics_to_print)


if __name__ == "__main__":
    main()