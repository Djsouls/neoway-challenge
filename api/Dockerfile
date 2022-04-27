FROM python:3.9

WORKDIR app/

COPY . .

RUN pip install -r requirements.txt

ENV FLASK_ENV development

# ENTRYPOINT ["python"]

CMD ["python", "app/main.py"]
