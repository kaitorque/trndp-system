# trndp-system
TRNDP System for FYP


## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)
* [Status](#status)

## General info
Evaluation system to solve TRNDP

## Technology
Project is create with:

* Windows 10 Operating System
* Python 3.7+
* Mysql 8.0+

## Setup
How to setup locally(Windows)

- Download Python 3.7 from 
https://www.python.org/downloads/

- Install Python 3.7
- Then set a python path to system enviroment if it not set by the installer
- Check if python is working when run command in cmd below:
```
python --version
```
- Then check whether pip is install using cmd below: 
```
pip --version
```
- Then Download Mysql from
https://dev.mysql.com/downloads/mysql/8.0.html

- Run the installer
- Tick Server, Connection and Workbench
- Workbench are optional but it is easier to add database and manage instead of using cmd
- check mysql in using command
```
mysql --version
```
- Open up Mysql Workbench select data import on the right side of menu.
- Choose Import from Self-Contained File
- Browse trndp.sql file in DB folder
- Click new schema button and name the schema trndp
- Then start the import
```
- Now everything is ready, you can now serve the system through
- Open up cmd in trndp_project folder where manage.py exist
- then run command below
```
python manage.py runserver
```
- Now the website is run on localhost for port 8000


## Status
Currently project has a few bug in it, other network model are not working except Mandl network. If the main page or list TRNDP page has error when it is loading, then try truncating table network in database by right click and truncate table

## Inspiration
Thank you to the supervisor, lecturer & friends