#!/usr/bin/python3
"""script that generates a tgz archive"""
from fabric.api import *
from datetime import datetime


def do_pack():
    """function that generates tgz archive"""
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("mkdir -p versions")
        local('tar -cvzf {} web_static'.format(file_name))
        return file_name
    except Exception as e:
        return None
