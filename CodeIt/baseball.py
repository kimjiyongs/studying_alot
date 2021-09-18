# 컴퓨터는 0과 9 사이의 서로 다른 숫자 3개를 무작위로 뽑습니다. 예를 들어서 컴퓨터가 5, 2, 3을 뽑을 수도 있고 6, 7, 4를 뽑을 수도 있는 거죠.
# 사용자는 컴퓨터가 뽑은 숫자의 값과 위치를 맞추어야 합니다.
# 컴퓨터는 사용자가 입력한 숫자 3개에 대해서, 아래의 규칙대로 스트라이크(S)와 볼(B)의 개수를 알려줍니다.
# 숫자의 값과 위치가 모두 일치하면 S입니다.
# 숫자의 값은 일치하지만 위치가 틀렸으면 B입니다.
# 예를 들어 컴퓨터가 1, 2, 3을 뽑았다고 가정합시다. 사용자가 1, 3, 5를 입력하면, 1S(1의 값과 위치가 일치) 1B(3의 값만 일치)입니다.
# 기회는 무제한입니다. 하지만 몇 번의 시도 끝에 맞췄는지 기록됩니다.
# 3S(숫자 3개의 값과 위치를 모두 맞춘 경우)가 나오면 게임이 끝납니다.


# 0~9사이에 서로 다른 세개의 숫자 랜덤으로 뽑기
# 숫자 3개를 차례대로 입력하세요 출력하기
# 1번째 숫자를 입력하세요 : * 3
# 중복되는 숫자를 입력하거나 범위에서 벗어나는 숫자를 입력하면 다시 입력 받기
# 사용자가 숫자 3개를 입력하면 '*s *b' 출력
# 3s가 아니면 처음부터 다시
# 사용자가 3s를 입력하면 축하합니다 *번만에 값과 위치를 모두 맞추셨습니다. 출력

# 한번 바꿔봄

from random import randint

def generate_numbers():
    numbers = []

    while len(numbers) < 3:
        a = randint(0,9)

        if a not in numbers:
            numbers.append(a)

    print('0과 9사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다. \n')
    return numbers


def take_guess():
    print('숫자 3개를 하나씩 차례대로 입력하세요.')

    new_guess = []

    while len(new_guess) < 3:
        if len(new_guess) == 0 :
            guess = int(input('첫번째 숫자를 입력하세요: '))
            if guess > 9:
                print('숫자의 범위를 벗어났습니다.')
            elif guess in new_guess:
                print('중복된 숫자 입니다.')
            else:
                new_guess.append(guess)
        
        if len(new_guess) == 1:
            guess = int(input('두번째 숫자를 입력하세요: '))
            if guess > 9:
                print('숫자의 범위를 벗어났습니다.')
            elif guess in new_guess:
                print('중복된 숫자 입니다.')
            else:
                new_guess.append(guess)
        
        if len(new_guess) == 2:
            guess = int(input('세번째 숫자를 입력하세요: '))
            if guess > 9:
                print('숫자의 범위를 벗어났습니다.')
            elif guess in new_guess:
                print('중복된 숫자 입니다.')
            else:
                new_guess.append(guess)

    return new_guess



def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(0,3):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count


solution = generate_numbers()
print(solution)
counter = 0
while True:
    strike_count = 0 
    guesses = take_guess()
    strike, ball = get_score(guesses,solution)
    print(f'{strike}S {ball}B')
    counter += 1

    if strike == 3:
        print('축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.'.format(counter))
        break