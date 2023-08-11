class NameError(Exception):
    def __init__(self, message):
        super().__init__(message)

try:
    name = input('이름을 입력해 주세요.')
    if len(name < 2 or len(name) > 4):
        ralse NameError('이름은 2 ~ 4 ')