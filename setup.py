import io
import sys

from setuptools import find_packages
from setuptools import setup
from setuptools.command.test import test as TestCommand

import opsgenie


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)


def read(*filenames, **kwargs):
    encoding = kwargs.get('encoding', 'utf-8')
    sep = kwargs.get('sep', '\n')
    buf = []
    for filename in filenames:
        with io.open(filename, encoding=encoding) as f:
            buf.append(f.read())
    return sep.join(buf)


long_description = read('README.rst')

setup(
    name='opsgenie-sdk',
    version=opsgenie.__version__,
    package_dir={'': 'opsgenie'},
    packages=find_packages('opsgenie'),
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
