# coding: utf-8

# standard
import csv
import logging
# math
from scipy import stats

from nlp import similarity, transformation

class WordSimilarity:

    def __init__(self, evaluation_data):
        if evaluation_data not in ('wordsim353', 'rg', 'mc','simlex999', 'rw','mc-cs','rg-cs', 'wordsim353-cs'):
            raise ValueError("'similarity_measure' can only be either 'wordsim353', 'rg','mc', 'rw' or 'simlex999'")
        input_file = open('evaluation_data/'+evaluation_data+'.tsv', 'r')
        csv_reader = csv.reader(input_file, delimiter='\t')
        self.ground_truth = []
        for row in csv_reader:
            word_1 = row[0]
            word_2 = row[1]
            similarity = row[2]
            self.ground_truth.append((word_1, word_2, similarity))
        print(self.ground_truth)


    def get_word_vec(self,word, model):
        try:
            uni_word = word.decode('utf-8')
            vec1 = model.wv.syn0norm[model.wv.vocab[uni_word].index]
        except KeyError:
            logging.error("Word %s was not found" % word)
            vec_UNK = []

            for i in range (len(model.wv.syn0norm[0])):
                vec_UNK.append(0.0)

            for i in range(1,10,1):
                index = 0
                for vecPart in model.wv.syn0norm[-i]:
                    vec_UNK[index] += float(vecPart) / 10.0
                    index += 1


            return vec_UNK
            #return {0}
        return vec1

    def measure_similarity(self ,word_1_vec, word_2_vec, similarity_measure='cosine', binary=False, useGensimModel=True):
        similarity_function = None
        if similarity_measure not in ('cosine', 'jaccard'):
            raise ValueError("'similarity_measure' can only be either 'cosine or 'jaccard'")
        elif similarity_measure == 'cosine':
            similarity_function = similarity.cosine
        elif similarity_measure == 'cosinenorm':
            similarity_function = similarity.cosine_norm
        elif similarity_measure == 'jaccard':
            similarity_function = similarity.jaccard


        return similarity_function(word_1_vec, word_2_vec)

    def evaluate(self, semantic_model, similarity_measure='cosine', binary=False, correlation_measure='spearman'):

        if correlation_measure not in ('pearson', 'spearman'):
            raise ValueError("'similarity_measure' can only be either 'pearson or 'spearman'")

        truth = []
        estimation = []
        for word_1, word_2, similarity in self.ground_truth:
            word_1_vector = self.get_word_vec(word_1,semantic_model)
            word_2_vector = self.get_word_vec(word_2,semantic_model)
            if (len(word_1_vector) > 1 and len(word_2_vector) > 1):
                estimated_similarity = self.measure_similarity(word_1_vector,
                                                                     word_2_vector,
                                                                     similarity_measure=similarity_measure,
                                                                     binary=binary, useGensimModel=True)
                truth.append(similarity)
                estimation.append(estimated_similarity)

        if correlation_measure == 'pearson':
            return stats.pearsonr(truth, estimation)
        elif correlation_measure == 'spearman':
            return stats.spearmanr(truth, estimation)

