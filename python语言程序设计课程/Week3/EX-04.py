'''星号三角形 I
描述
读入一个整数N，N是奇数，输出由星号字符组成的等边三角形，要求：
第1行1个星号，第2行3个星号，第3行5个星号，依次类推，最后一行共N的星号。'''
N=eval(input())
starsnumber=1
stars='*'
for i in range(N):
    if starsnumber<=N:
       # print(stars)
        print(stars.center(N,' '))
    starsnumber=starsnumber+2
    stars=stars + '**'
