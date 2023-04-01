from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker

KV = '''
MDFloatLayout:

    MDRaisedButton:
        text: "Open time picker"
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.show_time_picker()
    MDLabel:
        id:select_time
        text: "Текущее время"
        pos_hint: {'center_x': .9, 'center_y': .1}
'''


class Time(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        
        return Builder.load_string(KV)
    def show_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save=self.on_save,on_cancel=self.on_cancel)
        time_dialog.open()
    def on_cancel (self, intance, value):
        self.root.ids.select_time.text = "Отменено"
    def on_save (self, intance, value):
        self.root.ids.select_time.text = str(value)
Time().run()
