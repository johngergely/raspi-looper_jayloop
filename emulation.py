class LED():
    def __init__(self, id, set_debug=False):
        self._id = id
        self.state = ''
        self._debug_level = set_debug
    
    def on(self):
        self.state = 'O'
        if self._debug_level:
            self.debug("on")

    def off(self):
        self.state = ''
        if self._debug_level:
            self.debug("off")

    def __repr__(self):
        return self.state

    def debug(self, called_by=''):
        print("LED", self._id, called_by, self.state)

class Button():
    def __init__(self, id, set_debug=True):
        self._id = id
        self._debug_level = set_debug
   
    def wait_for_press(self):
        if self._debug_level:
            self._debug("wait_for_press")

    def __repr__(self):
        return 'Button ' + str(self._id)

    def _debug(self, called_by=''):
        print("Button", self._id, called_by)
