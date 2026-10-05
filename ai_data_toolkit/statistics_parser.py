import argparse

from ai_data_toolkit import statistics_type
from ai_data_toolkit.statistics import (
    get_all_statistics,
    get_correlation_matrix,
    get_descriptive_statistics,
    get_categorical_statistics,
    get_bar_chart,
    get_value_counts
)

def add_source_file_argument(parser):
    """Add the file argument to a parser."""
    parser.add_argument(
        "-s",
        "--source-file",
        required=True,
        help="The path to the file containing the dataset."
    )

def add_output_file_argument(parser):
    """Add the output file argument to a parser."""
    parser.add_argument(
        "-o",
        "--output-file",
        dest="output_file",
        help="The path to the CSV file where the output should be saved."
    )

def add_column_argument(parser, required=False):
    """Add the column argument to a parser."""
    parser.add_argument(
        "-c",
        "--column",
        required=required,
        help=get_value_counts.__doc__
    )

def get_parsed_arguments():
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

    add_source_file_argument(descriptive_parser)
    add_output_file_argument(descriptive_parser)

    categorical_parser = subparsers.add_parser(
        statistics_type.StatisticsType.CATEGORICAL.value,
        help=get_categorical_statistics.__doc__,
        description=get_categorical_statistics.__doc__
    )

    add_source_file_argument(categorical_parser)
    add_output_file_argument(categorical_parser)

    value_counts_parser = subparsers.add_parser(
        statistics_type.StatisticsType.VALUE_COUNTS.value,
        help=get_value_counts.__doc__,
        description=get_value_counts.__doc__
    )

    add_source_file_argument(value_counts_parser)
    add_output_file_argument(value_counts_parser)
    add_column_argument(value_counts_parser, required=True)

    value_counts_parser.add_argument(
        "-b",
        "--bar-chart",
        action="store_true",
        help=get_bar_chart.__doc__
    )

    correlation_parser = subparsers.add_parser(
    "correlation",
    help=get_correlation_matrix.__doc__,
    description=get_correlation_matrix.__doc__
    )
    
    add_source_file_argument(correlation_parser)
    add_output_file_argument(correlation_parser)

    all_parser = subparsers.add_parser(
        statistics_type.StatisticsType.ALL.value,
        description=get_all_statistics.__doc__,
        help=get_all_statistics.__doc__
    )

    add_source_file_argument(all_parser)
    add_column_argument(all_parser, required=True)

    return parser.parse_args()