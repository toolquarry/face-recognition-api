# Face Recognation API

Face Recognation API

## Setup

```sh
git clone https://github.com/toolquarry/face-recognition-api

pip install virtualenv

cd face-recognition-api

virtualenv venv
```

## Run

### On MacOs or Linux:

```sh
cd face-recognition-api

source venv/bin/activate

pip install

python -m flask run

deactivate
```

### On Windows:

```sh
cd face-recognition-api

venv\Scripts\activate

pip install

python -m flask run

deactivate
```

## Test

Once the app is running, we can test it with [curl](https://curl.se/):

```

curl -X POST -F "image=@/dev/pictures/1/0.png" http://127.0.0.1:5000/face-recognition/num-faces

```

## Notes

[Issue with MacOS M1 Apple Silicon and Python 3.9](https://github.com/davisking/dlib/issues/2268#issuecomment-920464038)
