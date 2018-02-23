import unittest
import os

import numpy as np

import meshcat
import meshcat.geometry as g
import meshcat.transformations as tf


class VisualizerTest(unittest.TestCase):
    def setUp(self):
        self.vis = meshcat.Visualizer().open()


class TestDrawing(VisualizerTest):
    def runTest(self):
        v = self.vis["shapes"]
        v.set_transform(tf.translation_matrix([1., 0, 0]))
        v["cube"].set_object(g.Box([0.1, 0.2, 0.3]))
        v["cube"].set_transform(tf.translation_matrix([0.05, 0.1, 0.15]))
        # TODO: cylinder
        v["sphere"].set_object(g.Mesh(g.Sphere(0.15), g.MeshLambertMaterial(color=0xff11dd)))
        v["sphere"].set_transform(tf.translation_matrix([0, 1, 0.15]))
        # TODO: ellipsoid

        v = self.vis["meshes/valkyrie/head"]
        v.set_object(g.Mesh(
            g.ObjMeshGeometry.from_file(os.path.join(meshcat.viewer_assets_path(), "data/head_multisense.obj")),
            g.MeshLambertMaterial(
                map=g.ImageTexture(
                    image=g.PngImage.from_file(os.path.join(meshcat.viewer_assets_path(), "data/HeadTextureMultisense.png"))
                )
            )
        ))
        v.set_transform(tf.translation_matrix([0, 0.5, 0.5]))

        v = self.vis["points"]
        v.set_transform(tf.translation_matrix([-1, 0, 0]))
        verts = np.random.rand(3, 100000)
        colors = verts
        v["random"].set_object(g.PointCloud(verts, colors))
        v["random"].set_transform(tf.translation_matrix([-0.5, -0.5, 0]))