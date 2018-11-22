"""Setup file and install script for CMDBtools.

Version 1.0.0 (Nov 22, 2018)
Copyright (c) 2018 Shujia Huang
"""
try:
    from setuptools import setup, find_packages
    _has_setuptools = True
except ImportError:
    from distutils.core import setup, find_packages


DESCRIPTION = "cmdbtools: A command line tools for CMDB variant browser."
DISTNAME = 'CMDBtools'
MAINTAINER = 'Shujia Huang (at) BGI'
MAINTAINER_EMAIL = 'huangshujia@bgi.com'
URL = 'https://github.com/ShujiaHuang/cmdbtools'
LICENSE = 'BSD (3-clause)'
DOWNLOAD_URL = 'https://github.com/ShujiaHuang/cmdbtools'
VERSION = "1.0.0"


if __name__ == "__main__":
    setup(name=DISTNAME,
          version=VERSION,
          author=MAINTAINER,
          author_email=MAINTAINER_EMAIL,
          maintainer=MAINTAINER,
          maintainer_email=MAINTAINER_EMAIL,
          description=DESCRIPTION,
          long_description=(open("README.md").read()),
          license=LICENSE,
          url=URL,
          download_url=DOWNLOAD_URL,
          packages=find_packages(),
          include_package_data=True,
          install_requires=[
              'PyYAML',
          ],

          scripts = [],
          entry_points = {

             'console_scripts': [
                  'cmdbtools = cmdbtools.cmdbtools:main'
              ]
          },
          classifiers=[
              'Intended Audience :: Science/Research',
              'Programming Language :: Python :: 2.7',
              'License :: OSI Approved :: BSD License',
              'Topic :: Scientific/Engineering :: Bio-Informatics',
              'Topic :: Scientific/Engineering :: Tools',
              'Topic :: Multimedia :: CMDB',
              'Operating System :: POSIX',
              'Operating System :: Linux/Unix',
              'Operating System :: MacOS'],
          )
