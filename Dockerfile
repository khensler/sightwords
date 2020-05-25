FROM python
RUN mkdir /App
WORKDIR /App
RUN git clone https://github.com/khensler/sightwords
WORKDIR /App/sightwords
RUN pip install --no-cache-dir -r requirements.txt
ENTRYPOINT ["gunicorn"]
CMD ["-w 4","'app:create_app()'"]