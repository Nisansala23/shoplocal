# Stage 1: Builder
FROM python:3.13-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Runner
FROM python:3.13-slim AS runner

WORKDIR /app

# Copy installed dependencies from the builder stage
COPY --from=builder /install /usr/local

# Copy application files
COPY app.py .
COPY templates/ templates/

# Security best practice: Run as a non-root user
RUN useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 5000

CMD ["python", "app.py"]
