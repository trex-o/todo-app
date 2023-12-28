FROM python:3.12.1-alpine3.19
RUN mkdir -p /home/app
COPY ./app /home/app
WORKDIR /home/app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD python app.py
