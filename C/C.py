# %%
# VScodeで入力をテキストから読み込んで標準入力に渡す
import sys
import os
f=open(r'.\C\C_input.txt', 'r', encoding="utf-8")
# inputをフルパスで指定
# win10でファイルを作るとs-jisで保存されるため、読み込みをutf-8へエンコードする必要あり
# VScodeでinput file開くとutf8になってるんだけど中身は結局s-jisになっているらしい
sys.stdin=f

#
# 入力スニペット
# num = int(input())
# num_list = [int(item) for item in input().split()]
# num_list = [input() for _ in range(3)]
##################################
# %%
# 以下ペースト可

import math

A, B, X = [int(item) for item in input().split()]

res = 0
res_list = []
delta = 10**9 // 4
N= 10**9 // 2


is_search = True

while is_search:
    res = A * N + B * len(str(N))
    if res > X:
        N = N -delta
    elif res <= X:
        res_list.append(N)
        N = N + delta

    if delta <= 0:
        break

    delta = delta // 2 

new_res_list = []
for i in range(N - 1000, N + 1000):
    res = A * i + B * len(str(i))
    if res <= X:
        new_res_list.append(i)


if new_res_list == [] or max(new_res_list) <1:
    print(0)
else:
    if 1<= max(new_res_list) < 10**9:
        print(max(new_res_list))
    else:
        print(10**9)
