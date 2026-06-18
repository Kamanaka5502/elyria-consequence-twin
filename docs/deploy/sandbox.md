# Sandbox Demo

## Local Python

```bash
make install
make api
```

Open:

```text
http://localhost:8080
```

Reset demo data:

```bash
curl -X POST http://localhost:8080/sandbox/reset
```

Load the exposure graph:

```bash
curl http://localhost:8080/exposures/demo
```

## Docker

```bash
docker compose up --build
```

Open:

```text
http://localhost:8080
```

## Demo Endpoints

```text
GET  /healthz
GET  /exposures/demo
POST /sandbox/reset
POST /movements/assess
GET  /receipts
GET  /receipts/{receipt_id}
POST /receipts/{receipt_id}/replay
```
