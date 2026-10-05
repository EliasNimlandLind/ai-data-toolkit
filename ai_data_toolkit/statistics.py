import pandas as pandas

def validate_dataframe(dataframe):
    """Validate that the input is a non-empty pandas DataFrame."""
    if not isinstance(dataframe, pandas.DataFrame):
        raise TypeError("dataframe must be a pandas DataFrame.")

    if dataframe.empty:
        raise ValueError("The dataset is empty.")

def validate_column(dataframe, column):
    """Validate that a column exists in the dataset."""
    validate_dataframe(dataframe)

    if not isinstance(column, str):
        raise TypeError("column must be a string.")
    
    if column not in dataframe.columns:
        raise ValueError(
            f"Column '{column}' does not exist in the dataset. "
            f"Available columns: {list(dataframe.columns)}"
        )

def get_descriptive_statistics(dataframe):
    """Calculate descriptive statistics for a dataset."""
    validate_dataframe(dataframe)

    return dataframe.describe()

def get_categorical_statistics(dataframe):
    """Calculate descriptive statistics for categorical columns."""
    validate_dataframe(dataframe)

    return dataframe.describe(include="object")

def get_value_counts(dataframe, column):
    """Get the value counts for a specific column in the dataset."""
    validate_column(dataframe, column)

    return dataframe[column].value_counts()

def get_bar_chart(
    dataframe,
    column,
    max_bar_length=50,
    amount_of_padding_between_bar_and_category=15
):
    """Create a bar chart showing the frequency of values in a column."""
    validate_column(dataframe, column)

    if not isinstance(max_bar_length, int):
        raise TypeError("max_bar_length must be an integer.")

    if max_bar_length <= 0:
        raise ValueError("max_bar_length must be greater than 0.")

    if not isinstance(amount_of_padding_between_bar_and_category, int):
        raise TypeError(
            "padding_between_bar_and_category must be an integer."
        )

    if amount_of_padding_between_bar_and_category < 0:
        raise ValueError(
            "padding_between_bar_and_category cannot be negative."
        )

    value_counts = get_value_counts(dataframe, column)
    max_value_count = value_counts.max()

    bar_chart_text = ""
    for current_category, current_count in value_counts.items():
        current_bar_length = int(
            (current_count / max_value_count) * max_bar_length
        )

        current_bar = "█" * current_bar_length

        bar_chart_text += (
            f"\n"
            f"{current_category:<{amount_of_padding_between_bar_and_category}} "
            f"{current_bar} "
            f"{current_count}\n"
        )

    return bar_chart_text

def get_correlation_matrix(dataframe):
    """
    Calculate the correlation matrix for numerical columns.

    Correlation coefficients range from -1 to +1:

    +1.0          Perfect positive correlation
    -1.0          Perfect negative correlation

    Positive correlation means that two variables tend to increase
    together. Negative correlation means that one variable tends to
    decrease as the other increases.
    """
    validate_dataframe(dataframe)

    return dataframe.corr(numeric_only=True)

def get_all_statistics(dataframe, column):
    """Get all statistics for a dataset."""
    validate_dataframe(dataframe)
    validate_column(dataframe, column)

    descriptive_statistics = get_descriptive_statistics(dataframe)
    categorical_statistics = get_categorical_statistics(dataframe)
    value_counts = get_value_counts(dataframe, column)
    bar_chart = get_bar_chart(dataframe, column)

    all_statistics_as_string = (
        f"\n=== Descriptive Statistics ===\n"
        f"\n{descriptive_statistics}\n\n"
        f"=== Categorical Statistics ===\n"
        f"\n{categorical_statistics}\n\n"
        f"=== Value Counts ===\n\n"
        f"{value_counts}\n\n"
        f"=== Value Counts Bar Chart ===\n"
        f"{bar_chart}"
    )

    return all_statistics_as_string