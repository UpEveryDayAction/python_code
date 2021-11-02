import A
# from A import val_a
from A import SampleA

A.val_a= "B"
# print(A.val_a)
# s = SampleA(A.val_a)
s = SampleA()
"""
グローバル変数はモジュールのプロパティとして扱うため
モジュール自体のインポートが必要である。
変数だけをモジュールからインポートしても、操作がうまくできない。
"""