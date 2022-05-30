
#C:\Program Files\Blender Foundation\Blender 2.93\blender.exe' -b -P C:\Users\k_nee\OneDrive\Documents\git_repos\Python-Code\blender_python\makeforest.py

#This is a blender script to instance trees on a ground plane.
#Easily Configurable
#Randomize or Adjust Scale, Rotation, and Location.

import bpy
import pathlib
import pdb
ROOT_DIR = pathlib.Path(__file__).parent.absolute()
import random

class Tree():
    def __init__(self, height, type, geo):
        self.height = height
        self.type = type
        self.geo = geo
        self.location = [0,0,0]
        self.rotation = [0,0,0]
    def set_location(self,loc):
        self.location = loc
        self.geo.location = self.location
    def set_rotation(self,rot):
        self.rotation = rot

class Forest():
    def __init__(self, num_trees, ground_geo, tree_instance):
        self.num_trees = num_trees
        self.ground_geo = ground_geo
        self.trees = self.get_trees(tree_instance)
    def duplicate_obj(self, mesh_name):
        ob = bpy.data.objects.get(mesh_name)
        ob_dup = ob.copy()
        bpy.data.collections["Collection"].objects.link(ob_dup)
        return ob_dup
    def get_trees(self, tree_instance):
        trees = []
        for num in range(self.num_trees):
            
            new_obj = self.duplicate_obj(tree_instance)
            tr = Tree(3,"pine", new_obj)
            trees.append(tr)
        return trees

    def set_tree_locations(self):
        ground_obj = bpy.data.objects[self.ground_geo]
        dims = ground_obj.dimensions
        for tree in self.trees:
            dim_tree = tree.geo.dimensions
            new_loc = [random.uniform(-0.5*dims.x, 0.5*dims.x), random.uniform(-0.5*dims.y, 0.5*dims.y), dims.z]
            tree.set_location(new_loc)

def open_file(file_path):
    bpy.ops.wm.open_mainfile(filepath = file_path)

def main():
    open_file(str(ROOT_DIR) +'\\'+r"data\forest_template.blend")
    forest = Forest(100, "forest_floor", "tree")
    forest.set_tree_locations()
    bpy.ops.wm.save_as_mainfile(filepath =str(ROOT_DIR) +'\\'+ r"data\test.blend")

if __name__ == '__main__':
    main()

    
    