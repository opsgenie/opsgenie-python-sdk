import json

from opsgenie.response import BaseResponse
from opsgenie.tests import OpsGenieTestCase


class TestResponse(OpsGenieTestCase):
    def test_response_from_json(self):
        class Response(BaseResponse):
            def __init__(self, json_str):
                BaseResponse.__init__(self, json_str)
                self.key = self.pop('key1')

                self.decode()

        json_str = json.dumps({'key1': 'value1', 'key2': 'value2'})

        response = Response(json_str)
        self.assertEqual('value1', response.key)
        self.assertEqual('value2', getattr(response, 'key2'))
        self.assertIsNone(getattr(response, 'key1', None), 'key1 should be None as it has been popped out in init')
