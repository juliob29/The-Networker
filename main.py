import wx

class Application(wx.Frame):

    def __init__(self, parent, id):
        style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX)
        wx.Frame.__init__(self, parent, id, 'The NetWorker', size=(800,800), style=style)

        panel = wx.Panel(self)

        exit_button = wx.Button(panel, label="Exit App", pos=(410,200), size=(100,60))
        self.Bind(wx.EVT_BUTTON, self.closebutton, exit_button)

        new_button = wx.Button(panel, label="Add Contact", pos=(280,200), size=(100,60))

        random_buttom = wx.Button(panel, label="Pick a random Contact!", pos=(305,300), size=(165,60))

        # This is to close the Window
        self.Bind(wx.EVT_CLOSE, self.closewindow)

        status = self.CreateStatusBar()
        menubar = wx.MenuBar()
        File = wx.Menu()

        # Design

        header = wx.StaticText(panel, -1, "The Networker", (300,30), (260,-1))
        subtitle = wx.StaticText(panel, -1, "The best way to stay up to date with your network.",(190,50),(260,-1))
        julio_text = wx.StaticText(panel, -1, "By: Julio Ballista", (690,747), (260,-1))

        font = wx.Font(24, wx.MODERN, wx.BOLD, wx.NORMAL)
        subtitle_font = wx.Font(14, wx.MODERN, wx.BOLD, wx.NORMAL)
        julio_font = wx.Font(10, wx.MODERN, wx.BOLD, wx.NORMAL)

        header.SetFont(font)
        subtitle.SetFont(subtitle_font)
        julio_text.SetFont(julio_font)

        header.SetForegroundColour('black')
        subtitle.SetForegroundColour('black')
        julio_text.SetForegroundColour('black')


        File.Append(wx.NewId(), "Save Contacts to Disk", "This will save your contacts to disk as a JSON.")

        menubar.Append(File,"File")

        self.SetMenuBar(menubar)

    def closebutton(self, event):
        exit()
    
    def closewindow(self, event):
        exit()

if __name__ == '__main__':
    app = wx.App()
    frame = Application(parent=None, id=-1)
    frame.Show()
    app.MainLoop()