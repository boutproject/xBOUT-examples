#!/usr/bin/env python

"""
Example producing a 3d animation from an elm-pb simulation.

For viewing the `.gif` produced by this script, you might find the [multigifview
viewer](https://github.com/johnomotani/multigifview) helpful.
"""

from mayavi import mlab

def test_fun():
    print("foobar")

#from argparse import ArgumentParser
#import dask
#from pathlib import Path
#import urllib.request
#from xbout import open_boutdataset
#
#parser = ArgumentParser(description="Example of creating a 3d movie. Uses elm-pb data")
#parser.add_argument(
#    "--ci",
#    action="store_true",
#    default=False,
#    help="Change settings for running in headless mode on a CI server.",
#)
#args = parser.parse_args()
#
#if args.ci:
#    from mayavi import mlab
#
#    mlab.options.offscreen = True
#
#script_dir = Path(__file__, "..").resolve()
#
#datapath = script_dir.joinpath("BOUT.dmp.*.nc")
#gridpath = script_dir.joinpath("cbm18_dens8.grid_nx68ny64.nc")
#variable = "P"
#save_as = script_dir.joinpath(f"{variable}.gif")
#
## Download data files if you do not have them already
#for filename in ["cbm18_dens8.grid_nx68ny64.nc", "BOUT.dmp.0.nc"]:
#    if not Path(filename).exists():
#        savepath = script_dir.joinpath(filename)
#        urllib.request.urlretrieve(
#            f"https://zenodo.org/record/4295926/files/{filename}?download=1", savepath
#        )
#
#ds = open_boutdataset(
#    datapath,
#    gridfilepath=gridpath,
#    geometry="toroidal",
#    keep_xboundaries=False,
#    keep_yboundaries=False,
#    info=False,
#    chunks={"t": 1},
#)
#
#nx = ds.metadata["nx"]
#
#da = ds[variable].bout.interpolate_parallel(n=16).bout.from_field_aligned()
#
#da.bout.plot3d(
#    engine="mayavi",
#    style="surface",
#    colormap="viridis",
#    colorbar={"orientation": "vertical", "title": variable},
#    colorbar_font_size=16,
#    vmin=None,
#    vmax=None,
#    mayavi_figure_args={
#        "size": (800, 800),
#        "bgcolor": (1.0, 1.0, 1.0),
#        "fgcolor": (0.0, 0.0, 0.0),
#    },
#    mayavi_view=(-40, 80, 8),
#    surface_xinds=(nx // 3, 38),
#    save_as=save_as,
#)
