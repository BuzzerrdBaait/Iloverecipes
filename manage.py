#!/usr/bin/env python

"""Django's command-line utility for administrative tasks."""

import os

import sys



def main():
    """..................IMPORTANT!!!
    ...............This manage.py file is modified to check if a local environment variable exists. 
    ...............IF localenv has been declared
    ...............USE Foodblog.localenv.py 
    ...............IF NOT localenv
    ...............use Foodblog.settings.py
    
    """

    env = os.environ.get('localenv')

    if env:

        os.environ.setdefault('DJANGO_SETTINGS_MODULE', f'FoodBlog.{env}')

    else:

        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FoodBlog.settings')



    try:

        from django.core.management import execute_from_command_line

    except ImportError as exc:

        raise ImportError(

            "Couldn't import Django. Are you sure it's installed and "

            "available on your PYTHONPATH environment variable? Did you "

            "forget to activate a virtual environment?"

        ) from exc

    

    execute_from_command_line(sys.argv)



if __name__ == '__main__':

    main()