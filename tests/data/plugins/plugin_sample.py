import sys
import os
import json
from enum import Enum
from typing import Union
from enum import Enum
from pathlib import Path
import dataclasses

from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from typing_extensions import Annotated
from typing import List, Dict, Optional

from pydantic import Field, TypeAdapter, BaseModel, Field
from pydantic.config import ConfigDict
from pydantic.dataclasses import dataclass

from json_editor.app.plugin_.plugin_base import ConfigModelPluginBase
from json_editor.app.plugin_.plugin_manager import PluginManager


root_dir = "TO_BE_FIX_ROOT_DIR"

class TestTypes(str, Enum):
    UnitTests = 'UnitTests'
    ComponentTests = 'ComponentTests'
    HWSWIntTests = 'HWSWIntTests'

class FrameworkTypes(str, Enum):
    Unity = 'Unity'
    GTest = 'GTest'
    VCast = 'VCast'

class RunnersTypes(str, Enum):
    CMake = 'CMake'
    VCastCLI = 'VCastCLI'
    NoRunner = 'NoRunner'

@dataclass
class Project:
    name: str = "Default Project"
    team: str = "Default Team"
    mail: str = "default@example.com"

@dataclass
class GlobalPaths():
    root_dir: str = "/default/root"
    src_dir: str = "/default/src"
    doc_dir: str = "/default/doc"
    build_dir: str = "/default/build"


class TestEnvironment(BaseModel):
    name: str = "DefaultTestEnv"
    # type: TestTypes = TestTypes.UnitTests
    # framework: FrameworkTypes = FrameworkTypes.Unity
    # runner: RunnersTypes = RunnersTypes.NoRunner
    execution_path: str = "/test/execution/path"


class SW_Component(BaseModel):
    name: str = "Default Component"
    version: str = "v0.0.0"
    tests_env: List[TestEnvironment]


class SW_Repo(BaseModel):
    """
    This is the description of the main model
    """

    model_config = ConfigDict(title='Environment')

    project: Project = Field(default_factory=Project)
    paths: GlobalPaths = Field(default_factory=GlobalPaths)
    components: List[SW_Component] = Field(default_factory=lambda: [SW_Component(name="Default Component", path="$(paths.root_dir)/default/path")])
    fecha_entrega: str


class ConfigModelSamplePlugin(ConfigModelPluginBase):

    def get_id(self):
        return ('SW_Repo')

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
        print("Opening SamplePlugin with args:", args)
        # Perform open logic if needed
        return "SamplePlugin opened successfully"

    def validate(self, *args, **kwargs):
        print("Validating SamplePlugin with args:", args)
        # Perform validation logic if needed
        return "SamplePlugin validation passed"

    def generate(self, *args, **kwargs):
        print("Generating SamplePlugin with args:", args)
        # Perform generation logic if needed
        return "SamplePlugin generated content"


class Plugin(QAction):
    def __init__(self, root):
        self.root = root
        super(QAction, self).__init__(root.tr('Import Vector CAN DBC Sinals'), root)
        self.setStatusTip('Import Vector CAN DBC Sinals.')
        self.triggered.connect(self.onAction)

    def onAction(self):
        print("OnAction plugin_sample")
        pass
