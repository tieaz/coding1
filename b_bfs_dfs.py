# Chapter B ⇒ BFS/DFS

from typing import *

words = ['aba', 'abo', 'abs', 'aby', 'ace', 'act', 'add', 'ado', 'ads', 'adz', 'aff', 'aft', 'aga', 'age', 'ago', 'ags', 'aha', 'ahi', 'ahs', 'aid', 'ail', 'aim', 'ain', 'air', 'ais', 'ait', 'ala', 'alb', 'ale', 'all', 'alp', 'als', 'alt', 'ama', 'ami', 'amp', 'amu', 'ana', 'and', 'ane', 'ani', 'ant', 'any', 'ape', 'apo', 'app', 'apt', 'arb', 'arc', 'are', 'arf', 'ark', 'arm', 'ars', 'art', 'ash', 'ask', 'asp', 'ass', 'ate', 'att', 'auk', 'ava', 'ave', 'avo', 'awa', 'awe', 'awl', 'awn', 'axe', 'aye', 'ays', 'azo', 'baa', 'bad', 'bag', 'bah', 'bal', 'bam', 'ban', 'bap', 'bar', 'bas', 'bat', 'bay', 'bed', 'bee', 'beg', 'bel', 'ben', 'bes', 'bet', 'bey', 'bib', 'bid', 'big', 'bin', 'bio', 'bis', 'bit', 'biz', 'boa', 'bob', 'bod', 'bog', 'boo', 'bop', 'bos', 'bot', 'bow', 'box', 'boy', 'bra', 'bro', 'brr', 'bub', 'bud', 'bug', 'bum', 'bun', 'bur', 'bus', 'but', 'buy', 'bye', 'bys', 'cab', 'cad', 'cam', 'can', 'cap', 'car', 'cat', 'caw', 'cay', 'cee', 'cel', 'cep', 'chi', 'cig', 'cis', 'cob', 'cod', 'cog', 'col', 'con', 'coo', 'cop', 'cor', 'cos', 'cot', 'cow', 'cox', 'coy', 'coz', 'cru', 'cry', 'cub', 'cud', 'cue', 'cum', 'cup', 'cur', 'cut', 'cwm', 'dab', 'dad', 'dag', 'dah', 'dak', 'dal', 'dam', 'dan', 'dap', 'daw', 'day', 'deb', 'dee', 'def', 'del', 'den', 'dev', 'dew', 'dex', 'dey', 'dib', 'did', 'die', 'dif', 'dig', 'dim', 'din', 'dip', 'dis', 'dit', 'doc', 'doe', 'dog', 'dol', 'dom', 'don', 'dor', 'dos', 'dot', 'dow', 'dry', 'dub', 'dud', 'due', 'dug', 'duh', 'dui', 'dun', 'duo', 'dup', 'dye', 'ear', 'eat', 'eau', 'ebb', 'ecu', 'edh', 'eds', 'eek', 'eel', 'eff', 'efs', 'eft', 'egg', 'ego', 'eke', 'eld', 'elf', 'elk', 'ell', 'elm', 'els', 'eme', 'ems', 'emu', 'end', 'eng', 'ens', 'eon', 'era', 'ere', 'erg', 'ern', 'err', 'ers', 'ess', 'eta', 'eth', 'eve', 'ewe', 'eye', 'fab', 'fad', 'fag', 'fan', 'far', 'fas', 'fat', 'fax', 'fay', 'fed', 'fee', 'feh', 'fem', 'fen', 'fer', 'fes', 'fet', 'feu', 'few', 'fey', 'fez', 'fib', 'fid', 'fie', 'fig', 'fil', 'fin', 'fir', 'fit', 'fix', 'fiz', 'flu', 'fly', 'fob', 'foe', 'fog', 'foh', 'fon', 'fop', 'for', 'fou', 'fox', 'foy', 'fro', 'fry', 'fub', 'fud', 'fug', 'fun', 'fur', 'gab', 'gad', 'gae', 'gag', 'gal', 'gam', 'gan', 'gap', 'gar', 'gas', 'gat', 'gay', 'ged', 'gee', 'gel', 'gem', 'gen', 'get', 'gey', 'ghi', 'gib', 'gid', 'gie', 'gig', 'gin', 'gip', 'git', 'gnu', 'goa', 'gob', 'god', 'goo', 'gor', 'gos', 'got', 'gox', 'goy', 'gul', 'gum', 'gun', 'gut', 'guv', 'guy', 'gym', 'gyp', 'had', 'hae', 'hag', 'hah', 'haj', 'ham', 'hao', 'hap', 'has', 'hat', 'haw', 'hay', 'heh', 'hem', 'hen', 'hep', 'her', 'hes', 'het', 'hew', 'hex', 'hey', 'hic', 'hid', 'hie', 'him', 'hin', 'hip', 'his', 'hit', 'hmm', 'hob', 'hod', 'hoe', 'hog', 'hon', 'hop', 'hot', 'how', 'hoy', 'hub', 'hue', 'hug', 'huh', 'hum', 'hun', 'hup', 'hut', 'hyp', 'ice', 'ich', 'ick', 'icy', 'ids', 'iff', 'ifs', 'igg', 'ilk', 'ill', 'imp', 'ink', 'inn', 'ins', 'ion', 'ire', 'irk', 'ism', 'its', 'ivy', 'jab', 'jag', 'jam', 'jar', 'jaw', 'jay', 'jee', 'jet', 'jeu', 'jew', 'jib', 'jig', 'jin', 'job', 'joe', 'jog', 'jot', 'jow', 'joy', 'jug', 'jun', 'jus', 'jut', 'kab', 'kae', 'kaf', 'kas', 'kat', 'kay', 'kea', 'kef', 'keg', 'ken', 'kep', 'kex', 'key', 'khi', 'kid', 'kif', 'kin', 'kip', 'kir', 'kis', 'kit', 'koa', 'kob', 'koi', 'kop', 'kor', 'kos', 'kue', 'kye', 'lab', 'lac', 'lad', 'lag', 'lam', 'lap', 'lar', 'las', 'lat', 'lav', 'law', 'lax', 'lay', 'lea', 'led', 'lee', 'leg', 'lei', 'lek', 'let', 'leu', 'lev', 'lex', 'ley', 'lez', 'lib', 'lid', 'lie', 'lin', 'lip', 'lis', 'lit', 'lob', 'log', 'loo', 'lop', 'lot', 'low', 'lox', 'lug', 'lum', 'luv', 'lux', 'lye', 'mac', 'mad', 'mae', 'mag', 'man', 'map', 'mar', 'mas', 'mat', 'maw', 'max', 'may', 'med', 'meg', 'mel', 'mem', 'men', 'met', 'mew', 'mho', 'mib', 'mic', 'mid', 'mig', 'mil', 'mim', 'mir', 'mis', 'mix', 'moa', 'mob', 'moc', 'mod', 'mog', 'mol', 'mom', 'mon', 'moo', 'mop', 'mor', 'mos', 'mot', 'mow', 'mud', 'mug', 'mum', 'mun', 'mus', 'mut', 'myc', 'nab', 'nae', 'nag', 'nah', 'nam', 'nan', 'nap', 'naw', 'nay', 'neb', 'nee', 'neg', 'net', 'new', 'nib', 'nil', 'nim', 'nip', 'nit', 'nix', 'nob', 'nod', 'nog', 'noh', 'nom', 'noo', 'nor', 'nos', 'not', 'now', 'nth', 'nub', 'nun', 'nus', 'nut', 'oaf', 'oak', 'oar', 'oat', 'oba', 'obe', 'obi', 'oca', 'oda', 'odd', 'ode', 'ods', 'oes', 'off', 'oft', 'ohm', 'oho', 'ohs', 'oil', 'oka', 'oke', 'old', 'ole', 'oms', 'one', 'ono', 'ons', 'ooh', 'oot', 'ope', 'ops', 'opt', 'ora', 'orb', 'orc', 'ore', 'ors', 'ort', 'ose', 'oud', 'our', 'out', 'ova', 'owe', 'owl', 'own', 'oxo', 'oxy', 'pac', 'pad', 'pah', 'pal', 'pam', 'pan', 'pap', 'par', 'pas', 'pat', 'paw', 'pax', 'pay', 'pea', 'pec', 'ped', 'pee', 'peg', 'peh', 'pen', 'pep', 'per', 'pes', 'pet', 'pew', 'phi', 'pht', 'pia', 'pic', 'pie', 'pig', 'pin', 'pip', 'pis', 'pit', 'piu', 'pix', 'ply', 'pod', 'poh', 'poi', 'pol', 'pom', 'pop', 'pot', 'pow', 'pox', 'pro', 'pry', 'psi', 'pst', 'pub', 'pud', 'pug', 'pul', 'pun', 'pup', 'pur', 'pus', 'put', 'pya', 'pye', 'pyx', 'qat', 'qis', 'qua', 'rad', 'rag', 'rah', 'rai', 'raj', 'ram', 'ran', 'rap', 'ras', 'rat', 'raw', 'rax', 'ray', 'reb', 'rec', 'red', 'ree', 'ref', 'reg', 'rei', 'rem', 'rep', 'res', 'ret', 'rev', 'rex', 'rho', 'ria', 'rib', 'rid', 'rif', 'rig', 'rim', 'rin', 'rip', 'rob', 'roc', 'rod', 'roe', 'rom', 'rot', 'row', 'rub', 'rue', 'rug', 'rum', 'run', 'rut', 'rya', 'rye', 'sab', 'sac', 'sad', 'sae', 'sag', 'sal', 'sap', 'sat', 'sau', 'saw', 'sax', 'say', 'sea', 'sec', 'see', 'seg', 'sei', 'sel', 'sen', 'ser', 'set', 'sew', 'sex', 'sha', 'she', 'shh', 'shy', 'sib', 'sic', 'sim', 'sin', 'sip', 'sir', 'sis', 'sit', 'six', 'ska', 'ski', 'sky', 'sly', 'sob', 'sod', 'sol', 'som', 'son', 'sop', 'sos', 'sot', 'sou', 'sow', 'sox', 'soy', 'spa', 'spy', 'sri', 'sty', 'sub', 'sue', 'suk', 'sum', 'sun', 'sup', 'suq', 'syn', 'tab', 'tad', 'tae', 'tag', 'taj', 'tam', 'tan', 'tao', 'tap', 'tar', 'tas', 'tat', 'tau', 'tav', 'taw', 'tax', 'tea', 'ted', 'tee', 'teg', 'tel', 'ten', 'tet', 'tew', 'the', 'tho', 'thy', 'tic', 'tie', 'til', 'tin', 'tip', 'tis', 'tit', 'tod', 'toe', 'tog', 'tom', 'ton', 'too', 'top', 'tor', 'tot', 'tow', 'toy', 'try', 'tsk', 'tub', 'tug', 'tui', 'tun', 'tup', 'tut', 'tux', 'twa', 'two', 'tye', 'udo', 'ugh', 'uke', 'ulu', 'umm', 'ump', 'uns', 'upo', 'ups', 'urb', 'urd', 'urn', 'urp', 'use', 'uta', 'ute', 'uts', 'vac', 'van', 'var', 'vas', 'vat', 'vau', 'vav', 'vaw', 'vee', 'veg', 'vet', 'vex', 'via', 'vid', 'vie', 'vig', 'vim', 'vis', 'voe', 'vow', 'vox', 'vug', 'vum', 'wab', 'wad', 'wae', 'wag', 'wan', 'wap', 'war', 'was', 'wat', 'waw', 'wax', 'way', 'web', 'wed', 'wee', 'wen', 'wet', 'wha', 'who', 'why', 'wig', 'win', 'wis', 'wit', 'wiz', 'woe', 'wog', 'wok', 'won', 'woo', 'wop', 'wos', 'wot', 'wow', 'wry', 'wud', 'wye', 'wyn', 'xis', 'yag', 'yah', 'yak', 'yam', 'yap', 'yar', 'yaw', 'yay', 'yea', 'yeh', 'yen', 'yep', 'yes', 'yet', 'yew', 'yid', 'yin', 'yip', 'yob', 'yod', 'yok', 'yom', 'yon', 'you', 'yow', 'yuk', 'yum', 'yup', 'zag', 'zap', 'zas', 'zax', 'zed', 'zee', 'zek', 'zep', 'zig', 'zin', 'zip', 'zit', 'zoa', 'zoo', 'zuz', 'zzz']

