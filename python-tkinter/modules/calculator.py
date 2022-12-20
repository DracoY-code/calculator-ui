class Calculator:
    def __init__(self) -> None:
        self.result: str = ''
        self.keys: str = '789+456-123*0.=/'

    def display(self, value: str) -> None:
        self.result += value
        print(f'{value} added!')

    def solve(self) -> None:
        if self.result == '':
            print('Empty result!')
            return
        try:
            self.result = str(eval(self.result))
            print(f'{self.result} returned!')
        except:
            self.result = 'ERR'
            print('An error is returned!')

    def clear(self) -> None:
        self.result = ''
        print('Screen cleared!')
