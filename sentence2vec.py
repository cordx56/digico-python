#!/usr/bin/env python3
from mecabobj import MecabObj
import re
from gensim.models import word2vec
import numpy as np

class Sentence2Vec:
    w2v = None
    mec = None
    idf = {}
    qaDic = {}
    calcedVec = {}
    def __init__(self, fileName = None, mecabOption = ""):
        self.mec = MecabObj(mecabOption)
        if fileName:
            self.w2v = word2vec.Word2Vec.load(fileName).wv

    def wordFilter(self, wc):
        return wc in ["名詞", "動詞", "形容詞"]
    def getIDF(self, word):
        return self.idf[word] if word in self.idf else max(self.idf.values())
    def genRandVec(self):
        vec = np.random.rand(200)
        vec /= np.linalg.norm(vec)
        return vec
    def getVec(self, sen):
        if sen in self.calcedVec:
            return self.calcedVec[sen]
        vec = np.zeros(200)
        parsed = self.mec.parse(sen)
        for word in parsed:
            if word[0] not in self.w2v:
                self.w2v[word[0]] = self.genRandVec()
            vec += self.getIDF(word[0]) * self.w2v[word[0]]
        vec /= np.linalg.norm(vec)
        self.calcedVec[sen] = vec
        return vec
    def answers(self, sentence):
        vec = self.getVec(sentence)
        vec /= np.linalg.norm(vec)
        res = []
        for key, val in self.qaDic.items():
            res.append({ "a": val, "q": key, "cos": np.sum(vec * self.getVec(key)) })
        return sorted(res, key = lambda x: -x["cos"])
    def loadDocs(self, docs):
        self.idf = {}
        self.qaDic = {}
        self.calcedVec = {}
        qPtrn = re.compile(r"^\s+")
        ansTxt = ""
        for line in [l.rstrip() for l in docs]:
            if qPtrn.match(line):
                line = qPtrn.sub("", line)
                self.qaDic[line] = ansTxt
            else:
                ansTxt = line
            # parsed = filter(lambda x: self.wordFilter(x[1][0]), self.mec.parse(line))
            parsed = self.mec.parse(line)
            idfAdded = []
            for word in parsed:
                if word[0] in idfAdded:
                    continue
                if word[0] not in self.idf:
                    self.idf[word[0]] = 0
                self.idf[word[0]] += 1
                idfAdded.append(word[0])
        for key, val in self.idf.items():
            self.idf[key] = np.log2(len(docs) / self.idf[key])
    def loadDocsFile(self, docsFile):
        with open(docsFile) as f:
            self.loadDocs(f.readlines())
    def saveDocsFile(self, fileName):
        writeDic = {}
        for key, val in self.qaDic.items():
            if val not in writeDic:
                writeDic[val] = []
            writeDic[val].append(key)
        with open(fileName, mode="w", encoding="utf-8") as f:
            for key, val in writeDic.items():
                f.write(key + "\n")
                for q in val:
                    f.write("\t" + q + "\n")
