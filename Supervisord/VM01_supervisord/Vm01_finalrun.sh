#!/bin/sh 

wget http://15.213.6.35:443/nexus/content/repositories/chef/NewRepo/VM01_supervisord/supervisord.conf

mv  supervisord.conf /usr/etc/supervisord.conf -f

yum install python-setuptools -y >> WQC_LOG.log

easy_install supervisor >> WQC_LOG.log

service supervisord restart