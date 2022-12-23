FROM python:3.7

RUN mkdir /app
WORKDIR /app
ADD . /app/
RUN pip3 install flask

EXPOSE 5000
CMD ["python3", "/app/main.py"]