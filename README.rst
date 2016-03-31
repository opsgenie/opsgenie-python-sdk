OpsGenie Python SDK - [BETA]
===================

Aim and Scope
-------------

OpsGenie Python SDK aims to access OpsGenie Web API through HTTP calls
from a client application in Python language.

OpsGenie Python SDK covers:

-  Alert API
-  Heartbeat API (*TODO: will be available soon*)
-  Integration API (*TODO: will be available soon*)
-  Policy API (*TODO: will be available soon*)

Future releases are subject to be delivered for packing more APIs soon.

For more information about OpsGenie Python SDK, please refer to
`OpsGenie Python
API <https://www.opsgenie.com/docs/api-and-client-libraries/opsgenie-python-api>`__
document.

Pre-requisites
--------------

-  The API is built for Python 2.7 but can also be used with other Python versions.
-  Before you begin, you need to sign up
   `OpsGenie <http://www.opsgenie.com>`__ if you don't have a valid
   account yet. Create an API Integration and get your API key.

Installation
------------

To download all packages in the repo with their dependencies, simply
execute

``pip install opsgenie-sdk``

Getting Started
---------------

One can start using OpsGenie Python SDK by initializing client and
making a request. Example shown below demonstrates how to initialize an
OpsGenie client and make a create alert request.

::

    from opsgenie import OpsGenie
    from opsgenie.alert.requests import CreateAlertRequest
    from opsgenie.config import Configuration
    from opsgenie.errors import OpsGenieError

    config = Configuration("YOUR_API_KEY")

    client = OpsGenie(config)

    try:
        response = client.alert.create_alert(CreateAlertRequest(message="Hello from OpsGenie Python SDK"))
        print 'message: {}'.format(response.message)
        print 'alert id: {}'.format(response.alert_id)
        print 'status: {}'.format(response.status)
        print 'code: {}'.format(response.code)
    except OpsGenieError as err:
        print err.message

There are useful sample code snippets under ``samples`` directory for
packages.

The Web API
-----------

Please follow the links below for more information and details about the
Web API.

-  `Alert API <https://www.opsgenie.com/docs/web-api/alert-api>`__
-  `Heartbeat
   API <https://www.opsgenie.com/docs/web-api/heartbeat-api>`__
-  `Integration
   API <https://www.opsgenie.com/docs/web-api/integration-api>`__
-  `Policy API <https://www.opsgenie.com/docs/web-api/policy-api>`__

Bug Reporting and Feature Requests
----------------------------------

If you like to report a bug, or a feature request; please open an issue.
