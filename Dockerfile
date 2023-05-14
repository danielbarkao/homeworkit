FROM python:3.9
COPY myip.py /app/
WORKDIR /app
RUN pip install flask
CMD ["python", "myip.py"]