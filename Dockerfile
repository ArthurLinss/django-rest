FROM python:3.9

ENV DockerHOME=/api 

RUN mkdir -p ${DockerHOME}

ENV PYTHONDONTWRITEBYTECODE=1 
ENV PYTHONUNBUFFERED=1 


RUN pip install --upgrade pip 
RUN pip install django
RUN pip install djangorestframework
RUN pip install markdown # Markdown support for the browsable API.
RUN pip install django-filter # Filtering support
RUN pip install django-environ
RUN pip install httpie


WORKDIR ${DockerHOME}
COPY . ${DockerHOME}

# port where the Django app runs  
EXPOSE 8000  

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

