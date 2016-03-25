from datetime import datetime
from unittest import TestCase

import pytz

from opsgenie.core import utility
from opsgenie.core.utility import list_to_str


class TestUtility(TestCase):
    def test_format_date(self):
        dt = None
        formatted_date = utility.format_date(dt)
        self.assertEqual(None, formatted_date)

        dt = datetime(2016, 03, 17, 16, 32, 24, 10)
        formatted_date = utility.format_date(dt)
        self.assertEqual('2016-03-17 16:32', formatted_date)

        dt = datetime(2016, 03, 17, 16, 32, 24, 10, pytz.utc)
        formatted_date = utility.format_date(dt)
        self.assertEqual('2016-03-17 16:32', formatted_date)

        dt = datetime(2016, 03, 17, 16, 32, 24, 10, pytz.timezone('Europe/Istanbul'))
        formatted_date = utility.format_date(dt)
        self.assertEqual('2016-03-17 16:32', formatted_date)

    def test_list_to_str(self):
        tags = None
        tags_str = list_to_str(tags)
        self.assertEqual(None, tags_str)

        tags = []
        tags_str = list_to_str(tags)
        self.assertEqual('', tags_str)

        tags = ['tag1', 'tag2', 'tag3']
        tags_str = list_to_str(tags)
        self.assertEqual('tag1,tag2,tag3', tags_str)