DIGIT_LETTERS = {
  '2': 'abc',
  '3': 'def',
  '4': 'ghi',
  '5': 'jkl',
  '6': 'mno',
  '7': 'pqrs',
  '8': 'tuv',
  '9': 'wxyz',
}

def phoneword(number: int, words: List[str]) -> bool:
  digits = str(number)
  if '0' in digits or '1' in digits:
    return False

  queue = [(digits, '')]
  while queue:
    digits, word = queue.pop(0)
    if not digits:
      if word in words:
        return True
      continue

    for letter in DIGIT_LETTERS[digits[0]]:
      queue.append((digits[1:], word + letter))

  return False


def phoneword_solution(number: int, words: List[str]) -> bool:
  global DIGIT_LETTERS
  digits = str(number)
  if '0' in digits or '1' in digits:
    return False

  queue = [(digits, '')]
  while queue:
    digits, word = queue.pop(0)
    if not digits:
      if word in words:
        return word
      continue

    for letter in DIGIT_LETTERS[digits[0]]:
      queue.append((digits[1:], word + letter))

  return None


def phoneword_solutions(number: int, words: List[str]) -> bool:
  global DIGIT_LETTERS
  digits = str(number)
  if '0' in digits or '1' in digits:
    return False

  queue = [(digits, '')]
  solutions = []
  while queue:
    digits, word = queue.pop(0)
    if not digits:
      if word in words:
        solutions.append(word)
      continue

    for letter in DIGIT_LETTERS[digits[0]]:
      queue.append((digits[1:], word + letter))

  return solutions

