from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

NEW_COLOUR = (1, 0, 0, 1)


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.names = ["Alice", "Bob", "Charlie", "Diana", "Eve"]

    def build(self):
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_name_widgets()
        return self.root

    def create_name_widgets(self):
        for name in self.names:
            label = Label(text=name)
            self.root.ids.main.add_widget(label)

        return self.root


DynamicLabelsApp().run()