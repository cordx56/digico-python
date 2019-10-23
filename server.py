#!/usr/bin/env python3

import os
from flask import Flask, request, jsonify
from sentence2vec import Sentence2Vec

app = Flask(__name__)

filesRoot = '/data'
mecabOpt = "-d /usr/lib/mecab/dic/mecab-ipadic-neologd"

s2v = Sentence2Vec(os.path.join(filesRoot, 'wiki.model'), mecabOpt)
s2v.loadDocsFile(os.path.join(filesRoot, 'ansLearn.txt'))

@app.route('/v1/answer')
def getAnswer():
    try:
        q = request.args.get('q')
        ans = s2v.answers(q)
        return jsonify({ 'status': True, 'answer': ans })
    except Exception as e:
        return jsonify({ 'status': False, 'message': str(e) }), 500

if __name__ == "__main__":
    port = 5000
    app.run(host = "0.0.0.0", port = port)
