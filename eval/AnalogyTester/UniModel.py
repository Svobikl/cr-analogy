__author__ = 'svobik'

import logging
import optparse


logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

def createHash(modelFile):

    hashMap = dict()
    b_firstLine = False
    firstLine = ""
    with open(modelFile, 'rb') as f:
        for line in f:
            if (b_firstLine == False):
                firstLine = line
                b_firstLine = True
            lineSplit = line.split(" ")
            hashMap[lineSplit[0]] = lineSplit[1:]


    return (hashMap,firstLine)

def writeUnifiedModel(modelName, outputFile, hashMap, firstLine):

    fw = open(outputFile, "a")
    fw.write(firstLine)
    count = 0
    with open(modelName, 'rb') as f:
        for line in f:

            lineSplit = line.split(" ")
            if (lineSplit[0] in hashMap):
                fw.write(line)
                fw.flush()
                count += 1

    fw.close()
    print("Count = %d" % count)

if __name__ == '__main__':

    parser = optparse.OptionParser(usage="%prog [OPTIONS]")
    parser.add_option('-m', '--model', default='vector.txt',

                      help='Give a path with the name of a model to load (default name= vector.txt)')
    parser.add_option('-c', '--corpus', default='./corpus/czech_emb_corpus.txt',
                      help='Give a name of corpus to analyze  (default: ./corpus/czech_emb_corpus.txt)')

    options, args = parser.parse_args()
    logging.info("Loading model")
    hashMap, firstLine =createHash("/media/data/korpusy/Trained/categories/vectors_nocatbig.bin")
    logging.info("Writing model")
    writeUnifiedModel("/media/data/korpusy/Trained/categories/vectors_cat.bin", "/media/data/korpusy/Trained/categories/vectors_cat_unibig.bin", hashMap, firstLine)