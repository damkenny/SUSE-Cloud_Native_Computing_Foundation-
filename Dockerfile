FROM  python: 3.9.1
LABEL maintainer="Kehinde"
COPY . /app
WORKDIR /app
RUN pip install -r requirement.txt
CMD ["python", "app.py"]
