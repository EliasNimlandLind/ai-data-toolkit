from enum import Enum

class StatisticsType(Enum):
    DESCRIPTIVE = "descriptive"
    CATEGORICAL = "categorical"
    VALUE_COUNTS = "value_counts"
    CORRELATION = "correlation"
    ALL = "all"
