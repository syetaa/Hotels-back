# Docker
## Development mode (fast-refresh)
```bash
docker compose watch
```

## Production mode
```bash
docker compose up --build -d
```
 
# Default
## Development mode (fast-refresh)
```bash
uvicorn main:app --reload
```

## Production mode
```bash
uvicorn main:app
```
