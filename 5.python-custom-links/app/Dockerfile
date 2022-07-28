FROM python:alpine

WORKDIR /app

RUN pip install pymongo

COPY . .

CMD [ "python","/app/main.py" ]