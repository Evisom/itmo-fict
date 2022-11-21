FROM debian:latest 
# Задаем базовый образ (последняя версия Debian)

LABEL maintainer="Dmitriy Shishmintsev"
# Задаем метаданные (необязательно)

RUN apt-get update
# Обновляем списки репозиториев
RUN apt-get install -y apache2
# Устанавливаем apache2 (-y - установка без вопросов [Y/N])

COPY ./index.html /var/www/html/index.html
# Копируем наш index.html 

RUN sed -i -e 's/Listen 80/Listen 80\nServerName localhost/' /etc/apache2/ports.conf
# Добавляем ServerName в файле после строки Listen 80

CMD ["apache2ctl", "-D", "server"]
# Запускаем apache2 с именем server

EXPOSE 80
# Открываем 80 порт для нашего контейнера
