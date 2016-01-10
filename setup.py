import codecs
import os
import sys

from setuptools import find_packages, setup
from setuptools.command.test import test as test_command

import const_choice


class PyTest(test_command):
    def finalize_options(self):
        super(test_command, self).finalize_options()
        self.test_suite = True

    def run_tests(self):
        import pytest

        os.chdir('tests/')
        errno = pytest.main(self.test_args)
        sys.exit(errno)


def long_description():
    with codecs.open('README.md', encoding='utf8') as f:
        rst = f.read()
    return rst


setup(
    name='const_choice',
    version=const_choice.__version__,
    description=const_choice.__doc__.strip(),
    long_description=long_description(),
    download_url='https://github.com/glowka/const_choice',
    license=const_choice.__license__,
    tests_require=['pytest'],
    cmdclass={'test': PyTest},
    packages=find_packages(),
    author_email='tk.glowka@gmail.com',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Topic :: Utilities'
        ]
)
