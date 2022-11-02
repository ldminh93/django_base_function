# OSインストール
FROM centos
RUN yum update -y

# PHPをインストール
RUN yum install https://dl.fedoraproject.org/pub/epel/epel-release-latest-7.noarch.rpm -y

#RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm

RUN rpm -Uvh http://remi.conetix.com.au/enterprise/remi-release-7.rpm


RUN sed -e "s/rpms\.remirepo\.net/remi.conetix.com.au/g" /etc/yum.repos.d/remi-safe.repo > tmp.txt
RUN cp tmp.txt /etc/yum.repos.d/remi-safe.repo
RUN sed -e "s/rpms\.remirepo\.net/remi.conetix.com.au/g" /etc/yum.repos.d/remi.repo > tmp.txt
RUN cp tmp.txt /etc/yum.repos.d/remi.repo
RUN sed -e "s/rpms\.remirepo\.net/remi.conetix.com.au/g" /etc/yum.repos.d/remi-php71.repo > tmp.txt
RUN cp tmp.txt /etc/yum.repos.d/remi-php71.repo

RUN yum install --enablerepo=remi,remi-php71 php7-intl php php-devel php-cli php-common php-mysql php-opcache php-mbstring php-pdo php-gd php-xml php-mcrypt php-intl zip unzip -y --skip-broken

# コンポーザをインストール
RUN curl -sS https://getcomposer.org/installer | php --disable-json
#RUN mv composer.phar /usr/local/bin/composer

WORKDIR /var/src

# npm インストール・実行
# RUN yum install -y npm node
# RUN npm install

# git インストール
RUN yum install -y git

# コンポーザでインストール
# ENTRYPOINT [ "composer", "install" ]
