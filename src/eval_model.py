#!/usr/bin/python
__maintainer__ 	= "jefferson amado <JAPeTo>"
__email__ = "jeffersonamado@gmail.com"
import sys, os, time
from constants import *

def eval_pr(predicted_file = None, result_file= None):
	print ( "perl conlleval.pl -d '\t' < "+predicted_file )
	print("eval model")
	start = time.time()
	process = os.popen("echo | perl conlleval.pl -d '\t' < "+predicted_file)
	end = time.time()
	print(end - start)
	conlleval = str ( process.read() )
	res=open(result_file, 'w')
	res.write(conlleval)
	res.close()

if __name__ == '__main__':
	FOLDER = "m1_baseline/"
	eval_pr(predicted_file = MOD_DIR+FOLDER+"esp.predict.3f.txt", 
		result_file = MOD_DIR+FOLDER+"eval.result.txt")
