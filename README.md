# dns-server

DNS Server with Django admin **(Python 3.11)**

### Install project

```bash
git clone https://github.com/AikoSora/dns-server.git && cd dns-server
```

```bash
python3 -m venv env && source env/bin/activate
```

```bash
python -m pip install pipenv && pipenv install
```

```bash
cd app && python manage.py migrate
```

### Start DNS server

```bash
sudo python manage.py rundnsserver --host $YOUR_IP
```

use dig to test server

```bash
dig @$YOUR_IP example.com
```

### Start Django Admin

```bash
python manage.py createsuperuser
```

```bash
python manage.py runserver
```

## Run with docker

Clone repo

```bash
git clone https://github.com/AikoSora/dns-server.git && cd dns-server
```

Configure `example.env` file and run the following command

```bash
cp example.env .env
```

Configure `docker-compose.override.yml.dist` file and run the following command

```bash
cp docker-compose.override.yml.dist docker-compose.override.yml
```

Run docker-compose

```bash
docker-compose up -d
```

Perform the migration

```bash
docker-compose exec -w /app server python manage.py migrate
```

Create superuser in admin

```bash
docker-compose exec -w /app server python manage.py createsuperuser
```
