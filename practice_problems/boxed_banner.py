class Banner:
    def __init__(self, message):
        self.message = message
        self.num_chars = len(self.message) + 2
    

    def __str__(self):
        return "\n".join([self._horizontal_rule(),
                          self._empty_line(),
                          self._message_line(),
                          self._empty_line(),
                          self._horizontal_rule()])

    def _empty_line(self):
        line = "|"+" "*self.num_chars+"|"
        return line

    def _horizontal_rule(self):
        line = "+"+"-"*self.num_chars+"+"
        return line

    def _message_line(self):
        return f"| {self.message} |"
    

# Comments show expected output

banner = Banner('To boldly go where no one has gone before.')
print(banner)
# +--------------------------------------------+
# |                                            |
# | To boldly go where no one has gone before. |
# |                                            |
# +--------------------------------------------+

banner = Banner('')
print(banner)
# +--+
# |  |
# |  |
# |  |
# +--+
