# Dockerfile

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python

# Allows docker to cache installed dependencies between builds
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY mysite code
WORKDIR /code

EXPOSE 8000
# entrypoint to run the django.sh file
ENTRYPOINT ["mysite/django.sh"]

#ENTRYPOINT ["python", "mysite/manage.py"]
#CMD ["runserver", "0.0.0.0:8000"]


