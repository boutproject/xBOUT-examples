#!/usr/bin/env python

"""
Example producing a 3d animation from an elm-pb simulation.

For viewing the `.gif` produced by this script, you might find the [multigifview
viewer](https://github.com/johnomotani/multigifview) helpful.
"""

import dask
from xbout import open_boutdataset

datapath = "BOUT.dmp.*.nc"
gridpath = "cbm18_dens8.grid_nx68ny64.nc"
variable = "P"

ds = open_boutdataset(
    datapath,
    gridfilepath=gridpath,
    geometry="toroidal",
    keep_xboundaries=False,
    keep_yboundaries=False,
    info=False,
    chunks={"t": 1},
)

nx = ds.metadata["nx"]

da = ds[variable].bout.interpolate_parallel(n=16).bout.from_field_aligned()

da.bout.plot3d(
    engine="mayavi",
    style="surface",
    colormap="viridis",
    colorbar={"orientation": "vertical", "title": variable},
    colorbar_font_size=16,
    vmin=None,
    vmax=None,
    mayavi_figure_args={
        "size": (800, 800),
        "bgcolor": (1.0, 1.0, 1.0),
        "fgcolor": (0.0, 0.0, 0.0),
    },
    mayavi_view=(-40, 80, 8),
    surface_xinds=(nx // 3, 38),
    save_as=f"{variable}.gif",
)
