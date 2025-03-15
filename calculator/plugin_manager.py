import importlib
import os

class PluginManager:
    def __init__(self, plugin_dir="plugins"):
        self.plugin_dir = plugin_dir
        self.plugins = {}

    def load_plugins(self):
        for filename in os.listdir(self.plugin_dir):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = f"plugins.{filename[:-3]}"
                module = importlib.import_module(module_name)
                if hasattr(module, "register"):
                    module.register(self)
    
    def register_plugin(self, name, function):
        self.plugins[name] = function

    def list_plugins(self):
        print("Available Plugins:")
        for plugin in self.plugins:
            print(f"- {plugin}")

