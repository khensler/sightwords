# sightwords

This repository hosts a python app to help learn sight words.  
It initialize the word DB edit loadwords.py to include the words you need to learn/teach
Run loadwords.py as a regular python script

Then run main.py as a flask app.  Access the app via a browser.

The app will select 5 known and 5 unknown words on each request and then select a random word of those 10
By pressing correct and incorrect the app will record the attempt in the DB to help with later word selection.


You can also run this in a docker image.  Download the Dockerfile and run docker build -t sightwords.  It will build the container with the latest from git and then run it with docker run -d -p 5000:5000 sightwords