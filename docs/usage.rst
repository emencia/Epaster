.. _intro_usage:
.. _buildout: http://www.buildout.org/
.. _virtualenv: http://www.virtualenv.org/
.. _Gestus client: https://github.com/sveetch/Gestus-client
.. _PO-Projects client: https://github.com/sveetch/PO-Projects-client
.. _Dr Dump: https://github.com/emencia/dr-dump
.. _emencia-recipe-drdump: https://github.com/emencia/emencia-recipe-drdump

*****
Usage
*****

**Epaster** can only really be used within its virtual environment, so you must remember to enable it first: ::

    cd /home/emencia/epaster
    source bin/active

Then you can go the path where you want to create your project.

List of available project types
===============================

The following command: ::

    paster create --list-templates

will display a list of available project types which you can create: ::

    Available templates:
      basic_package:  A basic setuptools-enabled package
      django:         Django project
      paste_deploy:   A web application deployed through paste.deploy

This is just a sample, your install may have different paste.

Create a new project
====================

The **Epaster** tool is an interactive command. When launched, some questions will be asked for the selection of components and options to be used within the project: ::

    paster create -t django myproject

Install a new project
=====================

Once the project has been created by Buildout, it is autonomous of **Epaster** and you can move it wherever you want. This is the process we recommend (i.e., do not keep it under the Epaster tree).

So, for a newly created project called ``myproject``, you will have to enter it in its directory and just execute the automatic install command from Makefile: ::

    make install

This will install the virtual environment and all required packages using the default config ``buildout.cfg``. When it's finished, active the virtual environment: ::

    source bin/active

Then if you need to use a specific config, execute it as follows: ::

    buildout -c production.cfg

Generally, the database type used is **sqlite3**, stored in a ``database.sqlite3`` file at the root directory of your project.

Makefile actions
================

A Makefile is shipped within a project to include some useful maintenance command actions:

* ``help``: display this help list;
* ``install``: to proceed with a new install of this project. Use clean command before if you want to reset a current install;
* ``clean``: to clean your local repository of all the buildout and instance usage elements;
* ``delpyc``: to remove all ``*.pyc`` files, this is recursive from the current directory;
* ``assets``: to minify all assets and collect static files;
* ``scss``: to compile all SCSS elements with compass;
* ``syncf5``: to synchronize required Javascript files from foundation5 sources dir to the project static files;

It is only used from its location as follows.

You can use it with the following syntax: ::

    make ACTION

Where ``ACTION`` is the command action to use, as follows: ::

    make install

PO-Projects
===========

The `PO-Projects client`_ is pre-configured in all created projects but disabled by default. When enabled, its config file is automatically generated (in ``po_projects.cfg``), don't edit it because it will be regenerated each time buildout is used.

**It aims to ease PO translations management** between developpers and translation managers. 

The principe is that **developpers and translators does not have anymore to directly exchange PO files**. The developpers update the PO to the translation project on PO-Project webservice, translators update translations on PO-Project service frontend and developpers can get updated PO from the webservice.

To use it, you will have first to enable it in the buildout config, to install the client package, fill the webservice access and buildout part. Then when it's done, you have to create a project on PO-Project webservice using its frontend, then each required language for translation using the same locale names that the ones defined in the project settings.

There is only two available actions from the client :

Push action
    The ``push`` action role is to send updated PO (from Django extracts) from the project to the PO-Project webservice.
    
    Technically, the client will archive the locale directory into a tarball then send it to the webservice, that will use it to update its stored PO for each defined locales.
    
    Common way is (from the root of your project): ::
    
        cd project
        django-instance makemessages -a
        cd ..
        po_projects push


Pull action
    The ``pull`` action role is to get the updated translations from the webservice and install into the project.
    
    Technically, the client will download a tarball of the latest locale translations from the webservice and deploy it to your project, note that it will totally overwrite the project's locale directory. The compile PO (``*.mo`` files) are lost during this action and so each time you use this action you will have to recompile them.
    
    Common way is (from the root of your project): ::
    
        po_projects pull
        
    And probably reload your webserver.

Note that the client does not manage your repository, each time you change your PO files (from Django ``makemessages`` action or ``pull`` client action) you still have to commit them.

Gestus
======

The `Gestus client`_ is pre-configured in all created projects, its config file is automatically generated (in ``gestus.cfg``), don't edit it because it will be regenerated each time buildout is used.

You can register your environment with the following command : ::

    gestus register

Remember this should only be used in integration or production environment and you will have to fill a correct accounts in the ``EXTRANET`` part.

Dr Dump
=======

`Dr Dump`_ is an utility to help you to dump and load datas from your Django project's apps. It does not have any command line interface, just a buildout recipe (`emencia-recipe-drdump`_) that will generate some bash scripts (``datadump`` and ``dataload``) in your ``bin`` directory so you can use them directly to dump your data into a ``dumps`` directory.

If the recipe is enabled in your buildout config (this is the default behavior), its bash scripts will be generated again each time you invoke a buildout.

Buildout will probably remove your dumps directory each time it re-install Dr Dump and Dr Dump itself will overwrite your dumped data files each time you invoke it dump script. So remember backup your dumps before doing this.

Note that Dr Dump can only manage app that it allready know in the used map, if you have some other packaged app or project's app that is not defined in the map you want to use, you have two choices :

* Ask to a repository manager of Dr Dump to add your apps, for some *exotic* or uncommon apps it will probably be refused;
* Download the map from the repository, embed it in your buildout project and give its path into the ``dependancies_map`` recipe variable so it will use it.

The second one is the most easy and flexible, but you will have to manage yourself the map to keep it up-to-date with the original one.
