worker: redis-server
worker: rq worker j_0
worker: rq worker j_2
worker: rq worker j_2
worker: rq worker j_3
worker: rq worker j_4
init: python manage.py create_admin 
init: python manage.py db init
migrate: python manage.py db migrate
upgrade: python manage.py db upgrade
web: gunicorn -k gevent app:app
