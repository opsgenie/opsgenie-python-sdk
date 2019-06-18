import abc


class Observer(abc.ABC):
    """
    An updating interface for objects, to whom metrics should be published.
    The published metrics can be accessed in a named tuple at publisher.data in the notify function.
    """

    @abc.abstractmethod
    def notify(self, publisher):
        pass
