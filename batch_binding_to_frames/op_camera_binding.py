import bpy

##############################################
#   MAIN OPERATOR
##############################################

class CB_OT_CameraBinding(bpy.types.Operator):
    """Bind selected objects to every frame using match by name with previosly renamed"""
    bl_idname = "cam_bind.camera_binding"
    bl_label = "Batch Binding Selected Objects"
    bl_options = {'REGISTER', 'UNDO'}

    # Outside Property
    clear_markers : bpy.props.BoolProperty(
        name = "Clear Scene Markers",
        description = "Clear the current scene markers",
        default = True,
    )

    # Prevents operator appearing in unsupported editors
    @classmethod
    def poll(cls, context):
        if (context.area.ui_type == 'VIEW_3D'):
            return True

    def execute(self, context):
        scene = bpy.context.scene # Scene
        scene.frame_start = 1 # Start frame
        scene.frame_end = len(bpy.context.selected_objects) +1 # End Frame
        scene.frame_current = scene.frame_start # Current Frame

        if self.clear_markers:
            # Clear previous markers
            context.scene.timeline_markers.clear()

        for frame in range(context.scene.frame_start, context.scene.frame_end, context.scene.frame_step):
            frame = context.scene.frame_current
            # Marker name and camera
            name = str(frame)
            camera = str(frame)
            # Create markers for every frame
            marker = scene.timeline_markers.new(name, frame=frame)
            marker.camera = scene.objects.get(camera)
            context.scene.frame_current += 1

        scene.frame_end -= 1
        scene.frame_current = 1


        return{'FINISHED'}
        
    # Popup
    def invoke(self, context, event):
        return context.window_manager.invoke_props_dialog(self)

    # Custom draw
    def draw(self, context):
        layout = self.layout
        layout.prop(self, "clear_markers")

##############################################
# Register/unregister classes and functions
##############################################
def register():
    bpy.utils.register_class(CB_OT_CameraBinding)

def unregister():
    bpy.utils.unregister_class(CB_OT_CameraBinding) 