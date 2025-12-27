# index : 尋找指定元素在List中第一次出現的位置
# 如果元素不在List中會發生錯誤, 所以使用前建議先判斷是否存在
L = [1, 3, 2, 4, 5]
print(L.index(3))  # 找到3在index 1的位置

# count : 計算指定元素在List中出現的次數
# 這個方法很適合用來檢查重複資料的數量
L = ["Hello", "World", "Hello", "Python"]
print(L.count("Hello"))  # Hello出現了2次

# sort : 將List中的元素進行排序(由小到大)
# 注意: sort方法會直接修改原本的List, 不會產生新的List
L = [5, 2, 4, 1, 3]
L.sort()  # 將List排序
print(L)  # 結果為 [1, 2, 3, 4, 5]

# sort(reverse=True) : 將List中的元素進行排序(由大到小)
# reverse=True參數可以讓排序結果反轉
L = [5, 2, 4, 1, 3]
L.sort(reverse=True)  # 將List排序並反轉
print(L)  # 結果為 [5, 4, 3, 2, 1]

# reverse : 將List中的元素順序顛倒
# 這不是排序, 而是將元素的順序反轉
L = [1, 3, 2, 4, 5]
L.reverse()  # 將List順序反轉
print(L)  # 結果為 [5, 4, 2, 3, 1]

# List 和字串有很多相似的操作方式
# 我們可以像操作字串一樣操作List

# 合併兩個List : 使用 + 運算子將兩個 List 連接在一起
# 這會產生一個新的 List, 原本的 List 不會改變
L1 = [1, 2, 3]
L2 = [4, 5, 6]
L3 = L1 + L2  # 合併兩個List
print(L3)  # 結果為 [1, 2, 3, 4, 5, 6]

# 重複 List : 使用 * 運算子將 List 重複多次
# 這在需要產生大量重複資料時很有用
L = [1, 2, 3]
L = L * 3  # 重複List三次
print(L)  # 結果為 [1, 2, 3, 1, 2, 3, 1, 2, 3]

# 不同資料型態之間的轉換技巧
print(range(10))  # range 物件本身看不到具體內容, 只是一個範圍描述
print(list(range(10)))  # 使用 list() 將 range 物件轉換成 List
print(list("Hello"))  # 將字串轉換成 List, 每個字元都會變成獨立元素

# split : 將字串依照指定的分隔符號切割成多個部分
# 這個處理文字資料時非常常用
s = "Hello World"
L = s.split(" ")  # 以空格為分隔符號切割字串
print(L)  # 結果為 ['Hello', 'World']
calendar = "2020/12/25"
L = calendar.split("/")  # 以斜線為分隔符號切割字串
print(L)  # 結果為 ['2020', '12', '25']

# join : 將多個字串元素合併成一個字串
# 可以指定使用什麼符號來連接這些元素
L = ["Hello", "World"]
s = " ".join(L)  # 使用空格將List元素合併成字串
print(s)  # 結果為 "Hello World"

# 字典(Dictionary) : 用來儲存[key-value]配對的資料結構
# 字典很適合用來表示影對應關係的資料,像是商品和價格的對應

# 建立字典 : 使用大括號 {} 並以冒號 : 分隔 key 和 value
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d)  # 結果為 {'蘋果': 20, '香蕉': 30, '橘子': 25}

# 從字典中取得特定 key 對應的 value
# 如果 key 不存在會發生錯誤
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}
print(d["蘋果"])  # 結果為 20
# print(d["葡萄"])  # 這行會發生錯誤, 因為葡萄不在字典中

# 遍歷字典 : 有多種方式可以走訪字典的內容
d = {"蘋果": 20, "香蕉": 30, "橘子": 25}

# 方式一: 直接遍歷字典, 會取得所有的 key
for k in d:
    print(k)  # 印出 key 名稱 : 蘋果 香蕉 橘子
    print(d[k])  # 印出 key 對應的 value : 20 30 25
# 方式二: 明確使用 keys() 方法取得所有 key
for k in d.keys():
    print(k)  # 印出 key 名稱 : 蘋果 香蕉 橘子
    print(d[k])  # 印出 key 對應的 value : 20 30 25
# 方式三: 使用 values() 方法取得所有 value
for v in d.values():
    print(v)  # 印出所有 value : 20 30 25
# 方式四: 使用 items() 方法同時取得 key 和 value
# 這是最常用的方式, 因為可以同時存取 key 和 value
for k, v in d.items():
    print(f"{k}:{v}")  # 印出 key 和 value : 蘋果:20 香蕉:30 橘子:25
