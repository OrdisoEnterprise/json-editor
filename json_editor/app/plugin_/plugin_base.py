# plugin_base.py

class ConfigModelPluginBase:
    def execute(self, *args, **kwargs):
        if "action" in kwargs:
            action = kwargs["action"]
            if action == "open":
                return self.open(*args, **kwargs)
            elif action == "validate":
                return self.validate(*args, **kwargs)
            elif action == "generate":
                return self.generate(*args, **kwargs)
            else:
                return f"Unknown action '{action}'"
        else:
            return "Action not specified in kwargs."

    def open(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement the open method.")

    def validate(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement the validate method.")

    def generate(self, *args, **kwargs):
        raise NotImplementedError("Subclasses must implement the generate method.")
