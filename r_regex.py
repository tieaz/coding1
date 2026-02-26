# Chapter R ⇒ Regex

from typing import *


def phone_number_search(s: str) -> str:
  n = len(s)
  ix = 0
  while ix < n:
    if (
      ix + 12 < n and
      s[ix:ix + 3].isnumeric() and
      s[ix + 3] == '-' and
      s[ix + 4:ix + 7].isnumeric() and
      s[ix + 7] == '-' and
      s[ix + 8:ix + 12].isnumeric()
    ):
      return s[ix:ix + 12]

    ix += 1

  return None

print('# Phone number search')
s = """Lorem ipsum dolor sit amet, consectetur adipiscing elit please
call +1 (555) 012-3456 to reach our eiusmod tempor incididunt ut labore
et dolore magna aliqua department. Ut enim ad minim veniam, quis nostrud
exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat
estimated at $4,250, with an additional overhead of $1120.50. Duis aute
irure dolor in reprehenderit in voluptate contact our 24/7 support line
at 800-794-0958 excepteur sint occaecat cupidatat non proident  555-0001.
"""
print('Brute force search:', phone_number_search(s))
# Brute force search: 800-794-0958


import re

print('\n# Regex')
print(re.findall(r'\d\d\d-\d\d\d-\d\d\d\d', s))  # ==>
# ['800-794-0958']
print(re.findall(r'\d{3}-\d{3}-\d{4}', s))  # ==>
# ['800-794-0958']
print(re.findall(r'(\d{3}-|\(\d{3}\)\s)\d{3}-\d{4}', s))  # ==>
# ['(555) ', '800-']
print(re.findall(r'((\d{3}-|\(\d{3}\)\s)\d{3}-\d{4})', s))  # ==>
# [('(555) 012-3456', '(555) '), ('800-794-0958', '800-')]
print([m[0] for m in re.findall(r'((\d{3}-|\(\d{3}\)\s)?\d{3}-\d{4})', s)])  # ==>
# ['(555) 012-3456', '800-794-0958', '555-0001']


def regex_match(s: str, p: str) -> bool:
  if not p: return not s

  has_star = len(p) >= 2 and p[1] == '*'
  if not s:
    return has_star and regex_match(s, p[2:])

  is_wildcard = p[0] == '.'
  if not has_star:
    return (is_wildcard or s[0] == p[0]) and regex_match(s[1:], p[1:])
  else:
    if not is_wildcard:
      return (
        regex_match(s, p[2:]) or
        s[0] == p[0] and regex_match(s[1:], p)
      )
    else:
      return regex_match(s[1:], p) or regex_match(s, p[2:])

print('\n# Regular expression matching')
for s, p, check in [
  ('aa', 'a', False),
  ('aa', 'a*', True),
  ('ab', '.*', True),
  ('mississippi', 'mis*is*ip*.', True),
  ('mississippii', 'mis*is*ip*.', False),
]:
  val = regex_match(s, p)
  print(s + '<-' + p, 'match:', val)
  assert val == check
  # aa<-a match: False
  # aa<-a* match: True
  # ab<-.* match: True
  # mississippi<-mis*is*ip*. match: True
  # mississippii<-mis*is*ip*. match: False


def regex_match_zug(s: str, p: str) -> bool:
  if not p: return not s

  has_star = len(p) >= 2 and p[1] == '*'
  has_zug = len(p) >= 2 and p[1] == '?'
  if not s:
    return (has_star or has_zug) and regex_match_zug(s, p[2:])

  is_wildcard = p[0] == '.'
  if not has_star and not has_zug:
    return (is_wildcard or s[0] == p[0]) and regex_match_zug(s[1:], p[1:])
  elif has_zug:
    return (
      regex_match_zug(s, p[2:]) or
      (is_wildcard or s[0] == p[0]) and regex_match_zug(s[1:], p[2:])
    )
  else:  # No zug or star.
    if not is_wildcard:
      return (
        regex_match_zug(s, p[2:]) or
        s[0] == p[0] and regex_match_zug(s[1:], p)
      )
    else:
      return regex_match_zug(s[1:], p) or regex_match_zug(s, p[2:])

print('\n# Zero-or-one quantifier')
for s, p, check in [
  ('aa', 'a', False),
  ('aa', 'a?', False),
  ('aa', 'a*', True),
  ('aa', 'aa?', True),
  ('ab', '.*', True),
  ('ab', 'a?.*', True),
  ('mississippi', 'mis*is*ip*.', True),
  ('mississippi', 'mis*is*ip*.?', True),
  ('mississippii', 'mis*is*ip*.', False),
]:
  val = regex_match_zug(s, p)
  print(s + '<-' + p, val)
  assert val == check
  # aa<-a False
  # aa<-a? False
  # aa<-a* True
  # aa<-aa? True
  # ab<-.* True
  # ab<-a?.* True
  # mississippi<-mis*is*ip*. True
  # mississippi<-mis*is*ip*.? True
  # mississippii<-mis*is*ip*. False
