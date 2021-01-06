FROM ubuntu:18.04
RUN apt update
RUN apt install -y apache2
RUN apt-get install -y libapache2-mod-wsgi-py3 python python-pip
RUN pip install requests requests_oauthlib confluent-kafka confluent-kafka[avro] flask
RUN a2enmod wsgi
RUN useradd -ms /bin/bash joe
RUN chmod 777 /var/log/apache2
USER joe
WORKDIR /home/joe

COPY . .

COPY python-kafka.wsgi /etc/apache2/sites-available/python-kafka.conf
ADD python-app/confluent.py /
EXPOSE 80
CMD service apache2 start
