
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
<<<<<<< HEAD
import configparser
import mysql.connector
from graph import Graph
from kivymd.toast import toast
=======
>>>>>>> 8133ee53aa417644fcca2d9022c33cd5b0798f5d

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
       Clock.schedule_once(self.login, 2)

    
    def login(self, *args):
       Screen_Manager.current = "TSPLogin"

class Login(Screen):
      def connect(self):
         App = app.get_running_app()
         input_username=App.manager.get_screen('TSPLogin').ids['input_username'].text
         input_password=App.manager.get_screen('TSPLogin').ids['input_password'].text

         if  input_username == "Hacknotts23" and input_password =="TheSoundProject":
               toast("check")
               Screen_Manager.current = "graph"
               Graph().run()
         
   
if __name__=='__main__':
    LoginApp().run()
































































