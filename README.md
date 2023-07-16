# Docker-Flask-Postgresql Project

This is a simple demo for how to containerize to a Flask app with Postgresql database. To run this on your computer you must first install [docker](https://docs.docker.com/engine/installation/).

## Running

First fork the repo then do a `git clone`.

    git clone https://github.com/<yournamehere>/container-project

You should also have [docker](https://docs.docker.com/install/). If you're on linux, you probably also want docker-compose. For Mac and Windows you get it with the default installation.

Once you have all of that, you should be good. No need to install [Postgres](https://www.postgresql.org/) or even Python.

```
docker-compose up --build -d   # Run the container.

docker-compose down   # Stop and remove everything.

The site will be available to you at `localhost:5000`.

To make the scripts executable (dont forget to change the path)

```shell
chmod +x /path/to/backup.sh
```
```shell
chmod +x /path/to/restore.sh
```
Then you can execute the scripts.

To schedule the backup, edit the crontab :
```shell
crontab -e
```
Add the following line to run the backup script daily at midnight:
```shell
0 0 * * * /path/to/backup.sh
```
