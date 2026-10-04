import argparse

import pandas as pd

from ai_data_toolkit.statistics import (
    calculate_descriptive_statistics,
    calculate_categorical_statistics,
    get_bar_chart
)

def parse_arguments():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Calculate statistics for a CSV dataset."
    )

    parser.add_argument(
        "-f",
        "--file",
        required=True,
        help="Path to the CSV dataset.",
    )

    parser.add_argument(
        "-t",
        "--type",
        choices=["descriptive", "categorical", "chart"],
        default="descriptive",
        help="Type of statistics to calculate.",
    )

    parser.add_argument(
    "-c",
    "--column",
    help="The name of the column to base the chart on.",
    )

    return parser.parse_args()

def main():
    arguments = parse_arguments()

    dataframe = pd.read_csv(arguments.file)

    match arguments.type:
        case "descriptive":
            statistics = calculate_descriptive_statistics(dataframe)
        case "categorical":
            statistics = calculate_categorical_statistics(dataframe)
        case "chart":
            if not arguments.column:
                print("\x1b[31mError: --column is required when using chart.\x1b[0m")
                return

            statistics = get_bar_chart(dataframe, arguments.column)

    print(statistics)

if __name__ == "__main__":
    main()