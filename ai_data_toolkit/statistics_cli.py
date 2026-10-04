import argparse

import pandas as pd

from ai_data_toolkit.statistics import (
    get_descriptive_statistics,
    get_categorical_statistics,
    get_bar_chart,
    get_value_counts
)
from ai_data_toolkit.statistics_type import StatisticsType

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Calculate statistics for a dataset."
    )

    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="The path to the file containing the dataset.",
    )

    parser.add_argument(
        "-t",
        "--type",
        choices=[StatisticsType.DESCRIPTIVE.value,
                 StatisticsType.CATEGORICAL.value, 
                 StatisticsType.VALUE_COUNTS.value, 
                 StatisticsType.ALL.value],
        default=StatisticsType.DESCRIPTIVE.value,
        help="The type of statistics to calculate.",
    )

    parser.add_argument(
    "-c",
    "--column",
    help="The name of the column to base the chart on.",
    )

    parser.add_argument(
    "-b",
    "--bar-chart",
    action="store_true",
    help="Display value counts as a bar chart."
    )

    return parser.parse_args()

def main():
    arguments = parse_arguments()

    dataframe = pd.read_csv(arguments.file)

    match arguments.type:
        case StatisticsType.DESCRIPTIVE.value:
            statistics = get_descriptive_statistics(dataframe)
        
        case StatisticsType.CATEGORICAL.value:
            statistics = get_categorical_statistics(dataframe)
        
        case StatisticsType.VALUE_COUNTS.value:
            if not arguments.column:
                print(
                    "\x1b[31m"
                    "Error: --column is required when using value_counts."
                    "\x1b[0m"
                )
                return

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
            
        case StatisticsType.ALL.value:
            statistics = (f"\n{str(get_descriptive_statistics(dataframe))}\n\n"
                          f"{str(get_categorical_statistics(dataframe))}\n"
                          f"{get_bar_chart(dataframe, arguments.column)}")

    print(statistics)

if __name__ == "__main__":
    main()