import string
from enum import IntEnum
from itertools import combinations

Weekdays = IntEnum('Weekdays', 'mon tue wed thu fri sat sun', start=0)
ALPHABET = list(string.ascii_uppercase)

def not_contain_golfer(group, groups):
    for golfer in group:
        for compare_group in groups:
            if golfer in compare_group:
                return False
    return True

class Schedule():
    def __init__(self,number_days=0, size_golfers=0, size_group=0):
        self._number_days = number_days
        if size_group * number_days != size_golfers:
            raise RuntimeError("It needs to be size group * number_days == size golfers")
        self._combinations = [elem for elem in combinations(ALPHABET[:size_golfers], size_group)]

    def create_subgroup(self):
        groups = []
        exclude = []
        for group in self._combinations:
            if group not in exclude and not_contain_golfer(group, groups):
                groups.append(group)
                exclude.append(group)
        # Removed used combinations
        self._combinations = set(self._combinations) - set(exclude)
        return groups

    def calculate(self):
        week_days = list(Weekdays)[:self._number_days]
        schedule = {key: [] for key in week_days}
        for day in week_days:
            proposal_subgroup = self.create_subgroup()
            schedule[day] = proposal_subgroup
        return schedule


def test_empty_constructor():
    schedule = Schedule ()
    assert schedule._number_days == 0

def test_one_day_constructor_fit_group_with_golfers():
    schedule = Schedule(number_days=1, size_golfers=3, size_group=3)
    calculated_schedule = schedule.calculate()
    assert Weekdays.mon in calculated_schedule.keys()

def test_subgroup():
    schedule = Schedule(number_days=5, size_golfers=20, size_group=4)
    groups = schedule.create_subgroup()
    assert len(groups) == 5
    assert len(groups[0]) == 4 and len(groups[1]) == 4




