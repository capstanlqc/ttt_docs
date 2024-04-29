## How to build the Okapi filter plugin

Three steps are required to create a new okapi plugin:

- build okapi framework
- build the okapi plugin
- deploy the okapi plugin build

### 1. Getting the Okapi repo code and making a build

Go to the dedicated folder where you'll do the building work:
```
cd ~/Repos/okapiframework
```

To get a fresh fresh copy, clone the Okapi general repository:

```
git clone https://bitbucket.org/okapiframework/okapi.git
``` 

Change directory to local clone and check out the `dev` branch:
```
cd okapi
git checkout dev
```

Optionally, to get updates: 
```
git pull origin dev
```

Build the Okapi framework from the `dev` branch:
```
mvn clean install --update-snapshots -DskipTests
```
Note: `-DskipTests` option just skips unit tests.


### 2. Getting the Okapi OmegaT Plugin repo code and making a build

Go to the dedicated folder where you'll do the building work:
```
cd ~/Repos/okapiframework
```

To get a fresh clone:
```
git clone https://bitbucket.org/okapiframework/omegat-plugin.git
```

Change directory to the filters folder and checkout the `dev` branch:
```
cd omegat-plugin/filters
git checkout dev
``` 

Optionally, to get updates: 
```
git pull origin dev
```

Make a build:
```
mvn clean package
```

### 3. Deploying the Okapi OmegaT Plugin build

Navigate to the OmegaT Plugin folder first if you're not there yet:
```
cd ~/Repos/okapiframework/omegat-plugin/filters
```
Nove the JAR file to your OmegaT user configuration folder (e.g. by default `~/.omegat` on Linux or `%APPDATA%\OmegaT` on Windows):

```
cp target/okapiFiltersForOmegaT-1.12-1.44.0-SNAPSHOT.jar YOUR_OMEGAT/plugins
```