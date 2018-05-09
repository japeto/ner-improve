#!/usr/bin/python
__maintainer__  = "jefferson amado <JAPeTo>"
__email__ = "jeffersonamado@gmail.com"
import sys, os, time
from system_paths import *
 
def built_train_conll1_0(train_file = None, new_train_file= None):
    #archivo=open('esp.train', 'r')
    #nuevoTrain=open("ConllTrain1_0", 'w')
    archivo=open(train_file, "r")
    nuevoTrain=open(new_train_file,"w")
    lineasEsp=archivo.readlines()
    for line in lineasEsp:
        arrayLine=line.replace("\n",'').split(" ")
        valor =0
        if len(arrayLine)==1:
            nuevoTrain.write("\n")
        else:
            if arrayLine[0][:1].isupper():
                if arrayLine[2][:2]=='B-'or arrayLine[2][:2]=='I-' or arrayLine[2][:2]=='O-':
                    valor=1
            nuevoTrain.write(arrayLine[0] + " " + arrayLine[1] + " " + str(valor) + " "+ arrayLine[2]+"\n")
    nuevoTrain.close()
    archivo.close()

#ConstruirTrainConll1_0()
def build_train_treshold(treshold=5, train_file = None, new_train_file= None):
    #archivo=open("Training/ConllTrain1_0", "r")
    #nuevoArchivo=open("Training/ConllTrainTreshold.txt","w")
    archivo=open(train_file, "r")
    nuevoArchivo=open(new_train_file,"w")
    lineasTrain0=archivo.readlines()
    for linea in lineasTrain0:
        array=linea.replace("\n", "").split(" ")
        #print array
        valor=0
        if  len(array) == 1: 
            nuevoArchivo.write("\n")
        else:
            palabra=array[0]
            posTag=array[1]
            mayus=array[2]
            etiqueta=array[3]
            if len(palabra) >= treshold:
                valor = 1
             
            nuevoArchivo.write(palabra + " " + posTag+ " " + mayus + " " + str(valor)+" "+ etiqueta + "\n")
         
    archivo.close()
    nuevoArchivo.close()    
 
def buld_train_sentence(train_file = None, new_train_file= None):
    #archivo=open("Training/ConllTrainTreshold.txt", "r")
    #nuevoArchivo=open("Training/ConllTrainSentence.txt", "w")
    archivo=open(train_file, "r")
    nuevoArchivo=open(new_train_file,"w")
    lineasTrain=archivo.readlines()
    count=0
    for linea in lineasTrain:
        array=linea.replace("\n", "").split(" ")
        valor=0
        if  len(array) > 1:
            palabra=array[0]
            posTag=array[1]
            mayus=array[2]
            tamanio=array[3]
            etiqueta=array[4]
             
            if count == 0:
                valor= 1
            elif count > 0:
                if lineasTrain[count-1].split(" ")== ["\n"] and posTag != "Fg":
                    valor =1
                    
            nuevoArchivo.write(palabra + " " + posTag+ " " + mayus + " " + tamanio +" " + str(valor)+" "+ etiqueta + "\n")
 
        elif linea.split(" ")==["\n"]:
            nuevoArchivo.write("\n")
        #if len(array) > 1:
        #   palabra=array[0]
        #   posTag=array[1]
        #   mayus=array[2]
        #   tamanio=array[3]
        #   etiqueta=array[4]
        #   if count == 0:
        #       valor=1
        #   elif count > 0:
        #       if linea.split(" ") == [" "]:
        #           tagAnterior=lineasTrain[count-1].split(" ")[0]
        #           if tagAnterior == "\n":
        #               valor =1
        #   nuevoArchivo.write(palabra + " " + posTag+ " " + mayus + " " + tamanio +" " + str(valor)+" "+ etiqueta + "\n")
         
        count+=1

def build_train_ner(train_file = None, new_train_file= None):
    #archivo=open('esp.train', 'r')
    #salida = open('ner.train','w')
    archivo=open(train_file, "r")
    salida=open(new_train_file,"w")
    lineasEsp=archivo.readlines()
    for line in lineasEsp:
        arrayLine=line.replace("\n",'').split(" ")
        if len(arrayLine)==1:
            salida.write("\n")
        else:
            salida.write(arrayLine[2] + "\n")
         
#palabra_ner()
#### TRAIN
built_train_conll1_0(train_file = DATA_DIR+"conll2002/esp.train", 
    new_train_file= DATA_DIR+"conll2002/esp.new.train")
build_train_treshold(treshold=5, train_file = DATA_DIR+"conll2002/esp.new.train", 
    new_train_file= DATA_DIR+"conll2002/esp.treshold.train")
buld_train_sentence(train_file = DATA_DIR+"conll2002/esp.treshold.train", 
    new_train_file= DATA_DIR+"conll2002/esp.sentence.treshold.train")
build_train_ner(train_file = DATA_DIR+"conll2002/esp.train", 
    new_train_file= DATA_DIR+"conll2002/esp.ner.train")

##### TEST
built_train_conll1_0(train_file = DATA_DIR+"conll2002/esp.testa", 
    new_train_file= DATA_DIR+"conll2002/esp.new.testa")
build_train_treshold(treshold=5, train_file = DATA_DIR+"conll2002/esp.new.testa", 
    new_train_file= DATA_DIR+"conll2002/esp.treshold.testa")
buld_train_sentence(train_file = DATA_DIR+"conll2002/esp.treshold.testa", 
    new_train_file= DATA_DIR+"conll2002/esp.sentence.treshold.testa")
build_train_ner(train_file = DATA_DIR+"conll2002/esp.testa", 
    new_train_file= DATA_DIR+"conll2002/esp.ner.testa")

built_train_conll1_0(train_file = DATA_DIR+"conll2002/esp.testb", 
    new_train_file= DATA_DIR+"conll2002/esp.new.testb")
build_train_treshold(treshold=5, train_file = DATA_DIR+"conll2002/esp.new.testb", 
    new_train_file= DATA_DIR+"conll2002/esp.treshold.testb")
buld_train_sentence(train_file = DATA_DIR+"conll2002/esp.treshold.testb", 
    new_train_file= DATA_DIR+"conll2002/esp.sentence.treshold.testb")
build_train_ner(train_file = DATA_DIR+"conll2002/esp.testb", 
    new_train_file= DATA_DIR+"conll2002/esp.ner.testb")






