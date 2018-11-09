"""Handles different challenges"""
from classes.features import Features
from classes.discord import Discord
from challenges.basic import Basic
from challenges.level import Level
import ngucon as ncon
import time


class Challenge(Features):
    """Handles different challenges."""

    def start_challenge(self, challenge):
        """Start the selected challenge."""
        self.rebirth()
        self.click(ncon.CHALLENGEBUTTONX, ncon.CHALLENGEBUTTONY)
        b = Basic()
        l = Level()
        color = self.get_pixel_color(ncon.CHALLENGEACTIVEX,
                                     ncon.CHALLENGEACTIVEY)

        if color == ncon.CHALLENGEACTIVECOLOR:
            text = self.ocr(ncon.OCR_CHALLENGE_NAMEX1,
                            ncon.OCR_CHALLENGE_NAMEY1,
                            ncon.OCR_CHALLENGE_NAMEX2,
                            ncon.OCR_CHALLENGE_NAMEY2)
            print("A challenge is already active: " + text)
            if "basic" in text.lower():
                print("Starting basic challenge script")
                b.basic()

            elif "24 hour" in text.lower():
                print("Starting 24 hour challenge script")
                try:
                    x = ncon.CHALLENGEX
                    y = ncon.CHALLENGEY + challenge * ncon.CHALLENGEOFFSET
                    self.click(x, y, button="right")
                    time.sleep(ncon.LONG_SLEEP)
                    target = self.ocr(ncon.OCR_CHALLENGE_24HC_TARGETX1,
                                      ncon.OCR_CHALLENGE_24HC_TARGETY1,
                                      ncon.OCR_CHALLENGE_24HC_TARGETX2,
                                      ncon.OCR_CHALLENGE_24HC_TARGETY2)
                    target = int(self.remove_letters(target))
                    print(f"Found target boss: {target}")
                    b.basic(target)
                except ValueError:
                    print("couldn't detect the target level of 24HC")
                    Discord.send_message("Couldn't detect the" +
                                         "target level of 24HC", Discord.ERROR)

            elif "100 level" in text.lower():
                print("starting 100 level challenge script")
                l.lc()

            elif "blind" in text.lower():
                print("starting blind challenge script")
                l.blind()

            else:
                print("Couldn't determine which script to start from the OCR",
                      "input")
            #  TODO: add other challenges here

        else:
            x = ncon.CHALLENGEX
            y = ncon.CHALLENGEY + challenge * ncon.CHALLENGEOFFSET

            if challenge == 1:
                self.click(x, y)
                time.sleep(ncon.LONG_SLEEP)
                self.confirm()
                b.basic(58)

            elif challenge == 3:
                try:
                    self.click(x, y, button="right")
                    time.sleep(ncon.LONG_SLEEP)
                    target = self.ocr(ncon.OCR_CHALLENGE_24HC_TARGETX1,
                                      ncon.OCR_CHALLENGE_24HC_TARGETY1,
                                      ncon.OCR_CHALLENGE_24HC_TARGETX2,
                                      ncon.OCR_CHALLENGE_24HC_TARGETY2)
                    target = int(self.remove_letters(target))
                    print(f"Found target boss: {target}")
                    self.click(x, y)
                    time.sleep(ncon.LONG_SLEEP)
                    self.confirm()
                    time.sleep(ncon.LONG_SLEEP)
                    b.basic(target)
                except ValueError:
                    print("couldn't detect the target level of 24HC")
                    Discord.send_message("Couldn't detect the" +
                                         "target level of 24HC", Discord.ERROR)

            elif challenge == 4:
                self.click(x, y)
                time.sleep(ncon.LONG_SLEEP)
                self.confirm()
                l.lc()

    def check_challenge(self):
        """Check if a challenge is active."""
        self.rebirth()
        self.click(ncon.CHALLENGEBUTTONX, ncon.CHALLENGEBUTTONY)
        time.sleep(ncon.LONG_SLEEP)
        color = self.get_pixel_color(ncon.CHALLENGEACTIVEX,
                                     ncon.CHALLENGEACTIVEY)

        return True if color == ncon.CHALLENGEACTIVECOLOR else False
