__author__ = 'svobik'

from gensim.models.word2vec import Word2Vec
from gensim import corpora, models, similarities, matutils
import re
import os
import logging
import optparse
import numpy as np
import operator
import codecs
from evaluation import word_similarity
from fnmatch import fnmatch

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

modelFile = "/media/data/korpusy/Trained/categories/new2.bin"
if __name__ == '__main__':

    parser = optparse.OptionParser(usage="%prog [OPTIONS]")
    parser.add_option('-m', '--model', default='vector.txt',

                      help='Give a path with the name of a model to load (default name= vector.txt)')
    parser.add_option('-c', '--corpus', default='./corpus/czech_emb_corpus. txt',
                      help='Give a name of corpus to analyze  (default: ./corpus/czech_emb_corpus.txt)')
    parser.add_option('-t', '--topn', default='1',
                      help='TOP N similar words')
    options, args = parser.parse_args()
    logging.info("Loading model")
    model = Word2Vec.load_word2vec_format(modelFile,binary=False)
    #model.save_word2vec_format('/media/data/korpusy/Trained/GoogleNews-vectors-negative300.txt', binary=False)
    acc =model.accuracy("/media/data/korpusy/Trained/categories/questions-words.txt")

    totalCorr = 0
    total = 0
    semantics = 0
    semanticsTotal = 0
    syntactic = 0
    syntacticTotal =0
    fw = open(modelFile+".out", "w")

    fw.write("> Mikolov's, word analogy test:\n")
    for item in acc[:-1]:
        section= item['section']

        correctCount = len(item['correct'])
        incorrectCount = len(item['incorrect'])
        totalCorr += correctCount
        total += correctCount + incorrectCount
        if (section.startswith("gram")):
            syntactic += correctCount
            syntacticTotal += correctCount + incorrectCount
        else:
            semantics += correctCount
            semanticsTotal += correctCount + incorrectCount
        fw.write(section + ":%.2f%% (%d/%d)\n" % (( float(correctCount) / float(correctCount + incorrectCount) * 100.0),correctCount,(correctCount+incorrectCount)) )
    fw.write("---------\n")
    fw.write("total: %.2f%% (%d/%d)\n" % ((float(totalCorr)/float(total) * 100.0),totalCorr,total))
    fw.write("semantics: %.2f%% (%d/%d)\n" % ((float(semantics)/float(semanticsTotal) * 100.0),semantics,semanticsTotal))
    fw.write("syntax: %.2f%% (%d/%d)\n" % ((float(syntactic)/float(syntacticTotal) * 100.0),syntactic,syntacticTotal))
    fw.write("---------\n")
    fw.write("Other similarity tests: \n")
    wordsim = word_similarity.WordSimilarity("wordsim353")
    evaluation = wordsim.evaluate(model)
    logging.info("Wordsim-353 evaluation (spearman)= %s" % evaluation[0])
    fw.write("> Wordsim-353 evaluation (spearman)= %s \n" % evaluation[0])
    mc = word_similarity.WordSimilarity("mc")
    evaluation = mc.evaluate(model)
    logging.info("MC-28 evaluation (spearman)= %s" % evaluation[0])
    fw.write("> MC-28 evaluation (spearman)= %s \n" % evaluation[0])
    rg = word_similarity.WordSimilarity("rg")
    evaluation = rg.evaluate(model)
    logging.info("RG-65 evaluation (spearman)= %s" % evaluation[0])
    fw.write("> RG-65 evaluation (spearman)= %s \n" % evaluation[0])
    simlex = word_similarity.WordSimilarity("simlex999")
    evaluation = simlex.evaluate(model)
    logging.info("Simlex-999 evaluation (spearman)= %s" % evaluation[0])
    fw.write("> Simlex-999 evaluation (spearman)= %s \n" % evaluation[0])
    rw = word_similarity.WordSimilarity("rw")
    evaluation = rw.evaluate(model)
    logging.info("Rare-words evaluation (spearman)= %s" % evaluation[0])
    fw.write("> Rare-words evaluation (spearman)= %s \n" % evaluation[0])
    fw.close()