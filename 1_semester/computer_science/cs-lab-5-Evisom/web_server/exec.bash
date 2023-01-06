id=$(sudo docker container ls --all --quiet --filter "name=webserver")
# получаем id контейнера по его name
docker exec -it $id bash
# Запускаем bash для существующего контейнера 
# -it -interactive -tty (Подсистема TTY используется для использования одного терминала несколькими процессами)
