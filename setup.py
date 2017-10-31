# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import io

with io.open('./README.rst', encoding='utf-8') as f:
    readme = f.read()

with io.open('./LICENSE', encoding='utf-8') as f:
    print(f.read())
if input("Do you approve the license terms? [yes|no]") != 'yes':
    print("I'm Sorry that you cannot accept the license. Have a nice day :)")
else:
    import os
    cat = os.path.join
    setup(name='Incantation',
      version='0.3.1',
      keywords='website, web-design',
      description = "Python Object Design about Website. Make Developing websites like saying incantations.",
      long_description=readme,
      license='GPLv3.0 License',
      url = 'https://github.com/thautwarm/Incantation',
      author='thautwarm',
      author_email='twshere@outlook.com',
      include_package_data=True,
      packages=['incantation'],
      platforms='any',
      classifiers=['Programming Language :: Python :: 3.6',
                   'Programming Language :: Python :: Implementation :: CPython'],
      zip_safe=False,
      install_requires=[
        'jinja2'
        ]
      )
    
