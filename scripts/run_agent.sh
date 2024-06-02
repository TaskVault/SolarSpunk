#!/bin/bash

cd ../python

# Fetch the agent from the local packages directory
aea fetch zarathustra/solar_punk --local

# Navigate to the project directory
cd solar_punk

# Install agent dependencies
aea install

# Create a key for the agent
aea generate-key ethereum && aea add-key ethereum

# Issue certificates for the Libp2p connection
aea issue-certificates

# and run the agent
aea run
