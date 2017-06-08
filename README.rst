OpsGenie Python SDK - [BETA]
============================

Aim and Scope
-------------

OpsGenie Python SDK aims to access OpsGenie Web API through HTTP calls from a client application in Python language.

OpsGenie Python SDK covers:

-  Alert API

Future releases are subject to be delivered for packing more APIs soon.

For more information about OpsGenie Python SDK, please refer to
`OpsGenie Python
API <https://www.opsgenie.com/docs/api-and-client-libraries/opsgenie-python-api>`__
document.

Pre-requisites
--------------

-  The API is specifically built for Python 2.7 but can also be used with other Python versions.
-  Before you begin, you need to sign up `OpsGenie <http://www.opsgenie.com>`__ if you don't have a valid
   account yet. Create an API Integration and get your API key.

Installation
------------

To download all packages in the repo with their dependencies, simply execute

``pip install opsgenie-sdk``

Getting Started
---------------

One can start using OpsGenie Python SDK by initializing client and making a request.
Example shown below demonstrates how to initialize our Swagger client and make a create alert request.

::

    from opsgenie.swagger_client import AlertApi
    from opsgenie.swagger_client import configuration
    from opsgenie.swagger_client.models import CreateAlertRequest
    from opsgenie.swagger_client.rest import ApiException

    configuration.api_key['Authorization'] = 'YOUR_API_KEY'
    configuration.api_key_prefix['Authorization'] = 'GenieKey'

    try:
        response = AlertApi().create_alert(body=CreateAlertRequest(message='Hello from OpsGenie Python SDK'))

        print('request id: {}'.format(response.request_id))
        print('took: {}'.format(response.took))
        print('result: {}'.format(response.result))
    except ApiException as err:
        print("Exception when calling AlertApi->create_alert: %s\n" % err)

There are useful sample code snippets under ``samples`` directory for packages. At the moment, we are continuing to support
our old OpsGenie client for creating alerts to new REST API:

::

    from opsgenie import OpsGenie
    from opsgenie.swagger_client import CreateAlertRequest
    from opsgenie.config import Configuration
    from opsgenie.swagger_client.rest import ApiException

    config = Configuration("YOUR_API_KEY")

    client = OpsGenie(config)

    try:
        response = client.alert_v2.create_alert(CreateAlertRequest(message="Hello from OpsGenie Python SDK"))
        print 'message: {}'.format(response.message)
        print 'alert id: {}'.format(response.alert_id)
        print 'status: {}'.format(response.status)
        print 'code: {}'.format(response.code)
    except ApiException as err:
        print("Exception when calling alert_v2->create_alert: %s\n" % err)


The Web API
-----------

Please follow the links below for more information and details about the
Web API.

-  `Alert API <https://www.opsgenie.com/docs/rest-api/alert-api>`__
-  `Alert API (Deprecated) <https://www.opsgenie.com/docs/web-api/alert-api>`__

Bug Reporting and Feature Requests
----------------------------------

If you like to report a bug, or a feature request; please open an issue.
