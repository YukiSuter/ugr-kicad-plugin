import os
import sys
import subprocess
import shutil

from pathlib import Path

import pcbnew
import wx

from .version import __version__

from .stencil_dialog import StencilDialog

try:
    from kikit.stencil import createPrinted
except Exception as e:
    wx.LogMessage(f"error occured: {e}")

class UGRDialog(wx.Dialog):
    def __init__(self: "UGRDialog", parent: wx.Frame) -> None:
        super().__init__(parent, -1, "UGRacing Plugin Dialog")

        information_section = self.get_information_section()
        button_section = self.get_button_section()

        buttons = self.CreateButtonSizer(wx.OK)

        header = wx.BoxSizer(wx.HORIZONTAL)
        header.Add(information_section, 3, wx.ALL, 5)
        header.Add(button_section, 2, wx.ALL, 5)

        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(header, 0, wx.EXPAND | wx.ALL, 5)
        box.Add(buttons, 0, wx.EXPAND | wx.ALL, 5)

        self.SetSizerAndFit(box)

    def get_information_section(self) -> wx.BoxSizer:
        source_dir = os.path.dirname(__file__)
        icon_file_name = os.path.join(source_dir, "icon_full.png")
        icon = wx.Image(icon_file_name, wx.BITMAP_TYPE_ANY)
        icon_bitmap = wx.Bitmap(icon)
        static_icon_bitmap = wx.StaticBitmap(self, wx.ID_ANY, icon_bitmap)

        font = wx.Font(
            12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD
        )

        box = wx.BoxSizer(wx.VERTICAL)
        box.Add(static_icon_bitmap, 0, wx.ALL, 5)
        text = wx.StaticText(self, -1, f"UGR plugin version: {__version__}",)
        box.Add(text, 0, wx.ALL, 5)

        return box

    def get_button_section(self) -> wx.BoxSizer:
        box = wx.BoxSizer(wx.VERTICAL)
        stencil = wx.Button(self, -1, label="Stencil (for 3DP)")

        stencil.Bind(wx.EVT_BUTTON, self.on_stencil_click)

        box.Add(stencil, 0, wx.ALL | wx.ALIGN_CENTER_VERTICAL, 5)
        return box

    def on_stencil_click(self, event: wx.CommandEvent) -> None:
        try:
            stencildialog = StencilDialog(self)
        except Exception as e:
            wx.LogMessage(f"Dialog creation failed: {e}")

        if stencildialog.ShowModal() == wx.ID_OK:
            try:
                board = pcbnew.GetBoard()
                pcb_path = Path(board.GetFileName())
                output_path = str(pcb_path.parent / "stencils")
                wx.LogMessage(output_path)
                ft_input = stencildialog.ft_input.GetValue()
                pt_input = stencildialog.pt_input.GetValue()
                if not shutil.which("openscad"):
                    os.environ["PATH"] = f"\\\\LUMIERE.eng-ad.gla.ac.uk\\Groups\\UGR\\Software\\openscad-2021.01{os.pathsep}{os.environ['PATH']}"
                    wx.LogMessage("Added openscad on path")
                wx.LogMessage("Found openscad on path")
                pw_message = wx.MessageDialog(self, "Stencils generating. Please wait.", "Please wait", wx.OK | wx.ICON_INFORMATION)
                pw_message.ShowModal()
                createPrinted(pcb_path, output_path, 1.6, 0.15, 1, "", "", float(ft_input), float(pt_input))
                openX = wx.MessageDialog(self, "The stencils have successfully been generated. Would you like to open the folder?", "Open stencil folder?", wx.YES_NO | wx.YES_DEFAULT | wx.ICON_QUESTION)
                response = openX.ShowModal()    

                if response == wx.ID_YES:
                    subprocess.Popen(["explorer", output_path])
            except Exception as e:
                wx.LogMessage(f"Error occured: {e}")
            
        stencildialog.Destroy()