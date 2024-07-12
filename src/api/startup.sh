#!/bin/bash
# startup.sh

echo "Current directory: $(pwd)"
echo "Files in venv/bin:"
ls -al /home/site/wwwroot/venv/bin/

source /home/site/wwwroot/venv/bin/activate

# echo "Setting PATH..."
# export PATH="/home/site/wwwroot/venv/bin:$PATH"

echo "Which Python: $(which python)"
echo "Which Gunicorn: $(which gunicorn)"

exec gunicorn -c gunicorn.conf.py app:app
