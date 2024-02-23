from datetime import datetime
from utils.date_utils import convert_datetime_to_utc
def path_to_parquet(table_name: str, counter: int) -> str:
    """
    Generates a file path for storing a Parquet file.

    Args:
        `table_name`: The name of the table.
        `counter`: An integer counter for versioning or distinguishing files.

    Returns:
        `str`: A string representing the file path in the format:
            "{table_name}/{table_name}__[#{counter}]__{date}.parquet"
            where {table_name} is the name of the table,
            {counter} is the version or counter value,
            and {date} is the current UTC datetime converted to string.
    """
    date = convert_datetime_to_utc(datetime.now())
    return f"{table_name}/{table_name}__[#{counter}]__{date}.parquet"