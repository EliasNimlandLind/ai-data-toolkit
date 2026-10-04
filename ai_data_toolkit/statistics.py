
import pandas as pd

def calculate_descriptive_statistics(dataframe):
    """Calculate descriptive statistics for a dataset."""
    return dataframe.describe()

def calculate_categorical_statistics(dataframe):
    """Calculate descriptive statistics for categorical columns."""
    return dataframe.describe(include="object")

def get_bar_chart(dataframe, column, max_bar_length=100):
    """Create a bar chart showing the frequency of values in a column."""
    value_counts = dataframe[column].value_counts()
    maximum_count = value_counts.max()
    bar_chart_string = ""

    for category, count in value_counts.items():
        bar_length = int((count / maximum_count) * max_bar_length)
        bar = "█" * bar_length

        bar_chart_string += f"\n{category:<15} {bar} {count}\n"

    return bar_chart_string