#........1.........2.........3.........4.........5.........6.........7.........8
#
# Copyright (c) 2018 ldpgh  All rights reserved

import inspect

#........1.........2.........3.........4.........5.........6.........7.........8
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
  print(s1)


def prog_line():
  return inspect.currentframe().f_back.f_lineno

def prog_file():
  return inspect.currentframe().f_back.f_code.co_name

def prog_file_line(stack_depth=1):
  frm=inspect.currentframe()
  for ii in range(stack_depth): frm=frm.f_back
  return "%s:%d" % (frm.f_code.co_name, frm.f_lineno)


def info(arg, stack_depth=1, type="INFO", fcolor=pdefault):
  my_print(
    fcolor(
      "%s  @  %s   %s" 
      % (type, prog_file_line(stack_depth=stack_depth+1), arg.__repr__())
    )
  ) 

def warn(arg, stack_depth=1):
  info(arg, stack_depth+1, type="WARNING", fcolor=pyellow)

def error(arg, stack_depth=1):
  info(arg, stack_depth+1, type="ERROR", fcolor=pred)
