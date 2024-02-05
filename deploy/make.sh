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
    echo No .env file found. Do you want to setup the environment variables? \(y/n\)
    read startSetup
    if [$startSetup == y]; then
        echo Please enter the Notion integration token: 
        read integrationToken
        echo Please enter the database id: 
        read databaseId
        echo NOTION_TOKEN=$integrationToken >> .env
        echo NOTION_DATABASE_ID=$databaseId >> .env
    fi
fi