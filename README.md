# Penguins Dashboard - Final Project (Module 7 - P7) by Blessing
An interactive dashboard built using PyShiny and the Palmer Penguins dataset. This final version includes filtering by species and body mass, summary statistics, scatter plots, and an interactive data grid.


## Tools

- Python
- Shiny for Python
- VS Code + Python Extension
- Git
- GitHub


## Try the Live Dashboard

You can view the live app here:  
[My Penguins Dashboard](https://teflxndxn.github.io/cintel-07-tdash/)


## Based on the original project by Denise Case:  
<https://github.com/denisecase/pyshiny-penguins-dashboard-express>

## Get the Code

```shell
 git clone https://github.com/teflxndxn/cintel-07-tdash
```

## Run Locally - Initial Start

After cloning your project down to your Documents folder, open the project folder for editing in VS Code.

Create a local project virtual environment named .venv, activate it, and install the requirements.

When VS Code asks to use it for the workspace, select Yes.
If you miss the window, after installing, select from the VS Code menu, View / Command Palette, and type "Python: Select Interpreter" and select the .venv folder.

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands (for Windows - the activate command is slightly different Linux/Mac).

```shell
py -m venv .venv
.venv\Scripts\Activate
py -m pip install --upgrade pip setuptools
py -m pip install --upgrade -r requirements.txt
```

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands.

```shell
shiny run --reload --launch-browser app/app.py
```

Open a browser to <http://localhost:8008/> and test the Pages app.


## Run Locally - Subsequent Starts

Open a terminal (VS Code menu "View" / "Terminal") in the root project folder and run these commands.

```shell
.venv\Scripts\Activate
shiny run --reload --launch-browser app/app.py
```

While the app is running, the terminal is fully engaged and cannot be used for other commands. 
To kill the terminal, click the trashcan icon in the VS Code terminal window. 

## After Changes, Export to Docs Folder

Export to docs folder and test GitHub Pages locally.

Open a new terminal (VS Code menu "Terminal" / "New Terminal") in the root project folder and run these commands. 
Remember to activate the environment first. 

```shell
.venv\Scripts\Activate
shiny static-assets remove
shinylive export app docs
py -m http.server --directory docs --bind localhost 8008
```

Open a browser to <http://[::1]:8008/> and test the Pages app.

## Push Changes back to GitHub


Open a terminal (VS Code menu "Terminal" / "New Terminal") in the root project folder and run these commands.

```shell
git add .
git commit -m "Final P7 dashboard improvements and README update"
git push -u origin main

```

## Features and Improvements in This Version

- Filter penguins by species and body mass.
- Summary value boxes with average bill length/depth and count.
- Scatter plot of bill length vs bill depth by species.
- Interactive data grid with filters.
- Added links to project repo, live app, and related resources.