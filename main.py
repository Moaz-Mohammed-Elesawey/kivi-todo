from kivymd.app import MDApp
from kivymd.uix.list import IRightBodyTouch, OneLineAvatarIconListItem
from kivymd.uix.selectioncontrol import MDCheckbox
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDRaisedButton

from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty


class MainLayoutScreen(Screen):
    pass

class MainScreen(Screen):
    pass

class AddScreen(Screen):
    pass

class ListItemWithCheckbox(OneLineAvatarIconListItem):
    '''Custom list item.'''
    icon = StringProperty("bookmark")


class RightCheckbox(IRightBodyTouch, MDCheckbox):
    '''Custom right container.'''
    pass


class MainApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Orange'
        self.theme_cls.primary_hue = '900'
        self.theme_cls.theme_style = 'Light'

    def on_start(self):
        # self.root.ids.dev_info.text = 'created and maintaned by [b]MOAZ MOHAMMED EL-ESSAWEY[/b]'
        self.populate_todos()

    def populate_todos(self):
        for i in range(30):
            self.root.ids.main_layout.ids.main_screen.ids.todos_list.add_widget(
                ListItemWithCheckbox(text=f"Item {i}", on_press=lambda e: self.show_todo(e.text))
            )

    def show_todo(self, title):
        todo_dialog = MDDialog(title=title,
            buttons=[
                MDRaisedButton(
                    text="UPDATE", md_bg_color=(0,0,1,1),
                ),
                MDRaisedButton(
                    text="DELETE", md_bg_color=(1,0,0,1),
                ),
            ],
        )
        todo_dialog.open()

    def on_task_done(self):
        pass

    def _change_style(self, *args):
        _theme = self.theme_cls.theme_style
        if _theme == 'Dark':
            self.theme_cls.theme_style = 'Light'
        elif _theme == 'Light':
            self.theme_cls.theme_style = 'Dark'

    def _change_theme(self):
        self.root.ids['nav_drawer'].set_state('close')
        theme_dialog = MDThemePicker()
        theme_dialog.open()

    def change_screen(self, screen_name, direction='left'):
        _manager = self.root.ids['main_layout'].ids['layout_manager']
        _manager.current = screen_name
        _manager.transition.direction = direction



if __name__ == '__main__':
    MainApp().run()
