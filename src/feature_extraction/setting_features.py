#!/usr/bin/python
__maintainer__ 	= "jefferson amado <JAPeTo>"
__email__ = "jeffersonamado@gmail.com"
import sys, os, time
from constants import *
#########
#First capital letter: it is a binary feature that represents
#if the first letter in the observed word is capital.
def letter_capital_feature(train_file= None, train_ouput= None):
	train_file=open(train_file, 'r')
	train_ouput=open(train_ouput, 'w')
	feature = {'True':"1", 'False':"0"}
	for row in train_file:
		if (row[0]!='\n'): # skip new line					
			is_capital = row[0].isupper()
			row = row.split()
			row.insert(2, feature[str(is_capital)])	#word chunk [feat] ...
			train_ouput.write(' '.join(row)+"\n")
		else:
			train_ouput.write("\n")
	train_ouput.close()
	train_file.close()
#Word Length: it is related to the length of the observed
#word. The feature is binary and it represents if the
#length of the word is up to the threshold 
def length_of_word_feature(train_file= None, train_ouput= None, treshold=5):
	train_file=open(train_file, 'r')
	train_ouput=open(train_ouput, 'w')
	feature = {'True':"1", 'False':"0"}
	for row in train_file:
		if (row[0]!='\n'): # skip new line
			row = row.split()
			is_long = (len(row[0]) >= treshold)
			row.insert(3, feature[str(is_long)]) #word chunk isCapital [feat] ...
			train_ouput.write(' '.join(row)+"\n")
		else:
			train_ouput.write("\n")
	train_ouput.close()
	train_file.close()
#First word: it is a binary feature that represents if the
#observed word is the first word in the sentences.
def begin_sentence_feature(train_file= None, train_ouput= None):
	train_file=open(train_file, 'r')
	train_ouput=open(train_ouput, 'w')
	feature = {'True':"1", 'False':"0"}
	n_row =0
	train_file = train_file.readlines()
	for row in train_file:
		if (row[0]!='\n'): # skip new line
			is_begin = n_row == 0 or (n_row > 0 and train_file[n_row-1] == "\n" and not (" Fg " in row))
			row = row.split()
			row.insert(3, feature[str(is_begin)]) #word chunk isCapital [feat] ...
			train_ouput.write(' '.join(row)+"\n")
		else:
			train_ouput.write("\n")
		n_row = n_row + 1
	train_ouput.close()
#Part-Of-Speech (POS): we use Freeling to extract
#complexity of the relations. We follow the hill-climbing
#(greedy) feature selection proposed by Caruana and
#Freitag [8]. In this scheme, the best performing set of
#features at each step is revised and we select the best
#feature set on the basis the best F1 scores. In table 1 we
#perfomed a description of the features.
def pos_feature(train_file= None, train_ouput= None):
	dic ={ }
	train_file=open(train_file, 'r')
	train_ouput=open(train_ouput, 'w')
	feature = {'NP00G00':"G", 'NP00V00':"V", "NP00SP0":"P", "NP00O00":"O",}
	n_row = 0
	for row in train_file:
		if (row[0]!='\n' and n_row > 303): # skip new line
			row = row.split()
			process = os.popen("echo '.' | analyze -f "+CFG_DIR+"es.cfg" )
			process = list(process.read().split()[2])
			row.insert(4, process[0]) #word chunk isCapital begin postag [feat] ...
			train_ouput.write(' '.join(row)+"\n")
		else:
			train_ouput.write("\n")
		n_row = n_row + 1
	train_ouput.close()

if __name__ == '__main__':
	DELETE = True
	#letter_capital_feature(train_file = DATA_DIR+"conll2002/esp.train",
	#	train_ouput = DATA_DIR+"conll2002/esp.1f.train")
	#letter_capital_feature(train_file = DATA_DIR+"conll2002/esp.testa",
	#	train_ouput = DATA_DIR+"conll2002/esp.1f.testa")
	#letter_capital_feature(train_file = DATA_DIR+"conll2002/esp.testb",
	#	train_ouput = DATA_DIR+"conll2002/esp.1f.testb")
#
	#length_of_word_feature(train_file = DATA_DIR+"conll2002/esp.1f.train",
	#	train_ouput = DATA_DIR+"conll2002/esp.2f.train")
	#length_of_word_feature(train_file = DATA_DIR+"conll2002/esp.1f.testa",
	#	train_ouput = DATA_DIR+"conll2002/esp.2f.testa")
	#length_of_word_feature(train_file = DATA_DIR+"conll2002/esp.1f.testb",
	#	train_ouput = DATA_DIR+"conll2002/esp.2f.testb")
	#if DELETE:
	#	os.remove(DATA_DIR+"conll2002/esp.1f.train")
	#	os.remove(DATA_DIR+"conll2002/esp.1f.testa")
	#	os.remove(DATA_DIR+"conll2002/esp.1f.testb")
#
	#begin_sentence_feature(train_file = DATA_DIR+"conll2002/esp.2f.train",
	#	train_ouput = DATA_DIR+"conll2002/esp.3f.train")
	#begin_sentence_feature(train_file = DATA_DIR+"conll2002/esp.2f.testa",
	#	train_ouput = DATA_DIR+"conll2002/esp.3f.testa")
	#begin_sentence_feature(train_file = DATA_DIR+"conll2002/esp.2f.testb",
	#	train_ouput = DATA_DIR+"conll2002/esp.3f.testb")
	#if DELETE:
	#	os.remove(DATA_DIR+"conll2002/esp.2f.train")
	#	os.remove(DATA_DIR+"conll2002/esp.2f.testa")
	#	os.remove(DATA_DIR+"conll2002/esp.2f.testb")
#
	pos_feature(train_file = DATA_DIR+"conll2002/esp.3f.train",
		train_ouput = DATA_DIR+"conll2002/esp.4f.train")
	#pos_feature(train_file = DATA_DIR+"conll2002/esp.3f.testa",
	#	train_ouput = DATA_DIR+"conll2002/esp.4f.testa")
	#pos_feature(train_file = DATA_DIR+"conll2002/esp.3f.testb",
	#	train_ouput = DATA_DIR+"conll2002/esp.4f.testb")

	if False:
		os.remove(DATA_DIR+"conll2002/esp.3f.train")
		os.remove(DATA_DIR+"conll2002/esp.3f.testa")
		os.remove(DATA_DIR+"conll2002/esp.3f.testb")
	



