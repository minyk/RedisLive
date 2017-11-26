FROM alpine
RUN apk add --no-cache --update py-pip
RUN mkdir -p /redislive
COPY . /redislive
RUN cd /redislive \
    && pip install -r requirements.txt

WORKDIR /redislive/src
RUN mv redis-live.conf.example redis-live.conf

EXPOSE 58888

# Configure container to run as an executable
#CMD ["./redis-monitor.py", "--duration=120", "--quiet"]

ENTRYPOINT ["./regular-check.py"]
