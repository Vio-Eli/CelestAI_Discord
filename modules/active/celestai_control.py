"""
A module for controlling CelestAI

Usage Examples:
    - "Celest stop"
    - "Enable Google"
"""

from celestai.classes.module import Module
from celestai.classes.task import ActiveTask
from celestai import brain, log


class QuitTask(ActiveTask):

    def __init__(self):
        super(QuitTask, self).__init__(patterns=[r'\b(celeste)?(quit|stop)\b.*']) # celeste bc speech bug
        # TODO add Celest to .dict file properly

    def action(self, text):
        brain.inst.quit()


class ListModulesTask(ActiveTask):

    def __init__(self):
        super(ListModulesTask, self).__init__(words=['list modules', 'list mods'])

    def action(self, text):
        brain.inst.list_mods()


class ToggleModuleTask(ActiveTask):

    def __init__(self):
        super(ToggleModuleTask, self).__init__(patterns=[r'.*\b(enable|add|disable|remove) (.*)'])
        self.groups = {1: 'enable', 2: 'module'}

    def match(self, text):
        return self.match_and_save_groups(text, self.groups)

    def action(self, text):
        mod_name = self.module.lower().strip().replace(' ', '')
        if 'disable' in self.enable.lower() or 'remove' in self.enable.lower():
            log.info("Attempting to disable '"+mod_name+"'")
            brain.inst.disable_mod(mod_name)
        else:
            log.info("Attempting to enable '"+mod_name+"'")
            brain.inst.enable_mod(mod_name)


class celestaiControl(Module):

    def __init__(self):
        tasks = [QuitTask(), ListModulesTask(), ToggleModuleTask()]
        super(celestaiControl, self).__init__('celestai_control', tasks, priority=3)
