import os

import pcbnew
import wx

from .ugr_dialog import UGRDialog


class UGRPluginAction(pcbnew.ActionPlugin):
    def defaults(self) -> None:
        self.name = "UGR Plugin"
        self.category = "Templates"
        self.description = "This is plugin template"
        self.show_toolbar_button = True
        self.icon_file_name = os.path.join(os.path.dirname(__file__), "icon.png")

    def Run(self) -> None:
        pcb_frame = next(
            x for x in wx.GetTopLevelWindows() if x.GetName() == "PcbFrame"
        )

        dlg = UGRDialog(pcb_frame)
        if dlg.ShowModal() == wx.ID_OK:
            # this plugin does nothing usefull
            pass

        dlg.Destroy()
