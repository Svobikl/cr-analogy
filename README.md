# cr-analogy

Download HR corpus for training here (or directly from this GitHub repository - check the folder "data"): 
```
https://uloz.to/!MeZ0BN3JkU7R/corpus-txt-zip
```


Analogy corpus is in folder "data". 

If you decide to use HR corpus, or analogy test data,, please cite the paper. The BibTeX format is:

```
@inproceedings{DBLP:conf/lrec/SvobodaB18,
  author    = {Luk{\'{a}}s Svoboda and
               Slobodan Beliga},
  title     = {Evaluation of Croatian Word Embeddings},
  booktitle = {Proceedings of the Eleventh International Conference on Language Resources
               and Evaluation, {LREC} 2018, Miyazaki, Japan, May 7-12, 2018.},
  year      = {2018},
  crossref  = {DBLP:conf/lrec/2018},
  timestamp = {Fri, 18 May 2018 10:35:14 +0200},
  biburl    = {https://dblp.org/rec/bib/conf/lrec/SvobodaB18},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```


### Reference
Corpus is merged from Wikipedia data plus fHrWaC - Filtered Croatian Web Corpus (hrWaC). 



Text Analysis and Knowledge Engineering Lab (http://takelab.fer.hr)
Faculty of Electrical Engineering and Computing, University of Zagreb

Version: 1.0
Release date: July 27, 2013

1 DESCRIPTION

fHrWaC is a filtered version of hrWaC, Croatian web corpus compiled by Ljubešić
and Erjavec (2011). In fHrWac, much of the non-textual content (e.g., code
snippets and formatting structure), encoding errors, and foreign-language
content is removed. fHrWaC is suitable for NLP tasks in which linguistic
quality is more important than coverage (e.g., for parsing).

The filtering was done heuristically on a per-document and per-sentence basis.
The exact parameter setting of the filtering procedure are deducible from the
source code (see below). For details, please refer to the following paper: 

  Jan Šnajder, Sebastian Padó, Željko Agić (2013). Building and Evaluating a
  Distributional Memory for Croatian. Proceedings of the 51st Annual Meeting of
  the Association for Computational Linguistics (Volume 2: Short Papers), Sofia:
  Association for Computational Linguistics, 2013

Should you decide to use fHrWaC, please cite the paper. The BibTeX format is:

@InProceedings{snajder2013building,
  title={Building and Evaluating a Distributional Memory for Croatian},
  author={{\v S}najder, Jan and Pad{\'o}, Sebastian and Agi{\'c}, {\v Z}eljko},
  booktitle={51st Annual Meeting of the Association for Computational Linguistics},
  year={2013},
  pages={in press}
}

2 DATASET

Download the fHrWaC from: http//takelab.fer.hr/data/fhrwac/fhrwac.1.0.tok.seg.tar.gz 

The corpus contains 50,940,598 sentences (one sentence per line, tokenized) and
1,232,632,208 tokens (1.2G tokens). The average sentence length is 24.1974
tokens.  

fHrWaC is licensed under a Creative Commons Attribution-ShareAlike 3.0
Unported License.
