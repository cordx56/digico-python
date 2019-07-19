#!/usr/bin/env python3
import MeCab

class MecabObj:
    mecab = None
    def __init__(self, option = ""):
        self.mecab = MeCab.Tagger(option)
    def parse(self, text):
        parsed = self.mecab.parse(text).split("\n")
        for i, v in enumerate(parsed):
            parsed[i] = parsed[i].split("\t")
            if len(parsed[i]) < 2:
                return parsed[:i]
            parsed[i][1] = parsed[i][1].split(",")
        return parsed
