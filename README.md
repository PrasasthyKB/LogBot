# PWP SPRING 2023
# PROJECT NAME
# Group information
* Student 1. Justin Seby, justin.seby@student.oulu.fi
* Student 2. Talha Zeeshan, talha.zeeshan@student.oulu.fi
* Student 3. Kazi_Haque, kazi.haque@student.oulu.fi
* Student 4. Prasasthy Balasubramanian, prasasthy.balasubramanian@oulu.fi

## Tools Used

* MongoDB
* py-mongo
* Flask-MongoEngine
* BCrypt
* Flask JWT Extended

### NOTE: All of the following commands are based on running the application in a Linux Distribution (Ubunttu)

## Download MongoDB 
MongoDb can be downloaded from the official website for your relevant OS (Windows/mac/linux). Follow the instructions provided on the webpage for setting up mongodb on your local machine. Once installed, install py-mongo to be able to interact with mongoDB via a pythong script.
We recommend setting up a virtual environment so to ensure you have a self contained environment which will not affect your locally installed python packages

## Environment Setup

Setup a virtual environment

`python3 -m venv /path/to/venv/file`

Activate your virtual environment

`source activate /path/to/venv/file/bin/activate`

Install the dependecies using the requirements.txt file from the root directory

`pip install -r requirements.txt`

## Start MongoDB
Install and start a Mongodb instance in your virtual machine

`sudo apt-get update`

`sudo apt install mongodb`

`sudo systemctl start mongodb`


To check the status and stop Mongodb instance

`sudo systemctl status mongodb`

`sudo systemctl stop mongodb`


## Run the Flask Server
Switch to the logbot directory and run the following command to start the Flask Server API
```bash
    cd logbot
    python app.py
```

