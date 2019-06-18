import logging


class Publisher:
    """
    A base Publisher class to contain the common functionality
    of adding, removing, and notifying observers
    """

    def __init__(self):
        self.observers = []
        self.logger = logging.getLogger('opsgenie_sdk')

    def subscribe(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)
            self.logger.debug('Observer subscribed')
        else:
            print('Failed to subscribe: {}'.format(observer))

    def unsubscribe(self, observer):
        try:
            self.observers.remove(observer)
            self.logger.debug('Observer unsubscribed')
        except ValueError:
            print('Failed to unsubscribe: {}'.format(observer))

    def notify(self):
        [o.notify(self) for o in self.observers]
