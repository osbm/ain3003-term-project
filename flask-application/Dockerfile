FROM python:3.11.6

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

# Set the default value for MONGO_URI if not provided
ENV MONGO_URI="mongodb://localhost:27017"


CMD ["python", "app.py"]