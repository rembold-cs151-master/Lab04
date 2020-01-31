# IMPORTANT!
# You don't need to do anything with this file
# It is only to provide some automated testing
# to give you feedback on if your code is working
# correctly! Please do not change!


import mock
import pytest

import Script1
import Script2

class Test_Script1:
    def test_small_word_big_length(self, capsys):
        _input = ['Hi', 40]
        with mock.patch('builtins.input', side_effect=_input):
            Script1.main()
            captured = capsys.readouterr()
            answer = captured.out.rstrip()
            assert answer == '------------------ Hi ------------------'

    def test_big_word_short_length(self, capsys):
        _input = ['This is a really great title!', 20]
        with mock.patch('builtins.input', side_effect=_input):
            Script1.main()
            captured = capsys.readouterr()
            answer = captured.out.rstrip()
            assert answer == 'The line length must be longer than the length of the desired title!'

class Test_Script2:
    def test_correct_output(self, capsys):
        Script2.main()
        captured = capsys.readouterr()
        answer = captured.out.rstrip()
        assert answer == 'The sum of the odd Fibonnaci numbers less than 100 is: 188'

