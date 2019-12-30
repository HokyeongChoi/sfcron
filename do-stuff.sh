#!/bin/bash

cd /home/ubuntu/cron

/home/ubuntu/cron/final_auto_crawling_db_update.py

/home/ubuntu/cron/man_proportion_prediction.R >> /home/ubuntu/cron/predlog.log

/home/ubuntu/cron/image_retriever.py

/home/ubuntu/cron/sqltojson.py

/home/ubuntu/cron/get_restaurant.py

scp -i /home/ubuntu/.ssh/sfshiny.pem /home/ubuntu/cron/SEOUL_FESTIVAL.db ubuntu@ec2-35-170-234-69.compute-1.amazonaws.com:/home/ubuntu/sfplumber

/home/ubuntu/cron/git-update.sh

cd /home/ubuntu/web

/home/ubuntu/cron/git-update.sh
