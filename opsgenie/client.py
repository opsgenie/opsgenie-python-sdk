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

    @property
    def alert(self):
        """

        Returns
        -------
        AlertService
        """
        return self._alert
