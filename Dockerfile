FROM python:3.7-slim
WORKDIR lab1
ADD converter.py .
ENTRYPOINT ["python3", "./converter.py"]