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
  curl https:// > $VIRTUAL_ENV/bin/rvenv && chmod +x $VIRTUAL_ENV/bin/rvenv

Execute from the command line to install packages to
``$VIRTUAL_ENV/lib/R.%v-library``.

Add the following lines to an R script to use locally-installed
packages::

  #!/usr/bin/env Rscript
  source(file.path(Sys.getenv('VIRTUAL_ENV'), 'bin', 'rvenv'))

Loading ``rvenv`` as above prepends ``$VIRTUAL_ENV/lib/R.%v-library``
to the library search path.

