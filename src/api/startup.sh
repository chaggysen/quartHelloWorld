#!/bin/bash
# startup.sh

echo "Current directory: $(pwd)"
echo "Files in venv/bin:"
ls -al /home/site/wwwroot/venv/bin/

source /home/site/wwwroot/venv/bin/activate

echo "Which Python: $(which python)"
echo "Which Gunicorn: $(which gunicorn)"
echo "Python Path: $(python -c 'import sys; print(sys.path)')"

exec /home/site/wwwroot/venv/bin/gunicorn -c gunicorn.conf.py app:app
