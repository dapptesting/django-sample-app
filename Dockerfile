FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /django-sample-app

# Upgrading pip
RUN pip install --upgrade pip

# Install dependencies
COPY requirements.txt /django-sample-app/
RUN pip install -r requirements.txt

# Copy project
COPY . /django-sample-app/

EXPOSE 8000


# Set the entrypoint to our bash script
COPY ./entrypoint.sh /django-sample-app/
RUN chmod +x /django-sample-app/entrypoint.sh
ENTRYPOINT ["/django-sample-app/entrypoint.sh"]

# Expose the port server will listen on
EXPOSE 8000
