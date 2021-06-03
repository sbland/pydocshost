# pydocshost

The frontend gui is created with Python Flask and Javascript React.
Flask creates the backend server with endpoints that allow making html calls to the python model.

The python flask model acts as an interface that is agnostic of the model being plugged in as long as it meets the interface requirements.

# Dependencies

## Backend

The backend requires python to be installed. It is recommended that you also use a python virtual environment.

## Frontend

The frontend requires node.js and yarn to be installed.

# Running Backend

`pip install -r requirements/common.txt`
`python app.py <model_import_strin>`

# Running the frontend

`cd client`
`yarn install`
`yarn start`
then go to `localhost:3000`

# Connecting to endpoints

Each endpoint is defined in `run_app.py`
