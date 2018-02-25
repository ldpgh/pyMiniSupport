#........1.........2.........3.........4.........5.........6.........7.........8
#
# Copyright (c) 2018 ldpgh  All rights reserved

import inspect

#........1.........2.........3.........4.........5.........6.........7.........8
# Import the package colorama. If colorama is not installed the needed
# functions get a basic implementation.
try:
  import colorama
  colorama.init()
  print(colorama.Style.BRIGHT)
  def pred(s1): return colorama.Fore.RED+s1+colorama.Fore.WHITE
  def pyellow(s1): return colorama.Fore.YELLOW+s1+colorama.Fore.WHITE
  def pdefault(s1): return s1
except:
  def pdefault(s1): return s1
  def pred(s1): return s1
  def pyellow(s1): return s1

#........1.........2.........3.........4.........5.........6.........7.........8
def my_print(s1):
  """Wrapper around print() ... allows future modification (eg. verbose level)

  Args:
    s1 (String) : The String to be printed.
  """
  print(s1)

def prog_line():
  """Returns line number of current line"""
  return inspect.currentframe().f_back.f_lineno

def prog_file():
  """Returns file name the current line of the source code is in."""
  return inspect.currentframe().f_back.f_code.co_name

def prog_file_line(stack_depth=1):
  """Returns combined output of prog_file() and prog_line()
  
  Args:
    # stack_depth (int, optional) : Compensates additional stack depth
  """
  frm=inspect.currentframe()
  for ii in range(stack_depth): frm=frm.f_back
  return "%s:%d" % (frm.f_code.co_name, frm.f_lineno)

def info(arg, stack_depth=1, type="INFO", fcolor=pdefault):
  """Print messsage with information regarding file and line number. The 
  outlook respective content can be customized by the arguments.

  Args:
    arg : Any kind of argument to be printed by arg.__repr__()
    stack_depth (int, optional) : Compensates additional stack depth
    type (string, optional) : String to identify the kind of output
    fcolor (function-pointer, optional) ... function to handle colorized string
  """
  my_print(
    fcolor(
      "%s  @  %s   %s" 
      % (type, prog_file_line(stack_depth=stack_depth+1), arg.__repr__())
    )
  ) 

def warn(arg, stack_depth=1):
  """Wrapper function around info() with type="WARNING" and color yellow."""
  info(arg, stack_depth+1, type="WARNING", fcolor=pyellow)

def error(arg, stack_depth=1):
  """Wrapper function around info() with type="ERROR" and color red."""
  info(arg, stack_depth+1, type="ERROR", fcolor=pred)
