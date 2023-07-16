#!/bin/bash

DATE=$(date +%Y%m%d)
CONTAINER_NAME="db"  # Update this with the service name in your Docker Compose file
DATABASE_USER="postgres"
BACKUP_FILE="backup_$DATE.sql"

# Perform database backup inside the container
docker exec $CONTAINER_NAME pg_dumpall -U $DATABASE_USER > "$BACKUP_FILE"

# Copy the backup file to the current folder
docker cp $CONTAINER_NAME:"$BACKUP_FILE" "$(pwd)/$BACKUP_FILE"
