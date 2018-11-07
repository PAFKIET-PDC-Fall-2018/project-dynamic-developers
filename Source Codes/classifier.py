from nltk.classify import NaiveBayesClassifier


def word_feats(words):
    return dict( [(word, True) for word in words] )


arr = []
def classify(sentence):
    positive_vocab = ['awesome', 'outstanding', 'fantastic', 'terrific', 'good', 'nice', 'great', ':)']
    negative_vocab = ['bad', 'terrible', 'useless', 'not', 'hate', ':(']
    neutral_vocab = ['movie', 'the', 'sound', 'was', 'is', 'actors', 'did', 'know', 'words', 'not']

    positive_features = [(word_feats( pos ), 'pos') for pos in positive_vocab]
    negative_features = [(word_feats( neg ), 'neg') for neg in negative_vocab]
    neutral_features = [(word_feats( neu ), 'neu') for neu in neutral_vocab]

    train_set = negative_features + positive_features + neutral_features

    classifier = NaiveBayesClassifier.train( train_set )

    # Predict
    neg = 0
    pos = 0
    sentence = sentence.lower()
    words = sentence.split( ' ' )
    for word in words:
        classResult = classifier.classify( word_feats( word ) )
        if classResult == 'neg':
            neg = neg + 2
        if classResult == 'pos':
            pos = pos + 1

    arr.append('Positive: ' + str( float( pos ) / len( words ) ))
    arr.append('Negative: ' + str( float( neg ) / len( words ) ))
    return arr
