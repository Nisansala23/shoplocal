# ShopLocal — Microservices Shopping App

A simple 2-service shopping app built for learning DevOps.

## Services

| Service  | Port | What it does              |
|----------|------|---------------------------|
| products | 5001 | Returns product list JSON |
| frontend | 5000 | Shows the shopping UI     |

## Project structure

```
shoplocal/
├── docker-compose.yml
├── frontend/
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── templates/
│       └── index.html
└── products/
    ├── app.py
    ├── requirements.txt
    └── Dockerfile
```

## Run with Docker Compose (easiest)

```bash
docker-compose up --build
```

Then open http://localhost:5000

## Run without Docker (for development)

Terminal 1 — start products service:
```bash
cd products
pip install -r requirements.txt
python app.py
```

Terminal 2 — start frontend:
```bash
cd frontend
pip install -r requirements.txt
python app.py
```

## API endpoints

Products service:
- GET http://localhost:5001/health
- GET http://localhost:5001/products
- GET http://localhost:5001/products/1

Frontend:
- GET http://localhost:5000
- GET http://localhost:5000/health

## Next steps (DevOps)

1. Dockerize — already done above
2. Push images to GitHub Container Registry (GHCR)
3. Deploy to Kubernetes with Minikube
4. Set up ArgoCD for GitOps
5. Add Prometheus + Grafana monitoring
