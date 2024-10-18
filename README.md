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
python manage.py runserver
```