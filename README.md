# KilimoSauti_Backend
# KILIMO SAUTI

 Kilimo sauti is mobile based and AI enhanced system that enhance the crop management awareness through easy interpretation of the voice recorded by the farmer in Kiswahili

## Table of Contents
* Features,
* Technologies Used,
* Setup.


## FEATURES

* Account App: Manages user accounts, authentication(OTP), and profile information.
  

## TECHNOLOGIES USED

* Python: The core programming language used for backend development.
* Django: The web framework that powers this project.

## SETUP

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/hassanyange/KilimoSauti_Backend.git
$ cd KilimoSauti_Backend
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ virtualenv2 --no-site-packages env
$ source env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `virtualenv2`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ python manage.py runserver
```
The KilimoSauti system should now be accessible at * N.B: This project is for Backend side
```sh
http://localhost:8000
```
## Author
Hassan Yange  <hassanyange@gmail.com>


