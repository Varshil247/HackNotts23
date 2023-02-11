from kivy.uix.screenmanager import ScreenManager,NoTransition
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
import kivy

<<<<<<< HEAD
Window.size = (350,580)
=======
kivy.require('1.0.8')
Window.size = (900,580)
>>>>>>> 8133ee53aa417644fcca2d9022c33cd5b0798f5d

class Graph(MDApp):
    def build(self):
     global Screen_Manager
     Screen_Manager = ScreenManager()
     Screen_Manager.add_widget(Builder.load_file("graph.kv"))
     return Screen_Manager

    def on_start(self):
       Clock.schedule_once(self.graph, 2)

    def graph(self, *args):
       Screen_Manager.current = "graph"
       

if __name__=='__main__':
    Graph().run()
