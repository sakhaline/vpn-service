FROM python:3.12.1-slim
LABEL maintainer="alexandra.ivva@gmail.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --upgrade pip && python -m pip install -r requirements.txt

COPY . /app/

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0", "port=5000"]
