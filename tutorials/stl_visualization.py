from pycad.visualization import STLVisualizer

path_to_stl = './data/outdata/liver_4.stl'

visualizer = STLVisualizer(path_to_stl, ['#ffc800'])
visualizer.visualize()