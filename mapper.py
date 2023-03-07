#!/usr/bin/env python
"""mapper.py"""

import sys,re

#speech cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), ' ', text)
    text = re.sub('[\d\n]', ' ', text)
    return text

def mapper(argv)
    for president in sys.stdin:
        speech_count=0
        speech_valences=[]
    # input comes from STDIN (standard input)
        for speech in president:
            speech_count+=1
            cleaned=clean_text(speech)
            valences=[]
            word_count=0
            for line in speech:
                # remove leading and trailing whitespace
                line = line.strip()
                # split the line into words
                #words = line.split()
                # increase counters
                for word in line.split():
                    word_count+=1
                    for row in valences:
                        if row[0]==word:
                            valences.append(row[0]) 
                    # write the results to STDOUT (standard output);
                    # what we output here will be the input for the
                    # Reduce step, i.e. the input for reducer.py
                    #
                    # tab-delimited; the trivial word count is 1
                    #print ('%s\t%s' % (word, 1))
            speech_valence=(1/word_count)*(sum(valences))
            speech_valences.append(speech_valence)
        prez_valence=(1/speech_count)*(sum(speech_valences))
        print(prez_valence)

if __name__ == "__main__":
    mapper(sys.argv)
