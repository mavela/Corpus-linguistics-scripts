import sys
import re

ID,FORM,LEMMA,UPOS,XPOS,FEAT,HEAD,DEPREL,DEPS,MISC=range(10) #the columns of the conllu format

def read_conll(inp,max_sent=0,drop_tokens=True,drop_nulls=True):
    """Yields sentences from conllu"""
    comments=[]
    sent=[]
    yielded=0
    for line in inp:
        line=line.strip()
        if line.startswith("#"):
            comments.append(line)
        elif not line:
            if sent:
                yield sent,comments
                yielded+=1
                if max_sent>0 and yielded==max_sent:
                    break
                sent,comments=[],[]
        else:
            cols=line.split("\t")
            if drop_tokens and "-" in cols[ID]:
                continue
            if drop_nulls and "." in cols[ID]:
                continue
            sent.append(cols)
    else:
        if sent:
            yield sent,comments


remove_spec_characters=re.compile("[^a-zäöå0-9 -]")
for sentence,comments in read_conll(sys.stdin):
    words=[columns[1] for columns in sentence]
    sentence_text=" ".join(words)
    #now you can do as you please with the sentence text
    #this will lowercase and remove characters not recognized by us
    sentence_text=remove_spec_characters.sub("",sentence_text.lower())
    sentence_text=re.sub(r"\s+"," ",sentence_text) #remove multiple whitespace, dunno if we need this
    print(sentence_text)
    
