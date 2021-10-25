import bpy

##############################################
#   DRAW PANEL
##############################################

class CB_PT_CameraBinding(bpy.types.Panel):
    bl_label = "Batch Binding to Frames"
    bl_idname = "cam_bind.camera_batch_binding_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Item'

    def draw(self,context):
        layout = self.layout
        layout.operator("cam_bind.camera_renamer", icon='FILE_FONT')
        layout.operator("cam_bind.camera_binding", icon='CAMERA_DATA')


##############################################
## Register/unregister classes and functions
##############################################
def register():
    # bpy.types.TIME_MT_marker.append(draw_camera_binding) 
    bpy.utils.register_class(CB_PT_CameraBinding) 
        
def unregister():
    # bpy.types.TIME_MT_marker.remove(draw_camera_binding) 
    bpy.utils.unregister_class(CB_PT_CameraBinding) 
    