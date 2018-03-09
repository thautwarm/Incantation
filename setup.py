# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('./LICENSE', encoding='utf-8') as f:
    print(f.read())
if input("Approve the license terms? [yes|no]") != 'yes':
    print("I'm Sorry that you cannot accept the license. Have a nice day :)")
else:
    import os

    cat = os.path.join
    setup(name='Incantation',
          version='0.4.0',
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
