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

COPY requirements.txt /usr/src/client/
RUN pip install --no-cache-dir -r /usr/src/client/requirements.txt

COPY client.py /usr/src/client/
COPY templates/index.html /usr/src/client/templates/

EXPOSE 5000

CMD ["py", "/usr/src/client/client.py"]