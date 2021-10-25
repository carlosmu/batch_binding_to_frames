import bpy

##############################################
#   MAIN OPERATOR
##############################################

class CB_OT_CameraRenamer(bpy.types.Operator):
    """Rename selected objects as frames sequence (1, 2, 3...)"""
    bl_idname = "cam_bind.camera_renamer"
    bl_label = "Rename Selected Objects"
    bl_options = {'REGISTER', 'UNDO'}

    # Prevents operator appearing in unsupported editors
    @classmethod
    def poll(cls, context):
        if (context.area.ui_type == 'VIEW_3D'):
            return True

    def execute(self, context):
        objects = context.selected_objects
        name = 1

        for ob in objects:    
            ob.name = str(name)
            name += 1

        return{'FINISHED'}

##############################################
# Register/unregister classes and functions
##############################################
def register():
    bpy.utils.register_class(CB_OT_CameraRenamer)

def unregister():
    bpy.utils.unregister_class(CB_OT_CameraRenamer)  
