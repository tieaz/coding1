# Chapter J ⇒ JSON

from typing import *

import json
import re


class Parser(object):
  def __init__(self, s: str):
    self.s = s
    self.n = len(s)
    self.ix = 0

  def skip_whitespace(self) -> None:
    while (self.ix < self.n and
        self.s[self.ix] in (' ', '\n', '\t')):
      self.ix += 1

  def read_char(self, ch: str) -> None:
    assert self.ix < self.n and self.s[self.ix] == ch, 'Expected character: ' + ch
    self.ix += 1

  def parse_string(self) -> str:
    # Matches a double quotes-wrapped string: "val".
    self.read_char('"')
    start_ix = self.ix
    escaped = False
    while self.ix < self.n:
      if self.s[self.ix] == '\\':
        escaped = True
      elif not escaped and self.s[self.ix] == '"':
        break
      else:
        escaped = False

      self.ix += 1  # Consume character.

    self.read_char('"')
    return self.s[start_ix:self.ix - 1]

  def parse_number(self) -> int:
    self.skip_whitespace()
    is_negative = False
    if self.s[self.ix] == '-':
      is_negative = True
      self.ix += 1
    elif self.s[self.ix] == '+':
      self.ix += 1

    self.skip_whitespace()
    assert self.ix < self.n and self.s[self.ix].isnumeric(), 'Expected number'
    value = 0
    while self.ix < self.n and self.s[self.ix].isnumeric():
      value = 10 * value + int(self.s[self.ix])
      self.ix += 1

    return -value if is_negative else value

  def parse_kv_pair(self) -> Tuple[str, any]:
    self.skip_whitespace()
    key = self.parse_string()
    self.skip_whitespace()
    self.read_char(':')
    self.skip_whitespace()

    assert self.ix < self.n, 'Expected character'
    if self.s[self.ix] == '"':
      value = self.parse_string()
    elif self.s[self.ix] == '{':
      value = self.parse_object()
    elif self.s[self.ix].isnumeric() or self.s[self.ix] in ('-', '+'):
      value = self.parse_number()
    else:
      assert False, "Can't parse value"

    self.skip_whitespace()
    return (key, value)

  def parse_object(self) -> object:
    # \s*{\s*(("key":"value",)*"key":"value")?\s*}
    self.skip_whitespace()
    self.read_char('{')
    object = {}

    while True:
      self.skip_whitespace()
      assert self.ix < self.n, 'Expected character'
      if self.s[self.ix] == '"':
        key, value = self.parse_kv_pair()
        object[key] = value
      elif self.s[self.ix] == ',':
        self.read_char(',')
        key, value = self.parse_kv_pair()
        object[key] = value
      elif self.s[self.ix] == '}':
        break

    self.read_char('}')
    return object

print('# JSON class parser')
s = """
{
  "foo": "bar",
  "zoo": {
    "asdf": "qwerty"
  },
  "bar": "foo",
  "nested1": {
    "nested2": {
      "nested3": {}
    }
  }
}
"""
print('From string:', re.sub(r'\s', '', s))
# From string: {"foo":"bar","zoo":{"asdf":"qwerty"},"bar":"foo","nested1":{"nested2":{"nested3":{}}}}
print('Parsed with class:', json.dumps(Parser(s).parse_object(), indent=2))
# Parsed with class: {
#   "foo": "bar",
#   "zoo": {
#     "asdf": "qwerty"
#   },
#   "bar": "foo",
#   "nested1": {
#     "nested2": {
#       "nested3": {}
#     }
#   }
# }


def parse_json(s: str) -> object:
  ix = 0
  n = len(s)

  # All helper methods advance `ix` inside `s`.

  def skip_whitespace() -> None:
    nonlocal ix
    while ix < n and s[ix] in (' ', '\n', '\t'):
      ix += 1

  def read_char(ch: str) -> None:
    nonlocal ix
    assert ix < n and s[ix] == ch, 'Expected character: ' + ch
    ix += 1

  def parse_string() -> str:
    # Matches a double quotes-wrapped string: "val".
    nonlocal ix
    read_char('"')
    start_ix = ix
    escaped = False
    while ix < n:
      if s[ix] == '\\':
        escaped = True
      elif not escaped and s[ix] == '"':
        break
      else:
        escaped = False

      ix += 1  # Consume character.

    read_char('"')
    return s[start_ix:ix - 1]

  def parse_kv_pair() -> Tuple[str, any]:
    # Parse doubles quotes-wrapped, colon-separated key-value pair.
    skip_whitespace()
    key = parse_string()
    skip_whitespace()
    read_char(':')
    skip_whitespace()

    # Value could be a string or object.
    assert ix < n, 'Expected character'
    if s[ix] == '"':
      value = parse_string()
    elif s[ix] == '{':
      value = parse_object()
    else:
      assert False, "Can't parse value"

    skip_whitespace()
    return (key, value)

  def parse_object() -> object:
    # \s*{\s*(("key":"value",)*"key":"value")?\s*}
    skip_whitespace()
    read_char('{')
    object = {}

    while True:
      skip_whitespace()
      assert ix < n, 'Expected character'
      if s[ix] == '"':
        key, value = parse_kv_pair()
        object[key] = value
      elif s[ix] == ',':
        read_char(',')
        key, value = parse_kv_pair()
        object[key] = value
      elif s[ix] == '}':
        break

    read_char('}')
    return object

  return parse_object()

print('Parsed with function:', json.dumps(parse_json(s), indent=2))
# Parsed with function: {
#   "foo": "bar",
#   "zoo": {
#     "asdf": "qwerty"
#   },
#   "bar": "foo",
#   "nested1": {
#     "nested2": {
#       "nested3": {}
#     }
#   }
# }


s = """
{
  "foo": 1,
  "zoo": {
    "asdf": "qwerty",
    "val1": +1234,
    "val2": -987
  },
  "bar": "foo",
  "nested1": {
    "nested2": {
      "nested3": {}
    }
  }
}
"""
print('From string:', re.sub(r'\s', '', s))
# From string: {"foo":1,"zoo":{"asdf":"qwerty","val1":+1234,"val2":-987},"bar":"foo","nested1":{"nested2":{"nested3":{}}}}
print('With numbers parsed with class:', json.dumps(Parser(s).parse_object(), indent=2))
# With numbers parsed with class: {
#   "foo": 1,
#   "zoo": {
#     "asdf": "qwerty",
#     "val1": 1234,
#     "val2": -987
#   },
#   "bar": "foo",
#   "nested1": {
#     "nested2": {
#       "nested3": {}
#     }
#   }
# }
