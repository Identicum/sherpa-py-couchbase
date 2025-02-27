# sherpa-py-couchbase is available under the MIT License. https://github.com/Identicum/sherpa-py-midpoint/
# Copyright (c) 2025, Identicum LLC - https://identicum.com/
#
# Author: Gustavo J Gallardo - ggallard@identicum.com
#

from setuptools import setup

setup(
    name='sherpa-py-couchbase',
    version='1.0.0',
    description='Python utilities for Couchbase',
    url='git@github.com:Identicum/sherpa-py-couchbase.git',
    author='Round Services',
    author_email='ggallard@roundservices.biz',
    license='MIT License',
    install_requires=['testresources', 'couchbase', 'sherpa-py-utils'],
    packages=['sherpa.couchbase'],
    zip_safe=False,
    python_requires='>=3.0'
)
