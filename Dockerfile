FROM python:3
MAINTAINER Infoglobo
ENV PORT=5000
COPY . /opt/feed-api
WORKDIR /opt/feed-api
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
EXPOSE $PORT
