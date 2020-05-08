#!bin/sh

mkdir /opt/DemoApp >> WQC_LOG.log
cd /opt/
unzip workspace.zip -d /opt/DemoApp >> WQC_LOG.log
cd /opt/DemoApp >> WQC_LOG.log
cd workspace

yum install python-setuptools -y >> WQC_LOG.log

easy_install supervisor >> WQC_LOG.log
mkdir  -p /etc/supervisor/conf.d/

touch /usr/etc/supervisord.conf

wget http://15.213.6.35:443/nexus/content/repositories/Nisha1/sylesh/supervisord

cp supervisord /etc/rc.d/init.d

chmod 777 /etc/rc.d/init.d/supervisord

echo "[supervisord]" >> /usr/etc/supervisord.conf
echo "environment=SOCKET_IO_URL="15.213.6.39:8086",CRAWL_TIMEOUT="240",CRAWLER_QUEUE="DATA_SERVICE_QUEUE",DAYS="5",dbUri="jdbc:mysql://15.213.6.38:3306/fsi_guid_dev",EUREKA_CLIENT_HOSTNAME="15.213.6.38",HTTP_PROXY="proxy.sgp.example.com",HTTP_PROXY_PORT="8080",HTTP_PROXY_URL="proxy.sgp.hp.com",IS_PROXY_REQUIRED="TRUE",POPULAR_REPORTS="PopularReports",queueUri="amqp://guest:guest@15.213.6.39:5672",REPORT_QUEUE="REPORT_DATA_QUEUE",SOCKET_IO_URL_PACKET="http://15.213.6.39:8086/post_report_packet",TOTAL_POPULAR_WEBSITE="5",totalpopularwebsite="5",CRAWLER_SERVICE_URL="http://15.213.6.39:8085/crawlreport?",DATASERVICE_UPDATE_REPORT_URL="http://15.213.6.38:8083/dataservice/update",RABBITMQ_SERVICE="amqp://guest:guest@15.213.6.39:5672",CRAWL_LEVEL="1",WEBSITE_SEPARATER=",",REPORT_TABLE_DATA_LIMIT="11",SOCKET_IO_URL="http://15.213.6.39:8086",CACHE_POPULAR_REPORT_URL="http://15.213.6.38:8084/read-popular-websites",CACHE_RETRIEVE_REPORT_URL="http://15.213.6.38:8082/websitequalitychecker/popularcrawlreport?",DATASERVICE_CONNECTION_TEST_URL="http://15.213.6.38:8083/dataservice/check-Availability",CRAWLER_SERVICE_CONNECTION_TEST_URL="http://15.213.6.39:8085/crawlerhealthcheck",CACHE_CONNECTION_TEST_URL="http://15.213.6.38:8084/check-Availability",SERVICE_TIMEOUT_THRESHOLD="400000",ROUTER_SERVICE_URL="http://15.213.6.38:8084/get-next-action",CRAWLER_HEALTH_CHECK_URL="/crawler-health-check",NODE_HEALTH_CHECK_URL="/node-health-check",QUEUE_HEALTH_CHECK_URL="/queue-health-check",SERVICE_RETRY_THRESHOLD="30000",REQUEST_VOLUME_THRESHOLD="0",SLEEP_WINDOW_TIME="300000",NODE_SERVICE_CONNECTION_TEST_URL="http://15.213.6.39:8086/listener-health-check",QUEUE_SERVICE_CONNECTION_TEST_URL="http://15.213.6.39:5672/api/aliveness-test/vdc062b83bcbc412e946b0f5be889218d",dbUser="root",ALL_REPORTS="allReports",CACHE_SERVICE_URL="http://15.213.6.38:8082/websitequalitychecker/cacheloader",NEXT_BEST_ACTION_KEY="nextBestAction",CACHE_URL="http://15.213.6.38:8082/websitequalitychecker/cacheloader",DATABASE_CHECK_AVAILABILITY="http://15.213.6.38:8083/dataservice/check-Availability",TO="prithvi.sureka@example.com",FROM="database.alert@email.com",cacheUri="redis://15.213.6.38:6379"" >> /usr/etc/supervisord.conf

echo "nodaemon=true" >> /usr/etc/supervisord.conf

echo "[program:eureka]" >>  /usr/etc/supervisord.conf
echo "command=java -Xms512m -Xmx768m -jar /opt/DemoApp/workspace/service-registry-eureka/target/eureka-service-0.0.1-SNAPSHOT.jar">> /usr/etc/supervisord.conf
echo "stdout_logfile=/var/log/eureka.log" >>/usr/etc/supervisord.conf


echo "[program:hystrix-dashboard]">>/usr/etc/supervisord.conf
echo "command=java -Xms512m -Xmx768m -jar /opt/DemoApp/workspace/hystrix-dashboard/target/hystrix-service-0.0.1-SNAPSHOT.jar ">>/usr/etc/supervisord.conf
echo "stdout_logfile=/var/log/hystrix.log" >>/usr/etc/supervisord.conf

echo "[program:web-crawler]" >>/usr/etc/supervisord.conf
echo "command=java -Xms512m -Xmx1024m -jar /opt/DemoApp/workspace/web-crawler/target/web-crawler-service-1.0.jar">>/usr/etc/supervisord.conf
echo "stdout_logfile=/var/log/web-crawler.log" >>/usr/etc/supervisord.conf


cd /opt/DemoApp/workspace

wget http://15.213.6.35:443/nexus/content/repositories/chef/NewRepo/demo_modules.tar

tar xvf /opt/DemoApp/workspace/demo_modules.tar

mv /opt/DemoApp/workspace/user_interface_modules/ /opt/DemoApp/workspace/user-interface/
mv /opt/DemoApp/workspace/user-interface/user_interface_modules/ /opt/DemoApp/workspace/user-interface/node_modules/
mv /opt/DemoApp/workspace/node_modules/ /opt/DemoApp/workspace/node-socket-io/

echo "[program:socket-install]">>/usr/etc/supervisord.conf
echo "directory=/opt/DemoApp/workspace/node-socket-io">>/usr/etc/supervisord.conf
echo "command=/usr/local/bin/npm install" >>/usr/etc/supervisord.conf
echo "stdout_logfile=/var/log/install_npm.log " >>/usr/etc/supervisord.conf

echo "[program:socket-node]" >>/usr/etc/supervisord.conf
echo "command=/usr/local/bin/node /opt/DemoApp/workspace/node-socket-io/server.js " >>/usr/etc/supervisord.conf
echo "stdout_logfile=/var/log/node.log" >>/usr/etc/supervisord.conf

echo "[program:ui-install]" >>/usr/etc/supervisord.conf
echo "directory=/opt/DemoApp/workspace/user-interface" >>/usr/etc/supervisord.conf
echo "command=/usr/local/bin/npm install" >>/usr/etc/supervisord.conf
echo "stdout_logfile=/var/log/UI_NPM.log " >>/usr/etc/supervisord.conf
 
echo "[program:UI]">>/usr/etc/supervisord.conf
echo "command=/usr/local/bin/node /opt/DemoApp/workspace/user-interface/server.js">>/usr/etc/supervisord.conf
echo "stdout_logfile=/var/log/ui.log " >>/usr/etc/supervisord.conf


exit
 

