
# assert.py


def get_score():
    s = int(input("请输入学生成绩: "))
    assert 0 <= s <= 100, '成绩超出范围'
    # if not (0 <= s <= 100):
    #     raise AssertionError('成绩超出范围')
    return s


try:
    score = get_score()
except AssertionError as err:
    print("错误数据是:", err)
    print('获取成绩失败')
    score = 0

print("学生的成绩为:", score)

