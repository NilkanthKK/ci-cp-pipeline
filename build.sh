set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --noinput
python manage.py migrate 

if [[$CRETE_SUPERUSER]];
then 
    python manage.py createsuperuser --no-input--email "$DJANGO_SUPERUSER_EMAIL"
fi 
 