print('# Phoneword')
print('phoneword(234):', phoneword(234, words))
# phoneword(234): False
print('phoneword_solution(234):', phoneword_solution(234, words))
# phoneword_solution(234): beg
print('phoneword_solutions(283):', phoneword_solutions(283, words))
# phoneword_solutions(283): ['ate', 'ave', 'bud', 'cud', 'cue']


import functools
import sys
import threading

def spinner(message='Loading...'):
  def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
      stop_event = threading.Event()

      def animate():
        chars = ['⠋', '⠙', '⠹', '⠸', '⠼', '⠴', '⠦', '⠧', '⠇', '⠏']
        for ch in iter(lambda: chars, None):
          for c in ch:
            if stop_event.is_set():
              return
            sys.stdout.write(f'\r{c} {message}')
            sys.stdout.flush()
            time.sleep(0.1)

      spinner_thread = threading.Thread(target=animate)
      spinner_thread.start()

      try:
        result = func(*args, **kwargs)
        return result
      finally:
        stop_event.set()
        spinner_thread.join()
        sys.stdout.write('\r' + ' ' * (len(message) + 2) + '\r')
        sys.stdout.flush()

    return wrapper
  return decorator


import time
import string

@spinner('Running slow word ladder ...')
def word_ladder(a: str, b: str, words: List[str]) -> bool:
  if len(a) != len(b):
    return False

  queue = [a]
  while queue:
    word = queue.pop(0)
    if word == b:
      return True

    for i in range(len(word)):
      for ch in string.ascii_lowercase:
        new_word = word[:i] + ch + word[i + 1:]
        if new_word != word and new_word in words:
          queue.append(new_word)

  return False

