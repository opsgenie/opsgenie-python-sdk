from opsgenie.errors import InvalidRequestError
from opsgenie.request import BaseRequest, required, required_one_of, should_be_one_of, max_value
from opsgenie.tests import OpsGenieTestCase


class TestRequest(OpsGenieTestCase):
    def test_request_from_json(self):
        class Request(BaseRequest):
            def __init__(self, id=None, alias=None, tiny_id=None, order_by=None, count=None, text=None, details=None):
                """

                Parameters
                ----------
                id : str
                alias : str
                tiny_id : six.string_types
                order_by
                count
                text
                details
                """
                BaseRequest.__init__(self)
                self.id = id
                self.alias = alias
                self.tiny_id = tiny_id
                self.order_by = order_by
                self.count = count
                self.text = text
                self.details = details

            @required('id')
            @required_one_of(['alias', 'tiny_id'])
            @should_be_one_of('order_by', ['asc', 'desc'])
            @max_value('count', 50)
            @max_value('text', 10)
            def validate(self):
                pass

            def decode(self):
                return {
                    'id': self.id,
                    'count': self.count,
                    'details': self.details
                }

        request = Request()
        with self.assertRaisesRegexp(InvalidRequestError, ".* property is required"):
            request.validate()

        request = Request(id='id1')
        with self.assertRaisesRegexp(InvalidRequestError, "One of .* properties is required"):
            request.validate()

        request = Request(id='id1', alias='alias1', tiny_id='tiny_id')
        with self.assertRaisesRegexp(InvalidRequestError, "Specify only one of .* properties"):
            request.validate()

        request = Request(id='id1', alias='alias1', order_by='AAA')
        with self.assertRaisesRegexp(InvalidRequestError, "property should be one of"):
            request.validate()

        request = Request(id='id1', alias='alias1', order_by='desc', count=51)
        with self.assertRaisesRegexp(InvalidRequestError, "property should be lower than"):
            request.validate()

        request = Request(id='id1', alias='alias1', order_by='desc', count=50, text="abcdefghijklmnopqrstuvwxyz")
        with self.assertRaisesRegexp(InvalidRequestError, "property should be lower than"):
            request.validate()

        request = Request(id='id1', alias='alias1', count=1, details={'key1': 'value1', 'key2': 'value2'})
        self.assertEqual({'id': 'id1', 'count': 1, 'details': {'key1': 'value1', 'key2': 'value2'}}, request.decode())
