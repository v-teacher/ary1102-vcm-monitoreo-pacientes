FROM python:3.12-slim
WORKDIR /workspace
RUN useradd --uid 10001 --create-home student && mkdir /data && chown student /data
COPY app ./app
USER 10001
ENV HOST=0.0.0.0 PORT=8080 DB_PATH=/data/events.sqlite3 PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
EXPOSE 8080
CMD ["python", "-m", "app.server"]