print('\n# Word Ladder')
start = time.perf_counter()
print('word_ladder(hot->tap):', word_ladder('hot', 'tap', words))
# word_ladder(hot->tap): True
print('Elapsed:', time.perf_counter() - start)
# Elapsed: 7.960171699523926


def bfs_path(
  init_state, succ_fn, is_goal_fn
) -> List[object]:
  queue = [[init_state]]
  while queue:
    path = queue.pop(0)
    if is_goal_fn(path[-1]):
      return path

    for next_state in succ_fn(path[-1]):
      queue.append(path + [next_state])

  return None


@spinner('Running slow word ladder path ...')
def word_ladder_path(a: str, b: str, words: List[str]) -> List[str]:
  if len(a) != len(b):
    return None

  queue = [[a]]
  while queue:
    path = queue.pop(0)
    word = path[-1]
    if word == b:
      return path

    for i in range(len(word)):
      for ch in string.ascii_lowercase:
        new_word = word[:i] + ch + word[i + 1:]
        if new_word != word and new_word in words:
          queue.append(path + [new_word])

  return None

print('\n# Word Ladder Path')
start = time.perf_counter()
print('word_ladder_path(hot->tap):', word_ladder_path('hot', 'tap', words))
# word_ladder_path(hot->tap): ['hot', 'tot', 'tat', 'tap']
print('Elapsed:', time.perf_counter() - start)
# Elapsed: 7.733508825302124


def bfs_visited(
  init_state, succ_fn, is_goal_fn
) -> bool:
  queue = [init_state]
  visited = set()
  while queue:
    state = queue.pop(0)
    visited.add(state)
    if is_goal_fn(state):
      return True

    for next_state in succ_fn(state):
      if next_state not in visited:
        queue.append(next_state)

  return False


def bfs(
  init_state: object,
  succ_fn: Callable[[object], List[object]],
  is_goal_fn: Callable[[object], bool],
) -> bool:
  queue = [init_state]
  while queue:
    state = queue.pop(0)
    if is_goal_fn(state):
      return True

    for next_state in succ_fn(state):
      queue.append(next_state)

  return False


def dfs(
  init_state, succ_fn, is_goal_fn
) -> bool:
  stack = [init_state]
  while stack:
    state = stack.pop()
    if is_goal_fn(state):
      return True

    for next_state in succ_fn(state):
      stack.append(next_state)

  return False


def dfs_recursive(
  state, succ_fn, is_goal_fn
) -> bool:
  if is_goal_fn(state):
    return True

  for next_state in succ_fn(state):
    if dfs_recursive(
      next_state, succ_fn, is_goal_fn
    ):
      return True

  return False


def bfs_solution(
  init_state, succ_fn, is_goal_fn
) -> object:
  queue = [init_state]
  while queue:
    state = queue.pop(0)
    if is_goal_fn(state):
      return state

    for next_state in succ_fn(state):
      queue.append(next_state)

  return None


def bfs_solutions(
  init_state, succ_fn, is_goal_fn
) -> object:
  queue = [init_state]
  solutions = []
  while queue:
    state = queue.pop(0)
    if is_goal_fn(state):
      solutions.append(state)
      continue

    for next_state in succ_fn(state):
      queue.append(next_state)

  return solutions
