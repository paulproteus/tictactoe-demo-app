#!/bin/bash
env/bin/flake8 tttproject --exclude=tttproject/manage.py,tttproject/tttproject/settings.py
source env/bin/python
cd tttproject ; python manage.py test tttapp
