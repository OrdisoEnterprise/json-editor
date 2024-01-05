# plugin_manager.py

import importlib
import inspect
import pkgutil
from pathlib import Path

class PluginManager:
    def __init__(self):
        self.plugins = {}

    def discover_plugins(self):
        # Discover and load plugins from the specified package
        # The 'package' parameter should be the name of the package containing your plugins
        # for _, name, _ in pkgutil.iter_modules([package]):
            # module = importlib.import_module(f"{package}.{name}")
            module_path = Path("C:/TTTech/asanchez_personal/env_manager/json-editor/tests/data/model/model/plugin_sample.py")
            module_name = module_path.stem  # Extract the module name without the extension

             # Import the module dynamically
            module = importlib.import_module(str(module_name))

            return module
            # for item_name in dir(module):
            #     item = getattr(module, item_name)
            #     if inspect.isclass(item) and issubclass(item, PluginBase) and item != PluginBase:
            #         self.register_plugin(name, item())

    def register_plugin(self, name, plugin):
        self.plugins[name] = plugin

    def execute_plugin(self, name, *args, **kwargs):
        if name in self.plugins:
            return self.plugins[name].execute(*args, **kwargs)
        else:
            print(f"Plugin '{name}' not found.")
