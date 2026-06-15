FROM python:3.12-slim
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

WORKDIR /code
ENV PATH="/code/.venv/bin:$PATH"
COPY pyproject.toml .python-version uv.lock ./
RUN uv sync --locked

COPY data_producer.py .
COPY airlines_flights_data.csv .

ENTRYPOINT ["python", "data_producer.py"]