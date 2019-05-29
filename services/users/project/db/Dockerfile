# base image
FROM postgress:11.3-alpine

# run create.sql on init
ADD create.sql /docker-entrypoint-initdb.d
