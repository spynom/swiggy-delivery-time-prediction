FROM python:3.12-bookworm

WORKDIR /app
COPY fastapi_app/ /app/


# install lightgbm dependency
RUN apt-get update && apt-get install -y libgomp1



RUN pip install -r app_requirements.txt

EXPOSE 8000

CMD ["python3.12", "app.py"]
