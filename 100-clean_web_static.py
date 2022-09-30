#!/usr/bin/python3
"""script that deploy archive!"""
from fabric.api import *
from datetime import datetime
env.hosts = ['3.236.80.232', '44.200.150.121']
env.user = 'ubuntu'


@runs_once
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


def do_deploy(archive_path):
    """function that distributes an archive to your web servers"""
    try:
        filename = archive_path.split("/")[-1]
        onlyname = filename.split(".")[0]
        uncompress_path = "/data/web_static/releases/{}".format(onlyname)
        put(archive_path, '/tmp/')
        run('sudo mkdir -p {}/'.format(uncompress_path))
        run('sudo tar -xzf /tmp/{} -C {}'.format(filename, uncompress_path))
        run('sudo rm /tmp/{}'.format(filename))
        run('sudo mv {0}/web_static/* {0}/'.format(uncompress_path))
        run('sudo rm -rf {}/web_static'.format(uncompress_path))
        run('sudo rm -rf /data/web_static/current')
        run('sudo ln -s {}/ /data/web_static/current'.format(uncompress_path))
        print('New version deployed!')
        return True
    except BaseException:
        print('Do it again')
        return False


def deploy():
    """creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        print('Something happen')
        return False
    print('New tar created...starting deployment in 3,2,1....!')
    return do_deploy(archive_path)


def do_clean(number=0):
    """script that deletes out-of-date archives"""
    number = int(number)

    if number < 0:
        return None
    number = 2 if (number == 0 or number == 1) else (number + 1)
    with lcd("./versions"):
        local('rm -rf $(ls -t | tail -n +{:d})'.format(number))
    with cd("/data/web_static/releases"):
        run('rm -rf $(ls -t | tail -n +{:d})'.format(number))