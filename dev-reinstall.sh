#!/bin/bash
python setup.py clean --all && \
pip uninstall -y django-simple-third-party-jwt-dev-dashboard && \
python setup.py sdist && \
python -m pip install ./dist/django-simple-third-party-jwt-dev-dashboard-0.0.1.tar.gz
