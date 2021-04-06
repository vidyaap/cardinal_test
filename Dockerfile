FROM python:3.7

RUN mkdir /cardinal_test
WORKDIR /cardinal_test
ADD . /cardinal_test/
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "/cardinal_test/hello-depl.py"]