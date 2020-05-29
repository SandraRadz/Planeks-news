# Planeks-news

## How to run project

1. Install dependencies
```bash
pip install -r requirements.txt
```
2. Commit DB migrations
```bash
python manage.py migrate
```
3. Initialize db with roles
```bash
python manage.py loaddata initial_role_data.json
```
4. Create superuser to get access to admin site
```bash
python manage.py createsuperuser
```
5. Install and run Redis server
```bash
redis-server
```
6. Run Celery server
```bash
celery -A planeks_news worker -l info
celery -A planeks_news worker --pool=solo -l info 
```
7. Run the server
```bash
python manage.py runserver
```