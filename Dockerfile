FROM python:3.10
RUN apt-get update && apt-get install -y bash
WORKDIR /appr
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN curl --proto '=https' --tlsv1.2 -sSf https://just.systems/install.sh | bash -s -- --to /usr/local/bin
COPY . .
ENV PYTHONPATH="${PYTHONPATH}:/app"
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]