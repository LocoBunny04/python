class Television:
  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  MAX_CHANNEL = 3
  
  def __init__(self):
    self.status = False
    self.muted = False
    self.volume = Television.MIN_VOLUME
  