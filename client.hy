
(import os sys traceback discord)
(import [sentence2vec [Sentence2Vec]])

(setv client (discord.Client))

(setv docsFile (. sys argv [2]))

(setv mecabOpt "-d /usr/lib/mecab/dic/mecab-ipadic-neologd")
(if (< 3 (len sys.argv))
    (setv mecabOpt (. sys argv [3]))
)

(setv s2v (Sentence2Vec (. sys argv [1]) mecabOpt))
(s2v.loadDocsFile docsFile)

(defn answerText [ans]
    (setv txt (+ (. ans [0] ["a"]) "\n"))
    (setv txt (+ txt "\n"))
    (lfor i (range (if (< 3 (len ans)) 3 (len ans))) (do
        (nonlocal txt)
        (setv txt (+ txt (cut (str (. ans [i] ["cos"])) 0 6) "    " (. ans [i] ["a"]) "\n"))
        (setv txt (+ txt "          " (. ans [i] ["q"]) "\n"))
    ))
    (setv txt (+ txt "\n"))
    (return txt)
)


(while True
    (setv q (input))
    (setv a (answerText (s2v.answers q)))
    (print a)
)
