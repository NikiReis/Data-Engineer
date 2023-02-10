#!/bin/bash

# Script to remove PostgreSQL from Ubuntu operating system
sudo apt remove postgresql postgresql-contrib

#Unistalling Dependencies Packages
sudo apt autoremove

# Listing Postgres Packages
dpkg -l |grep postgres

# Remove Postgres from your system by running the remove purge command
sudo apt-get --purge remove postgresql postgresql-15 postgresql-client-common postgresql-common posgresql-contrib


# Listing Postgres Packages again, to see if the unintalling was done correctly
dpkg -l |grep postgres
