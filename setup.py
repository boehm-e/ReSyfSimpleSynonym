#!/usr/bin/env python

from distutils.core import setup, Extension

setup(name='ReSyf',
      version='0.2',
      description='ReSyf resource API',
      author='Ricci Dorian',
      author_email='dorian@ricci.ovh',
      # url='https://www.python.org/sigs/distutils-sig/',
      packages=['ReSyf', 'ReSyf.src', "ReSyf.pylmflib", "ReSyf.pylmflib.common", "ReSyf.pylmflib.config", "ReSyf.pylmflib.core", "ReSyf.pylmflib.input", "ReSyf.pylmflib.utils"],
	  
	  )
