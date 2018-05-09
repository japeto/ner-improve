#!/usr/bin/python
__maintainer__ 	= "jefferson amado <JAPeTo>"
__email__ = "jeffersonamado@gmail.com"
import sys, os, time
from constants import *

def build_model(template, train_file, name_model, test_file, predict_file= None):
	print("Creating model")
	start = time.time()
	output = "\nTRAINING crf_learn STDOUT\n"
	print ( "crf_learn "+template+" "+train_file+" "+name_model+"" )
	process = os.popen("echo | crf_learn "+template+" "+train_file+" "+name_model+"")
	print( output.strip() )
	while output!= "" :
		output = process.readline()
		print( output.strip() )
	print("finished in {:.2f} sec.".format(time.time() - start), flush=True)
	start = time.time()

	print("crf_test ... \n", end="", flush=True)
	print(  "crf_test -m "+name_model+" "+test_file+" >> "+predict_file+"" )
	process = os.popen("echo | crf_test -m "+name_model+" "+test_file+" >> "+predict_file+"")
	print("finished in {:.2f} sec.".format(time.time() - start), flush=True)


if __name__ == '__main__':
	FOLDER = "m1_baseline/"
	build_model(template = MOD_DIR+FOLDER+"template",
	train_file = DATA_DIR+"conll2002/esp.3f.train",
	name_model = MOD_DIR+FOLDER+"esp.3f.model",
	test_file = DATA_DIR+"conll2002/esp.3f.testb",
	predict_file = MOD_DIR+FOLDER+"esp.predict.3f.txt")