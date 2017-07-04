import os
from setuptools import setup

setup(name='paper-hunt',
      version='0.1',
      description='Module for data extraction',
      url='https://github.com/swapnil96/paper-hunt',
      author='Swapnil Das',
      author_email='dassswapnil96@gmail.com',
      license='GNU General Public License v3.0',
      packages=['paper-hunt'],
      install_requires=[
          'selenium',
      ],
      zip_safe=False)