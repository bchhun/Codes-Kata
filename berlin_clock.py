import unittest

class BerlinClockTests(unittest.TestCase):
    def test_midnight(self):
        self.assertEqual(berlin_clock("00:00:00"), "Y\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO")

    def test_daytime(self):
        self.assertEqual(berlin_clock("13:17:01"), "O\nRROO\nRRRO\nYYROOOOOOOO\nYYOO")

    def test_nightime(self):
        self.assertEqual(berlin_clock("23:59:59"), "O\nRRRR\nRRRO\nYYRYYRYYRYY\nYYYY")
    
    def test_midnight_24h(self):
        self.assertEqual(berlin_clock("24:00:00"), "Y\nRRRR\nRRRR\nOOOOOOOOOOO\nOOOO")    

class BerlinClockOutput:
    y_flag = "Y"
    r_flag = "R"
    off_flag = "O"

    def __init__(self, timestamp):
        self.hours, self.minutes, self.seconds = timestamp.split(":")

    def filler_output(self, to_be_filled, max_char):
        to_be_filled += (max_char - len(to_be_filled)) * self.off_flag
        return to_be_filled

    def seconds_output(self):
        if int(self.seconds) % 2 == 0:
            return self.y_flag
        return self.off_flag

    def hours_output(self):
        hours_max_char = 4

        first_row = (int(self.hours) / 5) * self.r_flag
        first_row = self.filler_output(first_row, hours_max_char)
        second_row = (int(self.hours) % 5) * self.r_flag
        second_row = self.filler_output(second_row, hours_max_char)

        return "%s\n%s" % (first_row, second_row)

    def minutes_output(self):
        first_row = "OOOOOOOOOOO"
        second_row = "OOOO"
        return "%s\n%s" % (first_row, second_row)

    def output(self):
        return "\n".join([
            self.seconds_output()
            , self.hours_output()
            , self.minutes_output()
        ])

def berlin_clock(timestamp):
    bco = BerlinClockOutput(timestamp)
    return bco.output()

if __name__ == '__main__':
    unittest.main()
