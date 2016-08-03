from .alert.service import AlertService
from .config import Configuration


class OpsGenie:
    def __init__(self, configuration):
        """
        Init OpsGenie client to interact with OpsGenie Api

        Parameters
        ----------
        configuration : Configuration
        """
        configuration.validate()
        OpsGenie.configuration = configuration

        self._alert = AlertService(configuration)
        self._heartbeat = None
        self._integration = None
        self._policy = None

    @property
    def alert(self):
        """

        Returns
        -------
        AlertService
        """
        return self._alert

    @property
    def heartbeat(self):
        raise NotImplementedError()

    @property
    def integration(self):
        raise NotImplementedError()

    @property
    def policy(self):
        raise NotImplementedError()
