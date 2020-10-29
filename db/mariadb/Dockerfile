FROM mariadb:10.0.29
COPY ["model.db.sql", "/docker-entrypoint-initdb.d/"]
COPY ["import.sh", "/docker-entrypoint-initdb.d/"]
