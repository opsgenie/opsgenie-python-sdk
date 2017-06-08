from .alert.service import AlertService
from .config import Configuration
from .swagger_client import AlertApi


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
        self._alert_v2 = AlertApi()

    @property
    def alert(self):
        """

        Returns
        -------
        AlertService
        """
        return self._alert

    @property
    def alert_v2(self):
        """

        Returns
        -------
        AlertApi
        """
        return self._alert_v2
