FROM python:latest as python_base


# Install python dependencies
RUN pip install -U --no-cache-dir pip \
    && pip install --no-cache-dir pipenv

# Copy only requirements, to cache them in docker layer:

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /pysetup

COPY ./Pipfile ./Pipfile.lock /pysetup/

# Project initialization:
RUN pipenv install --dev --system

COPY . .


