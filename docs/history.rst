.. _intro_history:
.. _graphviz: http://www.graphviz.org/

*******
History
*******

Changelog
=========

Version 1.8 - 25/09/2014
------------------------

First public release on Github, there has been some changes to split Epaster from its Django project template, the template and its sources now resides in its own package named "emencia-paste-django". Both of them starts from the 1.8 version for history purpose.

Version 1.7 - 24/09/2014
------------------------

* Fix nginx template;
* Moving common apps from 'apps' dir to 'project';
* Some minor changes before going public on Github;
* This is the last version from our internal and private repository before Epaster goes public on Github, previous changelog is keeped here for history although you can't access to these previous versions;

Version 1.6 - 08/02/2014
------------------------

* Update to Foundation 5.3.3;
* Improve documentation by using Sphinx theme Bootstrap with 'yeti' bootswatch theme and add History page;
* Add a structure diagram in introduction (warning this will require to install `graphviz`_ on your system);

Version 1.5 - 07/28/2014
------------------------

* Update to Foundation 5.3.1;
* Update README for last changes and to use the version from ``git describe --tags``;

Version 1.4 - 07/27/2014
------------------------

* Update to last Gestus & Po-projects clients;
* Add emencia-django-staticpages package and 'staticpages' mod to replace 'prototypes' mod;
* Add 'sitemap' mod;
* Fix Gestus config with Jinja2 template syntax;
* Use now a template recipe that use jinja and improve the nginx conf;

