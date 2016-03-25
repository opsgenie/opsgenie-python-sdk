import random
import string


def random_str(n, prefix=""):
    """

    Parameters
    ----------
    n : int
    prefix : str

    Returns
    -------
    str
    """
    return prefix.join(random.choice(string.ascii_letters) for _ in range(n))
