from setuptools import find_packages
from setuptools import setup

version = '0.7'

install_requires = []
tests_require = install_requires + []

setup(
    version=version,
    name='formal',
    install_requires=install_requires,
    packages=find_packages(),
    test_suite='formal.tests',
)
