FROM tiangolo/uvicorn-gunicorn-fastapi:latest
RUN pip3 install dotenv pymongo pymongo[srv]
COPY ./app /app/app