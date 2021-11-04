FROM python
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install django-password-validators
RUN pip install -r requirements.txt
COPY . /code/




