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

Install to an active virtualenv using pip (or simply copy ``rvenv`` to
``$VIRTUAL_ENV/bin``)::

  % virtualenv r-env
  % source r-env/bin/activate
  % pip install git+https://github.com/nhoffman/rvenv.git

You can use the ``rvenv`` script from the command line to install
packages to ``$VIRTUAL_ENV/lib/R.%v-library``::

  % rvenv dplyr

Including the following lines in an R script will set the library path
to use locally-installed packages::

  #!/usr/bin/env Rscript
  if(Sys.getenv("VIRTUAL_ENV") == ""){ stop("An active virtualenv is required") }
  source(file.path(Sys.getenv('VIRTUAL_ENV'), 'bin', 'rvenv'))

Loading ``rvenv`` as above prepends ``$VIRTUAL_ENV/lib/R.%v-library``
to the library search path. See example script ``script.R``

To add the library path to an interactive R session::

  % eval $(rvenv -e)
  % R


usage
=====

::

  usage: ./rvenv [-h] [-r REQUIREMENTS] [--rm] [--update] [--list] [-e]
		 [--repos REPOS]
		 [packages [packages ...]]

  Install R packages to a python virtualenv

  Include the following in an R script to add "$VIRTUAL_ENV/lib/R.%v-library"
  to the library search path:

    #!/usr/bin/env Rscript
    if(Sys.getenv("VIRTUAL_ENV") == ""){ stop("An active virtualenv is required") }
    source(file.path(Sys.getenv("VIRTUAL_ENV"), "bin", "rvenv"))

  Also see https://github.com/nhoffman/rvenv

  positional arguments:
    packages              one or more package names

  optional arguments:
    -h, --help            show this help message and exit
    -r REQUIREMENTS, --requirements REQUIREMENTS
			  a file listing packages
    --rm                  remove listed packages
    --update              update existing packages
    --list                list packages installed locally
    -e, --environ         print shell command to set R_LIBS
    --repos REPOS         value for "install.packages(repos)" [http://cran.fhcrc.org/]
