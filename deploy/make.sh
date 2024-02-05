#!/bin/bash
set -e

### Configuration ###

GIT_URL=https://github.com/kuzniarz/notion-recipe-scraper

### Pull new changes from https://github.com/kuzniarz/notion-recipe-scraper

echo Updating project version...
cd ..
git pull

echo Installing python dependencies...
# Install dependencies
if [ ! -f "./bin" ]; then
    python3 -m venv .
    source ./bin/activate
fi
./bin/python -m pip install -r requirements.txt

#Create environment file
echo Checking for environment variables...
if [ ! -f ".env" ]; then
    read -p "No .env file found. Do you want to setup the environment variables? (Y/N): " -n 1 -r
    if [[ $REPLY =~ ^[Yy]$ ]]
    then
        read -p "Enter Notion integration token: " token
        read -p "Enter database ID (32-digits): " databaseID
        echo NOTION_TOKEN=$token >> .env
        echo NOTION_DATABASE_ID=$databaseID >> .env
    fi
fi