from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout


Builder.load_file('design.kv')
#Builder.load_file('variableLablel.kv')

class MyLayout(Widget):
    pass

class MyApp(App):
    def build(self):
        Window.clearcolor = (1,1,1,1)
        return MyLayout()
    
    
if __name__ == '__main__':
    MyApp().run()