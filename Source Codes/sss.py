

# importing libraries [By S M Fasih Ali 60838] 
import nltk 
from nltk.corpus import sentiwordnet as swn # for sentimental analysis [By S M Fasih Ali 60838] 


def analysis(doc): # takes one aurgumentdoc which is the text of tweets in our case  [By S M Fasih Ali 60838] 
  sentences = nltk.sent_tokenize(doc)  # tokenize the tweets into sentences [By S M Fasih Ali 60838] 
  stokens = [nltk.word_tokenize(sent) for sent in sentences] # tokenize sentence into words [By S M Fasih Ali 60838] 
  taggedlist = []
  for stoken in stokens:
    taggedlist.append(nltk.pos_tag(stoken))
    wnl = nltk.WordNetLemmatizer() # convert all the verbs to their base form [By S M Fasih Ali 60838] 
    score_list = [] # lsit of score of sentence [sentiments scores] [By S M Fasih Ali 60838] 
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
          synsets = list(swn.senti_synsets(lemmatized, newtag)) # find synonyms of words for simplicity to analize [By S M Fasih Ali 60838]  
          # Getting average of all possible sentiments, as  requested [By S M Fasih Ali 60838] 
          score = 0
          if (len(synsets) > 0):
            for syn in synsets:
              score += syn.pos_score() - syn.neg_score()
              score_list[idx].append(score / len(synsets))

    # print(score_list)
    sentence_sentiment = []

    for score_sent in score_list: # sentiment analysis of each word [By S M Fasih Ali 60838]  
      if len(score_sent) == 0:
        sentence_sentiment.append(0)
        continue
      sentence_sentiment.append(sum([word_score for word_score in score_sent]) / len(score_sent)) # dividing score of sum of all words by score of sentece [By S M Fasih Ali 60838] 
    if sentence_sentiment[0] > 0.03: # if greater than 0.03 positive [By S M Fasih Ali 60838] 
      return ("Happy")
    elif sentence_sentiment[0] <-0.03: # if lest than -0.05 negative [By S M Fasih Ali 60838] 
      return ("sad")
    else:# 
      return ("Normal") #else neutral [By S M Fasih Ali 60838] 
