#!/usr/bin/python
__maintainer__ 	= "jefferson amado <JAPeTo>"
__email__ = "jeffersonamado@gmail.com"
import sys, os, time
DEBUG = True
# Check current working directory.
CURR_DIR = os.getcwd()
# Now change the directory
SRC_DIR = CURR_DIR.replace("/src", "/src/" )
DATA_DIR = CURR_DIR.replace("/src", "/data/")
MOD_DIR = CURR_DIR.replace("/src", "/models/" )
TPL_DIR = CURR_DIR.replace("/src", "/templates/" )
TOOLS_DIR = CURR_DIR.replace("/src", "/utils/")