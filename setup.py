#!/usr/bin/env python

import os
from setuptools import setup


setup(
  name='whisper',
  version='0.10.0-rc1',
  url='http://graphiteapp.org/',
  author='Chris Davis',
  author_email='chrismd@gmail.com',
  license='Apache Software License 2.0',
  description='Fixed size round-robin style database',
  entry_points={
    'console_scripts': [
      'find-corrupt-whisper-files=whisper.cli.findcorruptwhisperfiles:main',
      'rrd2whisper=whisper.cli.rrd2whisper:main',
      'whisper-create=whisper.cli.create:main',
      'whisper-diff=whisper.cli.diff:main',
      'whisper-dump=whisper.cli.dump:main',
      'whisper-fetch=whisper.cli.fetch:main',
      'whisper-fill=whisper.cli.fill:main',
      'whisper-info=whisper.cli.info:main',
      'whisper-merge=whisper.cli.merge:main',
      'whisper-resize=whisper.cli.resize:main',
      'whisper-set-aggregation-method=whisper.cli.setaggregationmethod:main',
      'whisper-set-xfilesfactor=whisper.cli.setxfilesfactor:main',
      'whisper-update=whisper.cli.update:main',
      'whisper-auto-resize=whisper.contrib.autoresize:main',
      'whisper-auto-update=whisper.contrib.autoupdate:main',
    ],
  },
  packages=['whisper', 'whisper.cli', 'whisper.contrib'],
  classifiers=[
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
  ],
)
