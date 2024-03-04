git clone https://bitbucket.org/okapiframework/okapi.git
cd okapi
git checkout dev

(optional: to get update)
git pull origin dev



Note: making a build

$ mvn clean install --update-snapshots -DskipTests



---

plugin

cd  ~/Repos/okapiframework/omegat-plugin
cd filters
mvn clean package
---




git clone https://bitbucket.org/okapiframework/omegat-plugin.git
cd omegat-plugin
git checkout dev
git pull origin dev
cd filters
mvn clean package



-----

poetry cheatsheet: 

# poetry

# create venv
poetry install

poetry show
poetry env list
poetry env info
poetry env info --path

# activate venv
poetry shell


# cd app-folder # (to create poetry project)
# poetry init
# poetry add package # or: cat requirements.txt | xargs poetry add 
# poetry install # to install dependencies
# poetry shell # to activate
# exit # to deactivate