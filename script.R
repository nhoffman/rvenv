#!/usr/bin/env Rscript
source(file.path(Sys.getenv('VIRTUAL_ENV'), 'bin', 'rvenv'))

suppressPackageStartupMessages(library(argparse, quietly=TRUE))

main <- function(arguments){

  parser <- ArgumentParser(description='An example script')
  parser$add_argument('--foo', help='An argument')

  args <- parser$parse_args(arguments)
  print(args)
  print(.libPaths())

}

main(commandArgs(trailingOnly=TRUE))
