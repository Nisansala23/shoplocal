# Stage 1: Builder
FROM python:3.11-slim AS builder

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --prefix=/install -r requirements.txt

# Stage 2: Runner
FROM python:3.11-slim AS runner

WORKDIR /app

# Copy dependencies from builder stage
COPY --from=builder /install /usr/local

# Copy application code
COPY app.py .

# Setup non-root user for security
RUN useradd -m appuser && chown -R appuser /app
USER appuser

EXPOSE 5001

CMD ["python", "app.py"]
