# Pokética
## Coffee Scriptors :coffee: - Claire Liu, Sophia Xia, Emily Lee, Stefan Tan 
## Roles:
Claire Liu - Project Manager & Frontend/HTML
<br>
Sophia Xia - Database & HTML & App  
<br>
Emily Lee - Database & Gacha
<br>
Stefan Tan - Backend/ API & Database

## Overview:
TL;DR: RPG To-Do List!
Pokética is a web-based application based off of the application Habitica. Pokética allows the user to add and remove tasks to and from their own personalized to-do list. Whenever the user completes a task on their to-do list, they would gain gold which they could later use to buy more pokémons. Pokética is made for everyone, especially those who procrastinate all the time, as it provides an incentive and helps us all release our inner Ash Ketchum. **Gotta Catch 'Em All!**

## [our video demo here](www.youtube.com):

## Instructions to Run: 
1. Open a terminal session.
2. Create your own environment by typing (name is a placeholder for the name of the virtual environment of your choosing):
```
$ python3 -m venv name
```
3. Activate the virtual environment by typing ```$ . name/bin/activate``` in the terminal and make sure it is running python3 by typing ```(venv)$ python --version``` in the terminal.
4. Clone this repository. If you have already cloned this repository, skip this step. To clone this repo, open a terminal session and navigate to the directory you want for this repository to located in. Then clone using SSH by typing ```(venv)$ git git@github.com:cliu5/CoffeeScriptors.git``` or clone using HTTPS by typing ```(venv)$ git clone https://github.com/cliu5/CoffeeScriptors.git``` in the terminal.
5. Navigate to our repository by typing ```$ cd CoffeeScriptors/``` in the terminal.
6. Make sure you have all the dependencies installed in your virtual environment. To check, look at the [Dependencies section](https://github.com/cliu5/CoffeeScriptors#dependencies) below.
7. No API keys are needed for our application. To learn more about the API we used click [here](https://github.com/cliu5/CoffeeScriptors#api).
8. Run the python file by typing ```(venv)$ python app.py``` in the terminal.
9. This should appear in the terminal after running the python file.   
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 248-748-502
```

10. Open a web browser and navigate to the link http://127.0.0.1:5000/.
11. Follow the prompts of our application and enjoy!

## Dependencies/Necessary Packages:
* Flask==1.0.2

   Used as the framework for the app.
* Jinja2==2.10

   Template engine for Python.
* passlib==1.7.1

   Hashes password to increase security of our application.
1. Install the dependencies listed above by typing ```(venv)$pip install -r <path-to-file>requirements.txt``` in your terminal.

## API:
* Pokémon TCG API

  Used to retrieve information on pokémon cards. No API key is required to use this API. To learn more about this API go [here](https://pokemontcg.io/).
