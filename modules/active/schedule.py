"""
        File Name: schedule.py
        Schedules Shit
        Usage Examples:
        - "Add <insert task> to calendar"
"""

from celestai.classes.module import Module
from celestai.classes.task import ActiveTask

class SpeakPhrase(ActiveTask):

    def __init__(self):
        # Matches any statement with these words
        super(SpeakPhrase, self).__init__(words=['taken'])

    def action(self, text):
        self.speak('hi hi')


# This is a bare-minimum module
class Schedule(Module):

    def __init__(self):
        tasks = [SpeakPhrase()]
        super(Schedule, self).__init__('schedule', tasks, priority=2)
