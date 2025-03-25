up:
    docker-compose up -d --build

down:
    docker compose down -v

test:
    pytest tests -v

lint:
    black --check app
    flake8 app/
    isort --check app
    mypy app/

fix:
    black app/
    isort app/