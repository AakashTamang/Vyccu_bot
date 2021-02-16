FROM python:3.6
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential
RUN apt-get install -y supervisor
ADD . /app
WORKDIR /app
RUN pip3 install spacy
RUN python3 -m spacy download en_core_web_md
RUN python3 -m spacy link en_core_web_md en
RUN pip install -r requirements.txt
COPY ./init/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
CMD ["/usr/bin/supervisord"]

