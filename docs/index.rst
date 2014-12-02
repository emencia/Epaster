.. Epaster documentation master file, created by
   sphinx-quickstart on Sun May  5 14:59:11 2013.
.. _virtualenv: http://www.virtualenv.org/
.. _Emencia: http://www.emencia.com/
.. _Python Paste: http://pythonpaste.org/
.. _buildout: http://www.buildout.org/
.. _pip: http://www.pip-installer.org
.. _Django: https://www.djangoproject.com/
.. _emencia-paste-django: https://github.com/emencia/emencia-paste-django

Epaster
=======

Introduction
------------

`Emencia`_ uses the Epaster tool for web projects along with our techniques and procedures. It's mostly based on `Python Paste`_ and `buildout`_ to allow for the distribution of projects easy to install anywhere.

Its goal is to automatically create and initialize the project’s structure so you don't lose time assembling the different parts.

Epaster is not really a package, just a `buildout`_ project to assemble some apps to develop `Python Paste`_ templates (called a *paste*). In theory, you should be able to install these paste just with `virtualenv`_ and `pip`_, but Epaster assemble all our paste in a unique `buildout`_ project.

For now, it is only used to build `Django`_ projects through some paste packages.

Structure
---------

Finally, Epaster will build you a project that is designed to be use with some software and components, below you can find a simple diagram to resume their interaction.

.. graphviz::

    digraph environment {
        /* Define some default styles */
        node [shape=box, fillcolor=lightblue2, color=lightblue3, style=filled]; 
        edge [color=lightblue4]; 
        
        /* Define all the entities label */
        epaster [label="Epaster", shape=egg];
        buildout_env [label="Buildout", shape=note];
        django [label="Django Framework", shape=component];
        foundation [label="Foundation5", shape=component];
        eggs [label="Installed Eggs", shape=note];
        recipes [label="Buildout recipes", shape=note];
        scss [label="SCSS", shape=component];
        apps_sources [label="Development apps", shape=note];
        nginx_conf [label="Nginx Config", shape=folder];
        monit_conf [label="Monit Config", shape=folder];
        django_instance [label="django-instance", shape=folder];
        django_cms [label="DjangoCMS", shape=component];
        zinnia [label="Zinnia blog", shape=component];
        monit [label="Monit", shape=egg];
        nginx [label="Nginx", shape=egg];
        
        /* Entities cluster for Virtualenv */
        subgraph cluster_virtualenv {
            style=rounded;
            color=lightgrey;
            fontcolor="lightslategray";
            node [style=filled,color=white];
            label = "VirtualEnv";
            
            buildout_env -> {eggs apps_sources recipes};
            eggs -> django;
            recipes -> {django_instance nginx_conf monit_conf};
            django -> {django_cms zinnia};
            django_instance -> django;
            nginx_conf -> django_instance;
            monit_conf -> django_instance;
        }
        
        /* Entities cluster for SCSS */
        subgraph cluster_scss {
            style=rounded;
            color=lightgrey;
            fontcolor="lightslategray";
            node [style=filled,color=white];
            label = "Compass";
            
            scss -> foundation;
        }
        
        /* Root entities */
        epaster -> {buildout_env scss} [color=midnightblue];
        monit -> monit_conf [color=midnightblue];
        nginx -> nginx_conf [color=midnightblue];
    }


Table of contents
-----------------

.. toctree::
   :maxdepth: 2

   install.rst
   usage.rst
   emencia_paste_djangocms_2.rst
   emencia_paste_djangocms_3.rst
   tips.rst
   develop.rst
   history.rst
