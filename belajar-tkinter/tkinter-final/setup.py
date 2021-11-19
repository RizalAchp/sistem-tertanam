import setuptools
from setuptools import setup

print(setuptools.find_packages())

setup(name='tkinter-final-arduino',
      version='0.1',
      description='Tkinter based GUI to run arduino with pyfirmata',
      author='rizalachp',
      author_email='rizal.ahmadp@gmail.com',
      license='MIT',
      packages=setuptools.find_packages(),
      install_requires=[
          'tkinter',
          'tk_tools',
          'engineering_notation',
          'pyfirmata'
      ],
      zip_safe=False)
