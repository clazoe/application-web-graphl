FROM python:3.9.6-slim
RUN apt-get update \
&& apt-get install gcc -y \
&& apt-get clean
COPY requirements.txt /app/requirements.txt
#COPY migration.sh /
WORKDIR app
RUN pip install -r requirements.txt
COPY . /app
#COPY . /
#ENTRYPOINT []
#CMD ["./migration.sh"]
#ENTRYPOINT uvicorn app.main:app --reload --host 0.0.0.0 --port 1234