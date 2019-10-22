#!/usr/bin/env python
# License: Public Domain - https://creativecommons.org/share-your-work/public-domain/cc0/

from gimpfu import *


def create_animation_visible(image):
    newimage = gimp.Image(image.width, image.height, RGB)
    position = 0
    for layer in image.layers:
        if (layer.visible):
            newLayer = gimp.Layer(newimage, layer.name, newimage.width, newimage.height, RGBA_IMAGE, 100, NORMAL_MODE)
            newimage.add_layer(newLayer, position)
            position += 1
            pdb.gimp_edit_copy(layer)
            floatingLayer = pdb.gimp_edit_paste(newLayer, TRUE)
            pdb.gimp_floating_sel_anchor(floatingLayer)

    pdb.plug_in_animationplay(newimage, None)


register(
    "python_fu_create_animation_visible",
    "Creates animation from the visible layers of the current image.",
    "Creates animation from the visible layers of the current image.",
    "Balazs Papp",
    "Balazs Papp",
    "2019",
    "Create animation from visbile layers",
    "*",
    [
        (PF_IMAGE, 'image', 'Input image:', None)
    ],
    [],
    create_animation_visible, menu="<Image>/Filters/Animation/")

main()
