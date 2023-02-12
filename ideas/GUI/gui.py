
from kivy.uix.screenmanager import ScreenManager,NoTransition, Screen
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import ObjectProperty
from kivymd.toast import toast
from datetime import datetime
from kivy import app
import kivy

kivy.require('1.0.8')
Window.size = (350,580)

class LoginApp(MDApp):
   def build(self):
      global Screen_Manager
      Screen_Manager = ScreenManager()
      Screen_Manager.add_widget(Builder.load_file("TheSoundProject.kv"))
      Screen_Manager.add_widget(Builder.load_file("TSPLogin.kv"))
      Screen_Manager.add_widget(Builder.load_file("graph.kv"))
      return Screen_Manager

   def on_start(self):
      Clock.schedule_once(self.login, 1)
   
   def login(self, *args):
      Screen_Manager.current = "TSPLogin"

   def graph(self, *args):
      Screen_Manager.current = "graph"
   
if __name__=='__main__':
    LoginApp().run()
































































