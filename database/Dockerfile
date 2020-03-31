FROM alpine:edge

RUN echo "**** install Python ****" && \
    apk add --no-cache python3 && \
    if [ ! -e /usr/bin/python ]; then ln -sf python3 /usr/bin/python ; fi && \
    \
    echo "**** install pip ****" && \
    python3 -m ensurepip && \
    rm -r /usr/lib/python*/ensurepip && \
    pip3 install --no-cache --upgrade pip setuptools wheel && \
    if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi

COPY requirements.txt /usr/src/database/
RUN pip install --no-cache-dir -r /usr/src/database/requirements.txt

COPY database.py /usr/src/database/
COPY templates/index.html /usr/src/database/templates/
COPY static/stylesheets/style.css /usr/src/database/static/stylesheets/

EXPOSE 5000

CMD ["python3", "/usr/src/database/database.py"]