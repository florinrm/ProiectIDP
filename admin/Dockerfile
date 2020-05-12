FROM python:3.6
COPY /src_admin /app
RUN pip install requests
RUN pip install pika
WORKDIR /app
EXPOSE 80
CMD ["python", "admin.py"]
