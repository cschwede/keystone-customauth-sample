# -*- encoding: utf-8 -*-
__author__ = "Christian Schwede <info@cschwede.de>"
name = 'customauth'
entry_point = '%s.middleware:filter_factory' % (name)
version = '0.1'

from setuptools import setup, find_packages

setup(
    name=name,
    version=version,
    description='OpenStack Keystone custom authentication middleware example',
    license='Apache License (2.0)',
    author='Christian Schwede',
    author_email='info@cschwede.de',
    url='https://github.com/cschwede/keystone-customauth-sample',
    packages=find_packages(),
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.6',
        'Environment :: No Input/Output (Daemon)'],
    install_requires=['keystone'],
    entry_points={
        'paste.filter_factory': ['%s=%s' % (name, entry_point)]
    },
)
