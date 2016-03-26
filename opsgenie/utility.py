def format_date(dt):
    """
    Converts date time to yyyy-MM-dd HH:mm format
    Parameters
    ----------
    dt : datetime.datetime

    Returns
    -------
    str
    """
    if dt is None:
        return None

    return dt.strftime("%Y-%m-%d %R")


def list_to_str(list_of_str):
    """
    Converts list of string to comma separated string
    Parameters
    ----------
    list_of_str : list of str

    Returns
    -------
    str
    """
    if list_of_str is None:
        return None

    return ','.join(list_of_str)
