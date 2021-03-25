FROM python:3.9.2-slim
LABEL maintainer="Whitman Bohorquez"

WORKDIR /microservice

RUN apt-get update && apt-get install -y libpq-dev gcc

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN apt-get autoremove -y gcc

COPY . .
RUN python setup.py install

CMD [ \
"uvicorn", \
"--host", "0.0.0.0", \
"--port", "8000", \
"source.main:app" \
]