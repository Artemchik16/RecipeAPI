FROM python:3.10-alpine3.13

ENV PYTHONUNBUFFERED 1

RUN mkdir /RecipeAPI
WORKDIR /RecipeAPI
ADD . /RecipeAPI/
RUN pip install -r requirements.txt

EXPOSE 8000
