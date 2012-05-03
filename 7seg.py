import RPi.GPIO as GPIO

class seven_segment_display():
  segments = {'a': 11, 'b': 12, 'c': 13, 'd': 15, 'e': 16, 'f': 18, 'g': 22 }

  numbers = [
    "abcdef", #0
    "bc", #1
    "baged", #2
    "abgcd", #3
    "bcgf", #4
    "afgcd", #5
    "afgcde", #6
    "abc", #7
    "abcdefg", #8
    "abcdfg", #9
    ]

  # setup
  def __init__(self):
    for s in self.segments:
      GPIO.setup(self.segments[s], GPIO.OUT)
    self.off()

  def off(self):
    """ turn all segments of the 7 segment display off. """
    for s in self.segments:
      GPIO.output(self.segments[s], True)

  def set(self, number_to_display):
    """ show some number on the 7 segment display. """
    self.off()
    segments_to_turn_on = self.numbers[number_to_display]
    for s in segments_to_turn_on:
      GPIO.output(self.segments[s], False)

