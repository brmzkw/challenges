FROM python:3

RUN pip install poetry

ENV FLASK_APP=challenge
ENV FLASK_DEBUG=1

COPY docker-entrypoint.sh /
ENTRYPOINT ["/docker-entrypoint.sh"]

CMD ["poetry", "run", "flask", "run", "--host", "0.0.0.0"]
