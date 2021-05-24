#!/bin/python

from datetime import date
import calendar
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

full_year_mode = False
today = date.today()
day = today.strftime("%d")
mounth_num_curr = today.strftime("%-m")
year_num_curr = today.strftime("%Y")

mounths = [
"January",
"February",
"March",
"April",
"May",
"June",
"July",
"August",
"September",
"October",
"November",
"December",
]

class Test(Gtk.Window):
    def get_date(self, mounth_num_param, year_num_param):
        global today
        global year
        global mounth_num
        global curr_mounth
        
        mounth_num = mounth_num_param
        year = year_num_param
        curr_mounth = calendar.month(int(year_num_param), int(mounth_num_param))
        
    def get_all_mounths(self, year_num_param):
        global year
        global all_year
        
        year = int(year_num_param)
        all_year = calendar.calendar(year, 1, 1, 3, 4)
        

    def __init__(self):        
        self.get_date(mounth_num_curr, year_num_curr)
        self.get_all_mounths(year_num_curr)
        Gtk.Window.__init__(self, title="Calendar")
        self.set_wmclass("test_class", "test_class")
        self.box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.box)
        
        box_curr_date = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        box_curr_cal = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        
        self.view_switch = Gtk.Switch()
        self.view_switch.connect("notify::active", self.view_switch_activete)
        self.view_switch.set_active(False)
        
        mounths_store = Gtk.ListStore(str)
        for i in mounths:
            mounths_store.append([i])
        mounths_combo = Gtk.ComboBox.new_with_model(mounths_store)
        renderer_text = Gtk.CellRendererText()
        mounths_combo.pack_start(renderer_text, True)
        mounths_combo.add_attribute(renderer_text, "text", 0)
        mounths_combo.set_active(int(mounth_num_curr) - 1)
        mounths_combo.connect("changed", self.change_mounth)
        
        adjustment = Gtk.Adjustment(lower=0, upper=100000, step_increment=1, page_increment=10)
        button_change_year = Gtk.SpinButton()
        button_change_year.set_adjustment(adjustment)
        button_change_year.set_value(int(year_num_curr))
        button_change_year.connect("value_changed", self.change_year)

        self.add(box_curr_date)
        self.add(box_curr_cal)
        self.label_curr_date = Gtk.Label("Today: " + str(year) + "-" + str(mounth_num_curr) + "-" + str(day))
        self.label_mounth = Gtk.Label(curr_mounth)
        
        box_curr_date.pack_start(self.label_curr_date, True, True, 3)
        box_curr_date.pack_start(self.view_switch, False, False, 3)
        box_curr_cal.pack_start(self.label_mounth, True, True, 3)
        
        box_buttons = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=6)
        box_buttons.pack_start(mounths_combo, True, True, 0)
        box_buttons.pack_start(button_change_year, True, True, 0)

        self.box.pack_start(box_curr_date, False, True, 3)
        self.box.pack_start(box_curr_cal, True, False, 3)
        self.box.pack_start(box_buttons, False, True, 3)
        
        self.set_size_request(320, 240)
        self.connect("destroy", Gtk.main_quit)

    def change_mounth(self, combo):
        mounth_num = combo.get_active() + 1
        self.get_date(mounth_num, year)
        if full_year_mode:
            print("year view mode")
        else:
            self.label_mounth.set_text(curr_mounth)
        
    def change_year(self, button_change_year):
        year = button_change_year.get_value_as_int()
        self.get_date(mounth_num, year)
        self.get_all_mounths(year)
        if full_year_mode:
            print("year view mode")
            self.label_mounth.set_text(all_year)
        else:
            self.label_mounth.set_text(curr_mounth)

    def view_switch_activete(self, view_switch, gparam):
        global full_year_mode
        
        if self.view_switch.get_active():
            full_year_mode = True
            self.label_mounth.set_text(all_year)
        else:
            full_year_mode = False
            self.label_mounth.set_text(curr_mounth)
        print(full_year_mode)

win = Test()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
