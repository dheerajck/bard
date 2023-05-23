# To get started, follow the steps below

## I - Create a new Python virtual environment
```
python -m venv venv
```

## II - Activate the virtual environment and install the project requirements
```
source venv/bin/activate
pip install -r requirements.txt
```

## III - Create a new .env file on the root directory based on .env.example and update the variables in the .env file
```
cp .env.example .env
```
Login to bard from your browser, add SELECTED_BROWSER to your env file with value(chrome, firefox, edge, brave, safari) based on the browser you are using.<br>
You can follow the instructions in https://github.com/acheong08/Bard/tree/main to manually extract BARD_SESSION from the browser and add it to env file, if BARD_SESSION is present in env file, SELECTED_BROWSER will be ignored.

## IV - Now run main.py
```
python main.py
```

