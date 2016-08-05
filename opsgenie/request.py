from .errors import InvalidRequestError
from six import string_types


def required(attr):
    """

    Parameters
    ----------
    attr : str

    Returns
    -------

    """

    def wrapper(func):
        def validate(self):
            if getattr(self, attr, None) is None:
                raise InvalidRequestError("'{0}' property is required.".format(attr))
            return func(self)

        return validate

    return wrapper


def required_one_of(attrs):
    """

    Parameters
    ----------
    attrs : list of str

    Returns
    -------

    """

    def wrapper(func):
        def validate(self):
            attr_count = 0
            for attr in attrs:
                attr_value = getattr(self, attr, None)
                if attr_value is not None and attr_value is not '':
                    attr_count += 1
            if attr_count > 1:
                raise InvalidRequestError("Specify only one of '{0}' properties.".format(attrs))
            elif attr_count == 0:
                raise InvalidRequestError("One of '{0}' properties is required.".format(attrs))

            return func(self)

        return validate

    return wrapper


def should_be_one_of(attr, values):
    """

    Parameters
    ----------
    attr : str
    values : list of str

    Returns
    -------

    """

    def wrapper(func):
        def validate(self):
            if getattr(self, attr, None) is not None:
                if not (getattr(self, attr).lower() in (value.lower() for value in values)):
                    raise InvalidRequestError(
                        "'{0}' property should be one of '{1}'. Current value: '{2}'.".format(attr, values,
                                                                                              getattr(self, attr)))
            return func(self)

        return validate

    return wrapper


def max_value(attr, value):
    """

    Parameters
    ----------
    attr : int or str
    value : int

    Returns
    -------

    """

    def wrapper(func):
        def validate(self):
            if hasattr(self, attr):
                attr_val = getattr(self, attr)
                if isinstance(attr_val, int) and attr_val > value:
                    raise InvalidRequestError(
                        "'{0}' property should be lower than '{1}'. Current value: '{2}'.".format(attr, value,
                                                                                                  attr_val))
                elif isinstance(attr_val, string_types) and len(attr_val) > value:
                    raise InvalidRequestError(
                        "'{0}' property should be lower than '{1}' characters. Current value: '{2}', len'{3}'.".format(
                            attr,
                            value,
                            attr_val,
                            len(attr_val)))
                return func(self)

        return validate

    return wrapper


class BaseRequest:
    def __init__(self):
        pass

    def validate(self):
        """
        Validates request simply

        Raises
        -------
        InvalidRequestError
        """
        pass

    def decode(self):
        """
        Generates api request parameters from Request object

        Returns
        -------
        dict
        """
        return self.__dict__.copy()
