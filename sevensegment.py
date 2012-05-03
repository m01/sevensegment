import RPi.GPIO as GPIO

class NumberOutOfRange(Exception):
  """
  This exception is thrown for numbers that are outside the range of values that a
  7 segment display can display.
  """

  def __init__(self, number):
    self.number = number

  def __str__(self):
    return repr("The number %d is outside the range of your 7 segment display" % self.number)

  def __unicode__(self):
    return u"The number %d is outside the range of your 7 segment display" % self.number


class SevenSegmentDisplay():
  """
  This is a class that controls a seven segment display attached to a Raspberry Pi's GPIO headers.
  By default, it's assumed that the pins are wired up in the following way:
  - pin 11 controls segment a (the top one)
  - pin 12 controls segment b (the top right one)
  - pin 13->c, 15->d, 16->e, 18->f, 22->g.
  These outputs are assumed to be active low, i.e. the segment lights up when
  the pin is turned OFF.
  """

  # the mapping of numbers to segments needed for displaying that number
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

  current_state = None #.. which means off

  # setup
  def __init__(self,
                 segments = {'a': 11, 'b': 12, 'c': 13, 'd': 15, 'e': 16, 'f': 18, 'g': 22 }):
    """
    The optional "segments" argument contains the pin mapping - please specify yours in the
    following way, if it differs from the default:
    segments={'a':15', 'b': 13, (etc)}  # a, b etc are the segments, 15, 13 etc are the pin numbers
    """

    self.segments = segments
    for s in self.segments:
      GPIO.setup(self.segments[s], GPIO.OUT)
    self.off()

  def off(self):
    """ turns the 7 segment display off. """
    for s in self.segments:
      GPIO.output(self.segments[s], True)

    #update state
    self.current_state = None

  def set(self, number_to_display):
    """ show some number on the 7 segment display. """

    if not (0 <= number_to_display <= 9):
      raise NumberOutOfRange(number_to_display)

    self.off()
    segments_to_turn_on = self.numbers[number_to_display]
    for s in segments_to_turn_on:
      GPIO.output(self.segments[s], False)

    #update state
    self.current_state = number_to_display
