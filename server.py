#!/usr/bin/env python3

import os
from flask import Flask, request, jsonify
from sentence2vec import Ibpro, Trazo

app = Flask(__name__)

filesRoot = '/data'
mecabOpt = "-d /usr/lib/mecab/dic/mecab-ipadic-neologd"

ibp = Ibpro(os.path.join(filesRoot, 'wiki.model'), mecabOpt)
ibp.loadDocsFile(os.path.join(filesRoot, 'ansLearn.txt'))
trz = Trazo(os.path.join(filesRoot, 'wiki.model'), mecabOpt)
trz.loadDocsFile(os.path.join(filesRoot, 'ansLearn.txt'))

@app.route('/v1/answer')
def getAnswer():
    try:
        q = request.args.get('q')
        if q is None or len(q) < 1:
            return jsonify({ 'status': False, 'message': "Invalid request" }), 400
        en = request.args.get('engine')
        if en == 'ibp':
            ans = ibp.answers(q)
        else:
            ans = trz.answers(q)
        return jsonify({ 'status': True, 'answer': ans })
    except Exception as e:
        return jsonify({ 'status': False, 'message': str(e) }), 500

if __name__ == "__main__":
    port = 5000
    app.run(host = "0.0.0.0", port = port)
