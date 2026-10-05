import pandas as pandas

from ai_data_toolkit.statistics_parser import get_parsed_arguments
from ai_data_toolkit import statistics_type
from ai_data_toolkit.statistics import (
    get_all_statistics,
    get_descriptive_statistics,
    get_categorical_statistics,
    get_bar_chart,
    get_value_counts,
    get_correlation_matrix,
)

def main():
    arguments = get_parsed_arguments()

    try:
        dataframe = pandas.read_csv(arguments.source_file)

        statistics_to_print = ""

        match arguments.type:
            case statistics_type.StatisticsType.DESCRIPTIVE.value:
                statistics_to_print = f"\n\n{get_descriptive_statistics(dataframe)}"

            case statistics_type.StatisticsType.CATEGORICAL.value:
                statistics_to_print = f"\n\n{get_categorical_statistics(dataframe)}"

            case statistics_type.StatisticsType.VALUE_COUNTS.value:
                if arguments.bar_chart:
                    statistics_to_print = f"\n\n{get_bar_chart(
                        dataframe,
                        arguments.column
                    )}"
                else:
                    statistics_to_print = f"\n{get_value_counts(
                        dataframe,
                        arguments.column
                    )}"

            case statistics_type.StatisticsType.CORRELATION.value:
                statistics_to_print = f"\n\n{get_correlation_matrix(dataframe)}"

            case statistics_type.StatisticsType.ALL.value:
                statistics_to_print = f"\n\n{get_all_statistics(
                    dataframe,
                    arguments.column
                )}"

        if arguments.output_file:
            file_mode = "a" if arguments.output_mode == "append" else "w"

            with open(
                arguments.output_file,
                file_mode,
                encoding="utf-8"
            ) as file:
                file.write(statistics_to_print)

        print(statistics_to_print)

    except FileNotFoundError:
        print(
            f"Error: The file '{arguments.file}' was not found."
        )

if __name__ == "__main__":
    main()