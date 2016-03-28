import os
import sys

from setuptools import setup
from setuptools.command.test import test


class Tox(test):
    def finalize_options(self):
        test.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)

long_description = open(
    os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='opsgenie-sdk',
    version='0.1.2',
    packages=['opsgenie', 'opsgenie.alert', 'opsgenie.heartbeat', 'opsgenie.integration', 'opsgenie.policy',
              'opsgenie.tests'],
    install_requires=['requests', 'pytz'],
    tests_require=['tox', 'nose2', 'httpretty'],
    cmdclass={'test': Tox},
    url='https://github.com/opsgenie/opsgenie-python-sdk',
    license='Apache License 2.0',
    author='OpsGenie',
    author_email='support@opsgenie.com',
    description='Python SDK for OpsGenie Web/REST API',
    long_description=long_description,
    keywords=['OpsGenie', 'Web Api', 'Rest Api']
)
