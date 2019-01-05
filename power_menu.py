#!/usr/bin/env python

import gtk
import os

class PowerMenu():
    def __init__(self):
        self.window = gtk.Window();
        self.window.set_size_request(400,150)
        self.window.add(self.create_buttons())
        self.window.connect("delete-event", gtk.main_quit)
        self.window.connect("key-release-event", self.on_key_release)
        self.window.show_all()

    def create_buttons(self):
        my_layout = gtk.HBox();

        shutdown = gtk.Button("shutdown")
        reboot = gtk.Button("reboot")
        logout = gtk.Button("logout")

        shutdown.connect("clicked",self.menu, 1)
        reboot.connect("clicked",self.menu, 2)
        logout.connect("clicked",self.menu, 3)

        my_layout.pack_start(shutdown, True, True, 0)
        my_layout.pack_start(reboot, True, True, 0)
        my_layout.pack_start(logout, True, True, 0)

        return my_layout

    def on_key_release(self, widget, event, data=None):
        if ord('q') == event.keyval:
            gtk.main_quit()
        elif ord('s') == event.keyval:
            self.shutdown()
        elif ord('r') == event.keyval:
            self.reboot()
        elif ord('l') == event.keyval:
            self.logout()
        else:
            print(event)

    def menu(self, widget, choice):
        # 1 => shutdown
        # 2 => reboot
        # 3 => logout
        if 1  == choice:
            self.shutdown()
        elif 2 == choice:
            self.reboot()
        elif 3 == choice:
            self.logout()
        else:
            print(error)

    def shutdown(self):
        os.system("shutdown -P now")

    def reboot(self):
        os.system("reboot")

    def logout(self):
        username = os.popen("whoami").read()
        os.system("pkill -u " + username)

    def run(self):
        gtk.main()

menu = PowerMenu()
menu.run()
