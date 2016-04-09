#!/bin/bash

#mount data directory
mount -t ext4 /dev/xvdg /data

#switch to python 2.7
source /opt/py27environment/bin/activate
mv tweetwordcount EXTwoTweetwordcount

#start hadoop and postgres
/data/start_postgres.sh
sleep 5

#create the tcount database and tweetwordcount table
psql -U postgres -c "DROP DATABASE IF EXISTS tcount;"
psql -U postgres -c "CREATE DATABASE tcount;"
psql -U postgres -d tcount -c "DROP TABLE IF EXISTS tweetwordcount;"
psql -U postgres -d tcount -c "CREATE TABLE tweetwordcount (word TEXT PRIMARY KEY NOT NULL, count INT NOT NULL);"
