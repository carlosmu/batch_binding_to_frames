# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

####################################
# IMPORT MODULES
####################################

from . import pt_camera_binding
from . import op_camera_binding
from . import op_camera_rename

bl_info = {
    "name": "Batch Binding to Frames",
    "author": "Carlos Munoz, Joni Mercado",
    "blender": (2, 83, 0),
    "version": (1, 0, 2),
    "category": "Camera",
    "location": "3D Viewport Sidebar > Item",
    "description": "Bind selected objects to frames by matching names",
    "warning": "",
    "doc_url": "",
    "tracker_url": "",
}

####################################
# REGISTER/UNREGISTER
####################################


def register():
    pt_camera_binding.register()
    op_camera_binding.register()
    op_camera_rename.register()

def unregister():
    pt_camera_binding.unregister()
    op_camera_binding.unregister()
    op_camera_rename.unregister()