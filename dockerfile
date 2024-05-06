FROM python:latest
WORKDIR /app
COPY requirments.txt /app
COPY .  /app
RUN pip install --no-cache-dir -r requirments.txt
CMD ["python", "main.py"]

