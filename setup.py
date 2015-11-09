from setuptools import setup

setup(name='rvenv',
      version='0.1',
      description='Install and manage R packages in a python virtualenv',
      url='https://github.com/nhoffman/rvenv',
      author='Noah Hoffman',
      author_email='noah.hoffman@gmail.com',
      license='MIT',
      packages=['rvenv'],
      package_dir={'rvenv': '_rvenv'},
      zip_safe=False,
      scripts=['rvenv'],
)
