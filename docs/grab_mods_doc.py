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
    
    # Scan available mods
    mods_document = []
    for directory in sorted(os.listdir(modsdir_path)):
        mod_abs = os.path.join(modsdir_path, directory)
        if os.path.isdir(mod_abs):
            # mod title
            mods_document.append(directory)
            mods_document.append('\n')
            mods_document.append("-"*len(directory))
            mods_document.append('\n\n')
            # mod content
            mod = import_module_from_path(modsdir_path, directory)
            mods_document.append(mod.__doc__.strip())
            mods_document.append('\n\n')
    mods_document = ''.join(mods_document)
    
    # Get the doc from the base __init__ and replace its 
    # pattern '.. document-mods::' by the mods documentations
    mod_index = import_module_from_path(modsdir_path, '__init__')
    app_document.write(mod_index.__doc__.strip().replace('.. document-mods::', mods_document))
    app_document.write('\n\n')
            
    fp = open(document_name, 'w')
    fp.write(app_document.getvalue())
    fp.close()
    app_document.close()
    
