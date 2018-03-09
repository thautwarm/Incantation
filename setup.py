# -*- coding: utf-8 -*-
from setuptools import setup


setup(name='Incantation',
      version='0.4.1',
      keywords='website, web-design',
      description="Python Object Design about Website. Make Developing websites like saying incantations.",
      license='MIT',
      url='https://github.com/thautwarm/Incantation',
      author='thautwarm',
      author_email='twshere@outlook.com',
      include_package_data=True,
      packages=['incantation', 'incantation.CSS', 'incantation.Component', 'incantation.Templates',
                'incantation.Frequently', 'incantation.Javascript'],
      platforms='any',
      classifiers=['Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: Implementation :: CPython'],
      zip_safe=False)
