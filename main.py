import os
os.environ['KIVY_TEXT'] = 'pil'

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout


class RootWidget(AnchorLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        my_page = MyPage()

        self.add_widget(my_page)


class MyPage(GridLayout):

    def __init__(self, **kwargs):
        super(MyPage, self).__init__(**kwargs)
        self.cols = 2
        self.size_hint = [.5, .5]
        self.spacing = 5
        self.row_default_height=30
        for i in range(1, 7):
            self.add_widget(TextInput())
            self.add_widget(Button(text=f'К_{i}', font_size=10, size_hint_x=None, width=30))




class TestApp(App):

    def build(self):
        return RootWidget()


if __name__ == '__main__':
    TestApp().run()