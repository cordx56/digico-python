FROM python:3.7

RUN apt update
RUN apt install -y mecab libmecab-dev mecab-ipadic-utf8 swig
RUN git clone --depth=1 https://github.com/neologd/mecab-ipadic-neologd
RUN cd ./mecab-ipadic-neologd && ./bin/install-mecab-ipadic-neologd -y -p /var/lib/mecab/dic/mecab-ipadic-neologd
RUN rm -rf ./mecab-ipadic-neologd
RUN ln -s /var/lib/mecab/dic /usr/lib/mecab/dic

RUN cd /tmp && \
    curl -L -o "CRF++-0.58.tar.gz" "https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7QVR6VXJ5dWExSTQ" && \
    tar xvf "CRF++-0.58.tar.gz" && \
    cd "CRF++-0.58" && \
    ./configure && \
    make && \
    make install && \
    ldconfig

COPY ./buildfiles/cabocha-0.69.tar.bz2 /tmp/
RUN cd /tmp && \
    tar xvf "cabocha-0.69.tar.bz2" && \
    cd "cabocha-0.69" && \
    ./configure --with-charset=utf8 && \
    make && \
    make install && \
    pip install python/ && \
    ldconfig

RUN pip install mecab-python3

RUN pip install pipenv
COPY Pipfile* /tmp/
RUN cd /tmp && pipenv install --system

RUN rm -rf /tmp/*

RUN mkdir /script
WORKDIR /script
