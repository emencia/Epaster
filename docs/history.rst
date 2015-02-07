.. _intro_history:
.. _graphviz: http://www.graphviz.org/

*******
History
*******

Changelog
=========

Version 2.2.7 - 2015/02/07
--------------------------

* Update to ``emencia_paste_djangocms_3==1.3.5``;

Version 2.2.6 - 2015/02/03
--------------------------

* Force Python2.x usage in virtual environment from the Makefile because actually a lot of used apps can't works with Python3 and some distributions allready use Python3 as the default Python interpreter;
* Update to ``emencia_paste_djangocms_3==1.3.4``;

Version 2.2.5 - 2015/01/29
--------------------------

* Update to ``emencia_paste_djangocms_3==1.3.3``;

Version 2.2.4 - 2015/01/28
--------------------------

* Update to ``emencia_paste_djangocms_2==1.9.8``;
* Update to ``emencia_paste_djangocms_3==1.3.2``;

Version 2.2.3 - 2015/01/28
--------------------------

* Update to ``emencia_paste_djangocms_3==1.3.1``;

Version 2.2.2 - 2015/01/28
--------------------------

* Update to ``emencia_paste_djangocms_3==1.3.0``;

Version 2.2.1 - 2015/01/20
--------------------------

* Update to ``emencia_paste_djangocms_2==1.9.7``;
* Update to ``emencia_paste_djangocms_3==1.2.9``;

Version 2.2.0 - 2015/01/14
--------------------------

* Update to ``emencia_paste_djangocms_3==1.2.8``;

Version 2.1.9 - 2015/01/06
--------------------------

* Update to ``emencia_paste_djangocms_3==1.2.7``;

Version 2.1.8.1 - 2014/12/26
----------------------------

* Fix: Forgotted to update ``bootstrap.py`` in previous version;

Version 2.1.8 - 2014/12/26
--------------------------

* Update to ``emencia_paste_djangocms_2==1.9.6.1``;
* Update to ``emencia_paste_djangocms_3==1.2.6``;
* Backport fix from them to the Epaster Makefile to avoid any bugs;

Version 2.1.7 - 2014/12/25
--------------------------

* Update to ``emencia_paste_djangocms_3==1.2.5``;
* Update documentation to add some informations about *Dr Dump* in 'Usage' document;

Version 2.1.6 - 2014/12/19
--------------------------

* Update to ``emencia_paste_djangocms_3==1.2.4``;
* Update documentation to rename the tips section as the topics section, then improve it a little bit;

Version 2.1.5 - 2014/12/01
--------------------------

* Update to ``emencia_paste_djangocms_3==1.2.3``;
* Update documentation to add a *Tips* section;

Version 2.1.4 - 2014/11/25
--------------------------

* Update to ``emencia_paste_djangocms_3==1.2.2``;
* Fix "version.cfg";
* Update documentation;

Version 2.1.3 - 2014/11/17
--------------------------

* Update to ``emencia_paste_djangocms_2==1.9.6``;
* Update to ``emencia_paste_djangocms_3==1.1.3``;

Version 2.1.2 - 2014/11/16
--------------------------

* Update to ``emencia_paste_djangocms_3==1.1.2``;
* Add "Development" notes in the docs;
* Update documentation;

Version 2.1.1 - 2014/11/07
--------------------------

* Update to ``zc.buildout==2.2.5``;
* Update to ``emencia_paste_djangocms_2==1.9.5``;
* Update to ``emencia_paste_djangocms_3==1.1.1``;
* Update documentation;

Version 2.1 - 2014/11/03
------------------------

* Update to ``zc.buildout==2.2.4`` to fix a bug introduced in 2.2.3;
* Update to last ``bootstrap.py`` script;
* Update to ``emencia_paste_djangocms_3==1.1``;

Version 2.0 - 2014/11/02
------------------------

* Implement new pastes for djangocms 2.x and 3.x
* Update doc to fit to the new structure

Version 1.8.2 - 2014/09/27
--------------------------

* Update docs to get the mods documentation directly from their docstring (in their __init__.py);
* Add eggedpy build part;

Version 1.8.1 - 2014/09/26
--------------------------

* Add Development environnment, close #2;
* Try to fix 'Doc compile fail on rtd', fix #1;

Version 1.8 - 2014/09/25
------------------------

First public release on Github, there has been some changes to split Epaster from its Django project template, the template and its sources now resides in its own package named "emencia-paste-django". Both of them starts from the 1.8 version for history purpose.

Version 1.7 - 2014/09/24
------------------------

* Fix nginx template;
* Moving common apps from 'apps' dir to 'project';
* Some minor changes before going public on Github;
* This is the last version from our internal and private repository before Epaster goes public on Github, previous changelog is keeped here for history although you can't access to these previous versions;

Version 1.6 - 2014/08/02
------------------------

* Update to Foundation 5.3.3;
* Improve documentation by using Sphinx theme Bootstrap with 'yeti' bootswatch theme and add History page;
* Add a structure diagram in introduction (warning this will require to install `graphviz`_ on your system);

Version 1.5 - 2014/07/28
------------------------

* Update to Foundation 5.3.1;
* Update README for last changes and to use the version from ``git describe --tags``;

Version 1.4 - 2014/07/27
------------------------

* Update to last Gestus & Po-projects clients;
* Add emencia-django-staticpages package and 'staticpages' mod to replace 'prototypes' mod;
* Add 'sitemap' mod;
* Fix Gestus config with Jinja2 template syntax;
* Use now a template recipe that use jinja and improve the nginx conf;

