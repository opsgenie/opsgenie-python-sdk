import sys

if sys.version_info >= (2, 7):
    from unittest import TestCase
else:
    from unittest2 import TestCase


class OpsGenieTestCase(TestCase):
    pass
