# Python tricks

## Virtual environments

### Poetry cheatsheet

# to create poetry project

cd app-folder
poetry init


# to install dependencies
poetry add package 
or: 
cat requirements.txt | xargs poetry add 

# create venv
poetry install

# misc
poetry show
poetry env list
poetry env info
poetry env info --path

# activate venv
poetry shell

# to deactivate
exit
