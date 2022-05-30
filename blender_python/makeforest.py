import bpy

class Tree():
    def __init__(self, height, type, geo):
        self.height = height
        self.type = type
        self.geo = geo
        self.location = [0,0,0]
        self.rotation = [0,0,0]
    def set_location(self,loc):
        self.location = loc
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
        for num in self.num_trees:
            tr = Tree(3,"pine", )
            trees.append(tr)
            new_obj = self.duplicate_obj(tree_instance)
        return trees

def open_file(file_path):
    bpy.ops.wm.open_mainfile(filepath = file_path)

def main():
    open_file(r"C:\Users\k_nee\OneDrive\Documents\code\forest\forest_template.blend")
    forest = Forest(30, "forest_floor", "tree")
    bpy.ops.wm.save_as_mainfile(filepath = r"C:\Users\k_nee\OneDrive\Documents\code\forest\output\test.blend")

if __name__ == '__main__':
    main()

    
    