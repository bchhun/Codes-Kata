import unittest

class BerlinClockTests(unittest.TestCase):
    def test_midnight(self):
        self.assertEqual(berlin_clock("00:00:00"), "Y\nOOOO\nOOOO\nOOOOOOOOOOO\nOOOO")

    def test_daytime(self):
        self.assertEqual(berlin_clock("13:17:01"), "O\nRROO\nRRRO\nYYROOOOOOOO\nYYOO")

    def test_nightime(self):
        self.assertEqual(berlin_clock("23:59:59"), "O\nRRRR\nRRRO\nYYRYYRYYRYY\nYYYY")
        self.assertEqual(berlin_clock("23:58:59"), "O\nRRRR\nRRRO\nYYRYYRYYRYY\nYYYO")
    
    def test_midnight_24h(self):
        self.assertEqual(berlin_clock("24:00:00"), "Y\nRRRR\nRRRR\nOOOOOOOOOOO\nOOOO")    

class BerlinClock:
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
        first_row_max_char = 11
        second_row_max_char = 4
        first_row_single_value = 5

        first_row = "".join(
            map(
                lambda x: self.y_flag if x % 15 != 0 else self.r_flag 
                , range(5, int(self.minutes), 5)
            )
        )
        first_row = self.filler_output(first_row, first_row_max_char)


        second_row = self.y_flag * (int(self.minutes) % 5)
        second_row = self.filler_output(second_row, second_row_max_char)

        return "%s\n%s" % (first_row, second_row)

    def output(self):
        return "\n".join([
            self.seconds_output()
            , self.hours_output()
            , self.minutes_output()
        ])

def berlin_clock(timestamp):
    bco = BerlinClock(timestamp)
    return bco.output()

if __name__ == '__main__':
    unittest.main()
