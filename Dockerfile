FROM python:3.11-slim-bullseye
WORKDIR /scrt-tw-workspace
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "example.py" ]
