# coding=utf-8

from repeating_helper import lex_sort, remove_pyc, linux, backlight_dependent_on_time
from repeating_helper import lex_spell_checker, lex_duplicates, wortschatz

remove_pyc.main()
lex_sort.main()
backlight_dependent_on_time.main()
wortschatz.delete_duplicates()
lex_spell_checker.main()
lex_duplicates.main()
# todo - check last update date
linux.update_system()
# todo - check last backup date
# backup.main()
