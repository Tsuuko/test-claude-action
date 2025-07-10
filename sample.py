#!/usr/bin/env python3
"""
サンプルPythonコード - 日本語コードレビューのテスト用
"""

def calculate_sum(a, b):
    # 簡単な足し算の関数
    return a + b

def divide_numbers(x, y):
    # 割り算の関数（エラーハンドリングなし）
    return x / y

class Calculator:
    def __init__(self):
        self.result = 0
    
    def add(self, num):
        self.result += num
        return self.result
    
    def multiply(self, num):
        # 掛け算メソッド
        self.result *= num
        return self.result

# メイン処理
if __name__ == "__main__":
    calc = Calculator()
    
    # 計算のテスト
    print("足し算テスト:", calculate_sum(5, 3))
    print("割り算テスト:", divide_numbers(10, 2))
    
    # 計算機クラスのテスト
    calc.add(5)
    calc.multiply(2)
    print("計算機の結果:", calc.result)