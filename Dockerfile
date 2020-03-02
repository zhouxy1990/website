FROM python:3.8
LABEL maintainer="zhou xy"
RUN pip install -f requirments.txt
COPY . /app/
WORKDIR /app
EXPOSE 5000
CMD python app.py