# Faceit

This is a project at SB Cloud Hackathon (late 2016).

## Run

```sh
# Assuming meteor is already installed
$ meteor
```

## Dev

Deploy:

1. At your local, run
sh .meteor/bin/deploy.sh

2. At your remote run
cd /www/faceit/programs/server
npm install
cd ../../

3. forever is not started
MONGO_URL=$MONGO_URL ROOT_URL=$ROOT_URL PORT=$PORT forever start main.js

4. If forever started

MONGO_URL=$MONGO_URL ROOT_URL=$ROOT_URL PORT=$PORT forever restart 0
