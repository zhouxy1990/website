FROM python:2.7
LABEL maintainer="zhou xy"
RUN pip install -f requirments.txt
COPY . /app/
WORKDIR /app
EXPOSE 5000
CMD python app.py