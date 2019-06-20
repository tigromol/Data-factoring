FROM mongo

ENV MONGO_INITDB_ROOT_PASSWORD=panin

COPY init.js /docker-entrypoint-initdb.d/

#ENTRYPOINT [ "docker-entrypoint.sh" ]