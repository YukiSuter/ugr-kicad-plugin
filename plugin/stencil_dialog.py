import wx

class StencilDialog(wx.Dialog):
    def __init__(self, parent: wx.Frame):
        super().__init__(parent, title="Stencil Parameters", size=(300,200))

        vbox = wx.BoxSizer(wx.VERTICAL)
        
        ft_box = wx.BoxSizer(wx.HORIZONTAL)
        ft_label = wx.StaticText(self, label="Frame Tolerance (mm):")
        ft_box.Add(ft_label, 0, wx.ALL, 5)
        self.ft_input = wx.TextCtrl(self, value="0.2", style=wx.TE_PROCESS_ENTER)
        ft_box.Add(self.ft_input, 2, wx.EXPAND | wx.ALL, 5)

        pt_box = wx.BoxSizer(wx.HORIZONTAL)
        pt_label = wx.StaticText(self, label="Pad Tolerance (mm):")
        pt_box.Add(pt_label, 0, wx.ALL, 5)
        self.pt_input = wx.TextCtrl(self, value="0.0", style=wx.TE_PROCESS_ENTER)
        pt_box.Add(self.pt_input, 2, wx.EXPAND | wx.ALL, 5)

        buttons = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        vbox.Add(ft_box, 0, wx.ALL, 5)
        vbox.Add(pt_box, 0, wx.ALL, 5)
        vbox.Add(buttons, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        self.SetSizerAndFit(vbox)
