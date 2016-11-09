echo "export CRAWL_TIMEOUT=240" >> /etc/profile 
echo "export CRAWLER_QUEUE=DATA_SERVICE_QUEUE" >> /etc/profile 
echo "export DAYS=5" >> /etc/profile 
echo "export dbUri=jdbc:mysql://localhost:3306/wqc" >> /etc/profile 
echo "export EUREKA_CLIENT_HOSTNAME=localhost" >> /etc/profile 
echo "export HTTP_PROXY=proxy.sgp.hp.com" >> /etc/profile 
echo "export HTTP_PROXY_PORT=8080" >> /etc/profile 
echo "export HTTP_PROXY_URL=proxy.sgp.hp.com" >> /etc/profile 
echo "export IS_PROXY_REQUIRED=TRUE" >> /etc/profile 
echo "export JBP_CONFIG_SPRING_AUTO_RECONFIGURATION='[enabled: false]'" >> /etc/profile 
echo "export POPULAR_REPORTS=PopularReports" >> /etc/profile 
echo "export queueUri=amqp://guest:guest@localhost:15672/" >> /etc/profile 
echo "export REPORT_QUEUE=REPORT_DATA_QUUEE" >> /etc/profile 
echo "export SOCKET_IO_URL=http://localhost:8086/post_report_packet" >> /etc/profile 
echo "export TOTAL_POPULAR_WEBSITE=5" >> /etc/profile 
echo "export totalpopularwebsite=5" >> /etc/profile 
echo "export CRAWLER_SERVICE_URL=http://localhost:8085/crawlreport?" >> /etc/profile 
echo "export DATASERVICE_UPDATE_REPORT_URL=http://localhost:8083/dataservice/update" >> /etc/profile 
echo "export RABBITMQ_SERVICE=amqp://guest:guest@localhost:15672/" >> /etc/profile 
echo "export CRAWLER_QUEUE=DATA_SERVICE_QUEUE" >> /etc/profile 
echo "export REPORT_QUEUE=REPORT_DATA_QUEUE" >> /etc/profile 
echo "export CRAWL_LEVEL=1" >> /etc/profile 
echo "export WEBSITE_SEPARATER=","" >> /etc/profile 
echo "export REPORT_TABLE_DATA_LIMIT=11" >> /etc/profile 
echo "export SOCKET_IO_URL=http://localhost:8086" >> /etc/profile 
echo "export CACHE_POPULAR_REPORT_URL=http://localhost:8084/read-popular-websites" >> /etc/profile 
echo "export CACHE_RETRIEVE_REPORT_URL=http://localhost:8082/websitequalitychecker/popularcrawlreport?" >> /etc/profile 
echo "export DATASERVICE_UPDATE_REPORT_URL=http://localhost:8083/dataservice/update" >> /etc/profile 
echo "export DATASERVICE_CONNECTION_TEST_URL=http://localhost:8083/dataservice/check-Availability" >> /etc/profile 
echo "export CRAWLER_SERVICE_CONNECTION_TEST_URL=http://localhost:8085/crawlerhealthcheck" >> /etc/profile 
echo "export CACHE_CONNECTION_TEST_URL=http://localhost:8084/check-Availability" >> /etc/profile 
echo "export SERVICE_TIMEOUT_THRESHOLD=400000" >> /etc/profile 
echo "export ROUTER_SERVICE_URL=http://localhost:8084/get-next-action" >> /etc/profile 
echo "export CRAWLER_HEALTH_CHECK_URL=/crawler-health-check" >> /etc/profile 
echo "export NODE_HEALTH_CHECK_URL=/node-health-check" >> /etc/profile 
echo "export QUEUE_HEALTH_CHECK_URL=/queue-health-check" >> /etc/profile 
echo "export SERVICE_RETRY_THRESHOLD=30000" >> /etc/profile 
echo "export REQUEST_VOLUME_THRESHOLD=0" >> /etc/profile 
echo "export SLEEP_WINDOW_TIME=300000" >> /etc/profile 
echo "export RABBITMQ_SERVICE=amqp://guest:guest@localhost:15672/" >> /etc/profile 
echo "export CRAWLER_QUEUE=DATA_SERVICE_QUEUE" >> /etc/profile 
echo "export REPORT_QUEUE=REPORT_DATA_QUEUE" >> /etc/profile 
echo "export NODE_SERVICE_CONNECTION_TEST_URL=http://localhost:8086/listener-health-check" >> /etc/profile 
echo "export QUEUE_SERVICE_CONNECTION_TEST_URL=http://localhost:15672/api/aliveness-test/vdc062b83bcbc412e946b0f5be889218d" >> /etc/profile
echo "export QUEUE_URI=amqp://rabbitmq:guest@localhost:5672" >> /etc/profile"
" 