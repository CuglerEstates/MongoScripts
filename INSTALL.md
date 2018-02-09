# Installation guide

#### 1) Clone this repo to your home directory.
```
git clone git@github.com:alan-cugler/MongoScripts.git
```

#### 2) Run mongoInstall.sh to install both MongoDB and python3 virtualenv
```
sudo bash MongoScripts/MongoScripts/setup.sh
```

#### 3) Now we create virtualenv directory and activate the environment. 
```
python3 -m venv ~/venv
source ~/venv/bin/activate
```

#### 4) Install requirements.txt file with pip
```
pip install -r MongoScripts/MongoSripts/requirements.txt
```

#### 5) Modify and run the .py scripts available for your project needs!
```
python <file>.py
```
