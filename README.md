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
3. Install and run Redis server
```bash
redis-server
```
4. Run Celery server
```bash
celery -A planeks_news worker -l info
celery -A planeks_news worker --pool=solo -l info 
```
5. Run the server
```bash
python manage.py runserver
```