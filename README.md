# CI/CD
Для создания образа использовать команду:
```
docker build -t server .
```
Для запуска контейнера:
```
docker run -d -p 8000:8000 server
```
Либо можно использовать docker-compose и команду:
```
docker-compose up -d
```
