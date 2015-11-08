=======
 rvenv
=======

Install and manage R packages in a python virtualenv.

Why?
====

I need someplace to put project-specific R packages. The python
virtualenv I inevitably have installed in any given
project/analysis/pipeline seems as good a place as any.


Installation
============

Assumes an active virtualenv::

  virtualenv r-env
  source r-env/bin/activate
  curl https://raw.githubusercontent.com/nhoffman/rvenv/master/rvenv > $VIRTUAL_ENV/bin/rvenv && chmod +x $VIRTUAL_ENV/bin/rvenv

Execute from the command line to install packages to
``$VIRTUAL_ENV/lib/R.%v-library``.

Add the following lines to an R script to use locally-installed
packages::

  #!/usr/bin/env Rscript
  source(file.path(Sys.getenv('VIRTUAL_ENV'), 'bin', 'rvenv'))

Loading ``rvenv`` as above prepends ``$VIRTUAL_ENV/lib/R.%v-library``
to the library search path.

usage
=====

::

  usage: ./rvenv [-h] [-r REQUIREMENTS] [--rm] [--bioc] [--update] [--list]
		 [--repos REPOS]
		 [packages [packages ...]]

  Install R packages to a python virtualenv

  positional arguments:
    packages              one or more package names

  optional arguments:
    -h, --help            show this help message and exit
    -r REQUIREMENTS, --requirements REQUIREMENTS
			  a file listing packages
    --rm                  remove listed packages
    --bioc                packages are in Bioconductor
    --update              update existing packages
    --list                list packages installed locally
    --repos REPOS         value for "install.packages(repos)" [http://cran.fhcrc.org/]

