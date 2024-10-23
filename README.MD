# Бандл python-приложение + premetheus + grafana

Устанавливаем зависимости:
```sh
pip3 install -r ./requirements.txt
```

Запускаем main.py:
```sh
python3 ./main.py
```

Запускаем Prometheus и Grafana:
```sh
docker-compose up
```

Приложение: http://localhost:5000/process
Метрики: http://localhost:8000
Prometheus: http://localhost:9090
Grafana (логин: admin, пароль: admin): http://localhost:3000


