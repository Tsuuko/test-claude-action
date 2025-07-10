#!/usr/bin/env python3
"""
サンプルコードファイル
日本語コードレビュー機能をテストするためのサンプルです。
"""

def calculate_total(items):
    """
    アイテムの合計金額を計算する関数
    
    Args:
        items: 価格を持つアイテムのリスト
    
    Returns:
        合計金額
    """
    total = 0
    for item in items:
        total += item.price
    return total

def get_user_data(user_id):
    """
    ユーザーデータを取得する関数
    
    Args:
        user_id: ユーザーID
    
    Returns:
        ユーザー名とメールアドレス
    """
    # TODO: エラーハンドリングを追加
    user = database.get_user(user_id)
    return user.name, user.email

class ShoppingCart:
    """
    ショッピングカートクラス
    """
    
    def __init__(self):
        self.items = []
    
    def add_item(self, item):
        """
        アイテムを追加
        
        Args:
            item: 追加するアイテム
        """
        self.items.append(item)
    
    def get_total(self):
        """
        カートの合計金額を取得
        
        Returns:
            合計金額
        """
        return calculate_total(self.items)
    
    def clear(self):
        """
        カートを空にする
        """
        self.items = []

# テスト用のサンプルデータ
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

if __name__ == "__main__":
    # 使用例
    cart = ShoppingCart()
    
    # アイテムを追加
    cart.add_item(Item("商品A", 100))
    cart.add_item(Item("商品B", 200))
    cart.add_item(Item("商品C", 150))
    
    # 合計金額を表示
    print(f"合計金額: {cart.get_total()}円")
    
    # カートをクリア
    cart.clear()
    print(f"クリア後の合計金額: {cart.get_total()}円")