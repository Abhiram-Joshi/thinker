web: cd backend && gunicorn thinker.wsgi
release: cd backend && python manage.py makemigrations && python manage.py makemigrations account && python manage.py migrate