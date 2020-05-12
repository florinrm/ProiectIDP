FROM python:3.6
COPY /src_server /app
RUN pip install pika
RUN pip install flask
RUN pip install mysql-connector-python
RUN pip install jsonify
WORKDIR /app
EXPOSE 80
CMD ["python", "server.py"]
