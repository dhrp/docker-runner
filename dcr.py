#!/usr/bin/env python

__author__ = 'thatcher'
import sys
from docker_container_runner import utils
from docker_container_runner.manager import Application, DockerDaemon, Hipache


settings = utils.read_settings('settings.yml')



def initialize():
    """
    start it
    """

    directives = utils.read_appconfig(sys.argv[2])

    name, config = directives.items()[0]
    release_name = config['release_name']

    # Create the application
    application = Application(release_name, config, settings)

    # get (unitialized) containers
    containers = application.get_containers()

    for name, container in containers.items():
        print container.status

    return application


def create():
    application = initialize()
    application.create_containers()


def start():
    application = initialize()
    application.create_containers()
    application.start_containers()
    application.get_status()


def pull():
    application = initialize()
    application.pull_image()


def register():
    application = initialize()
    application.register()


# setup the application from the config file
# applications = create_applications()

def print_usage():
    print \
    """
    usage:

    dcr.py [status|create|start|pull] [configfile.yml]
    """

try:
    stream = open(sys.argv[2])
except:
    print_usage()
    sys.exit(1)

directives = utils.read_appconfig(sys.argv[2])


cmd = sys.argv[1]

if cmd == "status":
    initialize()
elif cmd == "create":
    create()
elif cmd == "start":
    start()
elif cmd == "pull":
    pull()
elif cmd == "register":
    register()


else:
    print_usage()
    sys.exit(1)
