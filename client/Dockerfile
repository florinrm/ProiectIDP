FROM python:3.6
RUN pip install requests
RUN pip install jsonify
RUN pip install flask
RUN pip install flask-socketio
COPY /src_client /app
WORKDIR /app
EXPOSE 80
CMD ["python", "client.py"]
