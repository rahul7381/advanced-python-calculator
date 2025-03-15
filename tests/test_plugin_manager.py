import pytest
from calculator.plugin_manager import PluginManager

@pytest.fixture
def plugin_manager():
    return PluginManager()

def test_plugin_manager_initialization(plugin_manager):
    assert isinstance(plugin_manager, PluginManager)

def test_load_plugins(plugin_manager):
    plugin_manager.load_plugins()
    assert isinstance(plugin_manager.plugins, dict)

def test_list_plugins(plugin_manager, capsys):
    plugin_manager.plugins = {"test_plugin": "TestPlugin"}
    plugin_manager.list_plugins()
    captured = capsys.readouterr()
    assert "test_plugin" in captured.out

def test_execute_plugin(plugin_manager):
    plugin_manager.plugins = {"sample_plugin": lambda x: x * 2}
    result = plugin_manager.plugins== 10

