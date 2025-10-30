def bold(text):
    return "\x1B[1m" + text + "\x1B[0m"

def italic(text):
    return "\x1B[3m" + text + "\x1B[0m"

def underline(text):
    return "\x1B[4m" + text + "\x1B[0m"

def strikethrough(text):
    return "\x1B[9m" + text + "\x1B[0m"

def reverse(text):
    return "\x1B[7m" + text + "\x1B[0m"

def rojo(texto):
  return "\x1B[31m" + texto + "\x1B[0m"

def celeste(texto):
  return "\x1B[36m" + texto + "\x1B[0m"

def verde(texto):
  return "\x1B[32m" + texto + "\x1B[0m"

def naranja(texto):
  return "\x1B[38;5;130m" + texto + "\x1B[0m"