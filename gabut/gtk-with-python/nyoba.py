#!/usr/bin/env python
from gi.repository import Gtk
import gi
gi.require_version('Gtk', '3.0')
Gtk.init(None)
Window = Gtk.ButtonsType()
Hello = Gtk.MessageDialog(message_type=Gtk.MessageType.INFO,
                          buttons=Gtk.ButtonsType.OK,
                          text="Hello world!",
                          secondary_text="This is an example dialog.")
Hello.run()
