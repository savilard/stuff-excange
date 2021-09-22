<h3 align="center">Stuff exchange</h3>

<p align="center">
  <a href="https://github.com/wemake-services/wemake-python-styleguide"><img src="https://img.shields.io/badge/style-wemake-blue?style=for-the-badge" alt="Code style"></a>
  <img alt="Platform" src="https://img.shields.io/badge/platform-linux-green?style=for-the-badge" />
  <img alt="Python version" src="https://img.shields.io/badge/python-3.9-green?style=for-the-badge" />
</p>

## Table of content

- [About the project](#about-the-project)
- [Installation](#installation)
- [How to run](#how-to-run)


## About the project

A person has a thing that has not lost its useful properties (not broken) or has lost it, but it can be used in another way.
The person does not need it for some reason, and does not want to sell it, but wants to give it to someone else.
But, not for nothing, but to get something he needs in return. This project will help organize the exchange of things.


## Installation

* Install [Poetry](https://python-poetry.org/) and make;
* Clone github repository:
```bash
git clone https://github.com/savilard/stuff-excange
```
* Go to folder with project:
```bash
cd stuff-excange
```
* Install dependencies:
```bash
make install
```
* Create a .env file with the following content:
```.env
SECRET_KEY='django secret key'
DEBUG=True to dev server
```
*Create a SQLite database file and migrate it with the following command:
```bash
python manage.py migrate
```

## How to run

Start the server:
```bash
python app/manage.py runserver
```

Open the site in your browser at http://127.0.0.1:8000/.
