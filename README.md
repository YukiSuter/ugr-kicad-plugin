# UGRacing KiCAD plugin

This plugin is for KiCad, intended for use by UGRacing. The features can be found below:

- 3D model stencil generation (with parameters)

The plugin is written in python and utilises wxPython for UI elements, and pcbnew for interacting with KiCad.

## Building the plugin

### Build dependencies:
 - hatch (https://hatch.pypa.io/latest/) - simple to install and use, standalone binary available.

The command ```hatch build --target kicad-package``` should be used in the git directory to build the plugin. The plugin will be built and placed in a "dist" folder. You may need to add the hatch.exe to your path.