"""Questing Script."""

# Helper classes
from classes.features import Features
from classes.window import Window

import coordinates as coords
import constants as const
import time

Window.__init__(object)
feature = Features()

Window.x, Window.y = feature.pixel_search(coords.TOP_LEFT_COLOR, 0, 0, 400, 600)
feature.menu("inventory")

print(f"Top left found at: {Window.x}, {Window.y}")

choice = ""
answers = {"y": True, "ye": True, "yes": True, "n": False, "no": False}
print("If you currently have an active quest that either is minor or has been subcontracted, consider skipping it before starting if you intend to use butter")
while choice not in answers:
    choice = input("Use butter for major quests? y/n: ").lower()

while True:  # main loop
    titans = feature.check_titan_status()
    if titans:
        feature.kill_titan(titans[0])
    text = feature.get_quest_text()
    majors = feature.get_available_majors()
    if majors == 0 and (coords.QUESTING_MINOR_QUEST in text.lower() or coords.QUESTING_NO_QUEST_ACTIVE in text.lower()):
        feature.questing(force=3)
    else:
        if not feature.check_pixel_color(*coords.COLOR_QUESTING_USE_MAJOR):
            feature.click(*coords.QUESTING_USE_MAJOR)
        feature.questing(butter=answers[choice])
    feature.pit()
    feature.gold_diggers(const.DEFAULT_DIGGER_ORDER)
    time.sleep(3)
