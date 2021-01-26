FROM python:3.93

COPY . /app
WORKDIR . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]
