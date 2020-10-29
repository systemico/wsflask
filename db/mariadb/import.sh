#!/bin/bash
cd /docker-entrypoint-initdb.d/
mysql --user=root --password=wsflask wsflask < model.db.sql
