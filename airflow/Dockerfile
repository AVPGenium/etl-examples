FROM apache/airflow:2.2.3

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --user -r /requirements.txt
RUN pip uninstall -y dataclasses

#RUN  sleep 10 && pip install --user -r /requirements.txt