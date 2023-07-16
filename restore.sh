#!/bin/bash

# Configuration
CONTAINER_NAME="container-project-db-1"  # Update this with the service name in your Docker Compose file
DATABASE_USER="myuser"

# Restore
read -p "Enter the name of the backup file to restore (including path if necessary): " restore_file
if [[ -f $restore_file ]]; then
    docker exec -i $CONTAINER_NAME psql -U $DATABASE_USER -d postgres < "$restore_file"
    echo "Database restored from backup"
else
    echo "Backup file not found!"
fi