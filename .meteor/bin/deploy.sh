# Assume meteor is installed, otherwise run `curl https://install.meteor.com/ | sh`

# Cleanup

rm -rf .meteor/local/*
ssh root@47.91.16.100 rm -rf /www/faceit/*

# Build project
npm install
meteor build --directory .meteor/local --server-only --server http://faceit.tonny.me

scp -r .meteor/local/bundle/* root@47.91.16.100:/www/faceit
