FROM python:3

WORKDIR /home/app/web




RUN pip3 install --upgrade pip

RUN pip3 install djangorestframework
RUN pip3 install django-cors-headers
RUN pip3 install channels
RUN pip3 install django_elasticsearch_dsl
RUN pip3 install elasticsearch
RUN pip3 install elasticsearch-dsl
RUN pip3 install django-elasticsearch-dsl
RUN pip3 install djangorestframework-simplejwt
RUN pip3 install channels-redis

RUN pip install -U pip \
                   gunicorn
RUN pip3 install social-auth-app-django

COPY . ./
RUN pip install -r requirements.txt

#ENTRYPOINT ["sh", "migrate_index.sh"]


