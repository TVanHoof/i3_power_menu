#!/usr/bin/python

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import os

SHUTDOWN = 1
REBOOT = 2
LOGOUT = 3

NUM = 0
STR = 1

class PowerMenu():
    def __init__(self):
        self.actions = {(0,"quit"): Gtk.main_quit}
        self.window = Gtk.Window();
        self.window.set_size_request(400,150)
        self.window.add(self.create_buttons())
        self.window.connect("delete-event", Gtk.main_quit)
        self.window.connect("key-release-event", self.on_key_release)
        self.window.show_all()

    def add_button_and_connect(self, layout, caption, menuval, action):
        button = Gtk.Button(caption)
        button.connect("clicked", self.menu, menuval)
        layout.pack_start(button, True, True, 0)
        self.actions[(menuval, caption)] = action

        return button

    def create_buttons(self):
        my_layout = Gtk.HBox();

        self.add_button_and_connect(my_layout, "shutdown", SHUTDOWN, self.shutdown)
        self.add_button_and_connect(my_layout, "reboot", REBOOT, self.reboot)
        self.add_button_and_connect(my_layout, "logout", LOGOUT, self.logout)

        return my_layout

    def on_key_release(self, widget, event, data=None):
        for index_tuple in self.actions.keys():
            if ord(index_tuple[STR][0]) == event.keyval:
                self.actions[index_tuple]()

    def menu(self, widget, choice):
        for index_tuple in self.actions.keys():
            if choice == index_tuple[NUM]:
                self.actions[index_tuple]()

    def shutdown(self):
        os.system("shutdown -P now")

    def reboot(self):
        os.system("reboot")

    def logout(self):
        username = os.popen("whoami").read()
        os.system("pkill -u " + username)

    def run(self):
        Gtk.main()

menu = PowerMenu()
menu.run()
