#!/bin/bash

docker run --name webserver -d -p 80:80 webserver-image
# Запускаем контейнер с именем webserver, в фоновом режиме (-d - detach) с портом 80 