FROM postgres:13
ENV POSTGRES_USER=user
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=api_monitor
COPY seed_data.py /docker-entrypoint-initdb.d/
