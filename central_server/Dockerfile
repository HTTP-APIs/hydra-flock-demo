FROM tiangolo/uwsgi-nginx-flask:flask-python3.5-index-upload

MAINTAINER Akshay Dahiya <xadahiya@gmail.com>


COPY ./requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

RUN rm -rf *


# Clone and install hydra-py ( will be available by name hydra)
RUN git clone https://github.com/andrejsab/hydra-py
RUN pip install ./hydra-py/


# Clone hydrus into hydrus_main
RUN git clone -b develop https://github.com/HTTP-APIs/hydrus hydrus_main

COPY  . /app/

ENV PYTHONPATH $PYTHONPATH:/app/hydrus_main/:/app/

RUN mv hydrus_main/hydrus/uwsgi.ini ./uwsgi.ini

RUN mv api_docs/doc_gen.py hydrus_main/hydrus/metadata/
RUN mv api_docs/doc.py hydrus_main/hydrus/metadata/

ENV MESSAGE "Hail Hydra"
