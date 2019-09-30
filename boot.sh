source imdb/bin/activate
flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - imdb:app