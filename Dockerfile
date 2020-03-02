FROM python:3.8
LABEL maintainer="zhou xy"
COPY . /app/
WORKDIR /app
RUN pip install -r requirments.txt
EXPOSE 5000
CMD python app.py