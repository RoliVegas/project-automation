#!/bin/bash

echo ---- BASH SCRIPT STARTED ----
echo Enter project name:
read PROJECT_NAME

cd /Users/roland/Desktop/Coding
mkdir $PROJECT_NAME
cd $PROJECT_NAME
touch README.md

cd /Users/roland/Desktop/Coding/tools/scripts
echo ---- CALLING PYTHON SCRIPT ----
python3 create-git-repo.py $PROJECT_NAME

echo ---- CONTINUING BASH SCRIPT ----
cd /Users/roland/Desktop/Coding/$PROJECT_NAME
git init
git remote add origin git@github.com:RoliVegas/$PROJECT_NAME.git
git add .
git commit -m "Initial commit."
git branch -M main
git push -u origin main
code .

echo ---- BASH SCRIPT FINISHED ----