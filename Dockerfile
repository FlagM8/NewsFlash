# syntax=docker/dockerfile:1

FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install -r requirements.txt

EXPOSE 5001

COPY . .

CMD [ "python", "-m", "flask", "run" ]
 