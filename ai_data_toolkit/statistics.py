
import pandas as pd

def get_descriptive_statistics(dataframe):
    """Calculate descriptive statistics for a dataset."""
    return dataframe.describe()

def get_categorical_statistics(dataframe):
    """Calculate descriptive statistics for categorical columns."""
    return dataframe.describe(include="object")

def get_value_counts(dataframe, column):
    """Get the value counts for a specific column in the dataset."""
    return dataframe[column].value_counts()

def get_bar_chart(dataframe, column, max_bar_length=100, padding_between_bar_and_category=15):
    """Create a bar chart showing the frequency of values in a column."""
    value_counts = get_value_counts(dataframe, column)
    max_value_count = value_counts.max()
    bar_chart_string = ""

    for current_category, current_count in value_counts.items():
        current_bar_length = int((current_count / max_value_count) * max_bar_length)
        current_bar = "█" * current_bar_length

        bar_chart_string += f"\n{current_category:<{padding_between_bar_and_category}} {current_bar} {current_count}\n"

    return bar_chart_string