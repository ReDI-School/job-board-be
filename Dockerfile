FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7
WORKDIR /app
COPY requirements.txt .
RUN pip --no-cache-dir install -r requirements.txt
COPY . .
CMD python ./src/jobs_api.py
