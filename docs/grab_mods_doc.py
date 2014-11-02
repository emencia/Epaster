"""
Grap all mods doc strings for each Paste

Paste apps are not real full python apps so we can't nicely import them to use 
them with "Sphinx.ext.autodoc" and so we must grap mods docs with this script.

This script is to be used only to re-generate RST file when you update some mods 
docs. It would need to be executed with 'eggedpy' to have buildout eggs context.
"""
import imp, os
import StringIO
import emencia_paste_djangocms_2
import emencia_paste_djangocms_3

def import_module_from_path(base_path, module_name):
    """
    Import a module from its base path
    """
    fp, pathname, description = imp.find_module(module_name, [base_path])
    try:
        module = imp.load_module(module_name, fp, pathname, description)
    except:
        return None, None
    finally:
        if fp:
            fp.close()
    return module


# Grab mods for each Paste app and write a RST document about its mods
for paste_app in (emencia_paste_djangocms_2, emencia_paste_djangocms_3):
    app_name = paste_app.__name__
    document_name = '{0}.rst'.format(app_name)
    app_path = os.path.dirname(paste_app.__file__)
    modsdir_path = os.path.join(app_path, 'django_buildout/project/mods_available')
    print "* Writing document '{document}' from path '{path}'".format(document=document_name, path=modsdir_path)
    app_document = StringIO.StringIO()
    
    # Add RST 'anchor' tag
    app_document.write(".. _intro_{0}:".format(app_name))
    app_document.write('\n')
    
    # Get the doc from the base __init__
    mod_index = import_module_from_path(modsdir_path, '__init__')
    app_document.write(mod_index.__doc__.strip())
    app_document.write('\n\n')
    
    # Scan available mods
    for directory in sorted(os.listdir(modsdir_path)):
        mod_abs = os.path.join(modsdir_path, directory)
        if os.path.isdir(mod_abs):
            # mod title
            app_document.write(directory)
            app_document.write('\n')
            app_document.write("-"*len(directory))
            app_document.write('\n\n')
            # mod content
            mod = import_module_from_path(modsdir_path, directory)
            app_document.write(mod.__doc__.strip())
            app_document.write('\n\n')
            
    fp = open(document_name, 'w')
    fp.write(app_document.getvalue())
    fp.close()
    app_document.close()
    
