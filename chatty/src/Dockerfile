FROM python:3

WORKDIR /var/www/html

RUN pip3 install djangorestframework
RUN pip3 install django-cors-headers
RUN pip3 install channels
RUN pip3 install django_elasticsearch_dsl
RUN pip3 install elasticsearch
RUN pip3 install elasticsearch-dsl
RUN pip3 install django-elasticsearch-dsl
RUN pip3 install djangorestframework-simplejwt
RUN pip3 install channels_redis
RUN pip3 install python-social-auth
RUN pip3 install social-auth-app-django
COPY . ./
#ENV PATH="/env/bin:$PATH"
RUN pip3 install -r requirements.txt
RUN chmod 777 migrate_index.sh
#ENTRYPOINT ["sh", "./migrate_index.sh"]