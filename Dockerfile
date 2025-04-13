FROM python:3.11-slim

WORKDIR /app

COPY import_flow.py /app/
RUN pip install requests

CMD ["python", "import_flow.py"]
