import os
import subprocess
from setuptools import setup

subprocess.call(
    ('mkdir -p _rvenv/data && '
     'git describe --tags --dirty > _rvenv/data/ver.tmp'
     '&& mv _rvenv/data/ver.tmp _rvenv/data/ver '
     '|| rm -f _rvenv/data/ver.tmp'),
    shell=True, stderr=open(os.devnull, "w"))

from _rvenv import __version__

setup(name='rvenv',
      version=__version__,
      description='Install and manage R packages in a python virtualenv',
      url='https://github.com/nhoffman/rvenv',
      author='Noah Hoffman',
      author_email='noah.hoffman@gmail.com',
      license='MIT',
      packages=['rvenv'],
      package_dir={'rvenv': '_rvenv'},
      zip_safe=False,
      scripts=['rvenv'],
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: System Administrators',
          'Operating System :: POSIX',
          'Programming Language :: Python :: 2.7',
      ],
)
