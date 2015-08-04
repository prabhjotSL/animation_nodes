import bpy
from bpy.props import *
from .. events import treeChanged
from .. utils.recursion import noRecusion
from .. utils.nodes import iterAnimationNodes

class AnimationNodeTree(bpy.types.NodeTree):
    bl_idname = "an_AnimationNodeTree"
    bl_label = "Animation";
    bl_icon = "ACTION"

    def update(self):
        update()
        treeChanged()

@noRecusion
def update():
    updateAllNodes()

def updateAllNodes():
    for node in iterAnimationNodes():
        node.edit()
