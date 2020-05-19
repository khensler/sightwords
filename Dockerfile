FROM python:3.7
RUN apt install git
RUN git clone https://github.com/khensler/sightwords
RUN pip install --no-cache-dir -r requirements
ENTRYPOINT ["python"]
CMD ['main.py']