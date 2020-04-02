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

COPY requirements.txt /usr/src/admin-server-frontend/
RUN pip install --no-cache-dir -r /usr/src/admin-server-frontend/requirements.txt

COPY admin-server-frontend.py /usr/src/admin-server-frontend/
COPY templates/index.html /usr/src/admin-server-frontend/templates/
COPY templates/page.html /usr/src/admin-server-frontend/templates/
COPY static/stylesheets/style.css /usr/src/admin-server-frontend/static/stylesheets/

EXPOSE 5001

CMD ["python3", "/usr/src/admin-server-frontend/admin-server-frontend.py"]