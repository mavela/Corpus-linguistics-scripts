import sys
import re
import subprocess
import os



def read_text(inp):
    feats = []
    id = None
    for line in inp:
        line=line.strip()
        if line.startswith("# ID"):
            if id != None:
                yield(id, feats) # tässä tiedot mitä halutaan kerätä
                feats = []
                id =line # tätä voi vielä putsatakin
                
            elif id == None:
                id =line
            else:
                continue
        else:
            if line.startswith("#"): #tämä skippaa nyt muut metatiedot
                continue
            else:
                if line:
                    line=line.split("\t")
#                    feats.append(line[5]) # feats on periaatteessa tekstiä sitä mitä halutaan kerätä
                    feats.append(line[1]) #nyt tämä kerää pelkät sanat, mutta esim. 2lla saa lemmat (kolmas sarake) 
    yield(id, feats)

for id, feats in read_text(sys.stdin):
        print(id, " ".join(feats))
