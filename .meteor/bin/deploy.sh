# Assume meteor is installed, otherwise run `curl https://install.meteor.com/ | sh`

# Cleanup

rm -rf .meteor/local/*

# Build project
npm install
meteor build --directory .meteor/local --server-only --server http://faceit.tonny.me

cd .meteor/local/bundle/programs/server
npm install

cd ../../
node main.js
