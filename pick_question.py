from enum import Enum
import re


class QuestionOrientation(Enum):
    forward: 1
    backward: 2


class Answer:
    """
    题目答案：
    """

    def __init__(self, s):
        self.sn = 'A'
        self.title = ''
        self.parse_answer(s)

    def parse_answer(self, s):
        if (not str is None) and (str[1] == '.'):
            sa = s.split(s, '.')
            self.sn = sa[0].upper()
            self.title = sa[1].strip()
        return None


class Answers:
    """
    答案列表：
    """



class Question:
    """
    题目：
    """

    def __init__(self, s):
        self.isQuestion = False
        self.sn = 1
        self.title = ''
        self.orientation = QuestionOrientation.forward
        self.answers = None
        self.parse_question(s)

    def parse_question(self, s):
        matches = re.match(r'^(-?)(\d+)\.(.+)', s)
        if matches:
            self.isQuestion = True
            if matches[1] == '-':
                self.orientation = QuestionOrientation.backward
            else:
                self.orientation = QuestionOrientation.forward
            self.sn = matches[2]
            self.title = matches[3]
        return None

    def set_answers(self, answers):
        self.answers = answers
        return None


if __name__ == '__main__':
