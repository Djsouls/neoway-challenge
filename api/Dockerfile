FROM python:3.9 as base

WORKDIR app/

COPY . .

RUN pip install -r requirements.txt


FROM base as tests

RUN ["pytest", "-v"]

FROM base as development

ENV FLASK_ENV development

CMD ["python", "-m", "neoway"]