# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import nltk
from nltk.corpus import sentiwordnet as swn


def analysis(doc):
  sentences = nltk.sent_tokenize(doc)
  stokens = [nltk.word_tokenize(sent) for sent in sentences]
  taggedlist = []
  for stoken in stokens:
    taggedlist.append(nltk.pos_tag(stoken))
    wnl = nltk.WordNetLemmatizer()
    score_list = []
    for idx, taggedsent in enumerate(taggedlist):
      score_list.append([])
      for idx2, t in enumerate(taggedsent):
        newtag = ''
        lemmatized = wnl.lemmatize(t[0])
        if t[1].startswith('NN'):
          newtag = 'n'
        elif t[1].startswith('JJ'):
          newtag = 'a'
        elif t[1].startswith('V'):
          newtag = 'v'
        elif t[1].startswith('R'):
          newtag = 'r'
        else:
          newtag = ''
        if (newtag != ''):
          synsets = list(swn.senti_synsets(lemmatized, newtag))
          # Getting average of all possible sentiments, as you requested
          score = 0
          if (len(synsets) > 0):
            for syn in synsets:
              score += syn.pos_score() - syn.neg_score()
              score_list[idx].append(score / len(synsets))

    # print(score_list)
    sentence_sentiment = []

    for score_sent in score_list:
      if len(score_sent) == 0:
        sentence_sentiment.append(0)
        continue
      sentence_sentiment.append(sum([word_score for word_score in score_sent]) / len(score_sent))

    if sentence_sentiment[0] > 0.03:
      return ("Happy")
    elif sentence_sentiment[0] <-0.03:
      return ("sad")
    else:
      return ("Normal")
