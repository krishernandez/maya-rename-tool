#----------------------------------------------------------------------------------------#
#------------------------------------------------------------------------------ HEADER --#

"""
:author:
    Kris Hernandez

:synopsis:
    This object renames objects you have selected. 

:description:
    This module is focused on selecting, creating and renaming objects in a Python module. 
    This simplifies repetitive task in Maya when running the script.

:applications:
    Maya.

:see_also:
    N/A
"""

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------- IMPORTS --#

# Default Python Imports
import maya.cmds as cmds

#----------------------------------------------------------------------------------------#
#--------------------------------------------------------------------------- FUNCTIONS --#

def rename_objects_by_type():
    # Get selected objects
    selected_objects = cmds.ls(selection=True)

    # Check if any objects are selected
    if not selected_objects:
        cmds.warning("No objects selected!")
        return

    # Create dictionaries for object type prefixes
    type_prefix = {
        'mesh': 'geo',
        'joint': 'jnt',
        'camera': 'cam',
        'light': 'lgt',
        'nurbsCurve': 'crv',
    }

    # Loop through each selected object
    for obj in selected_objects:
        # Get object type
        obj_type = cmds.objectType(obj)
        
        # Find out the prefix based on object type
        prefix = type_prefix.get(obj_type, 'obj')
        
        # Create a new name with a prefix and a number
        new_name = f"{prefix}_{obj}_01"
        
        # Rename the object
        cmds.rename(obj, new_name)
        print(f"Renamed {obj} to {new_name}")

# Run the function
rename_objects_by_type()
