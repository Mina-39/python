# append 可以在已經存在的List當中加入新的資料
# 可以在程式執行的過程當中可以將資料加入已經存在的List的"最後面"
L = ["Hello", "World"]
L.append("Python")  # 加入python
print(L)  # 結果為 ['Hello', 'World', 'Python']

# insert 在程式執行的過程當中可以將資料加入已經存在的List的"指定位置"
# 記得List的index是從0開始
# 如果新增的位置超過List的長度, 會直接加入在最後面
# 如果新增的位置是負數, 會從List的最後面開始算起, 例如-1是最後一個位置
L = ["Hello", "World"]
L.insert(1, "Python")  # 在index 1的位置加入python
print(L)  # 結果為 ['Hello', 'Python', 'World']
L.insert(-1, "Java")  # 在倒數第一個位置加入Java
print(L)  # 結果為 ['Hello', 'Python', 'Java', 'World']
L.insert(-100, "C++")  # 索引位置超過範圍, 會加入在最前面
print(L)  # 結果為 ['C++', 'Hello', 'Python', 'Java', 'World']

# remove : 移除List中的指定資料
# 電腦會從左到右尋找第一個符合的元素並移除, 只移除一次
L = ["Hello", "World", "Python"]
L.remove("World")  # 移除World
print(L)  # 結果為 ['Hello', 'Python']

# pop : 移除List中的指定位置的資料, 並回傳該資料
L = ["Hello", "World", "Python"]
# 不給索引時, pop() 會移除最後一個元素
L.pop()  # 移除最後一個元素
print(L)  # 結果為 ['Hello', 'World']
s = L.pop(1)  # 如果用變數去存, 可以取得被移除的元素
print(s)  # 結果為 World
print(L)  # 結果為 ['Hello']
# 如果索引超過範圍, 會發生錯誤
# 負數索引也可以使用
L = ["Hello", "World", "Python"]
L.pop(-2)  # 移除倒數第二個元素
print(L)  # 結果為 ['Hello', 'Python']
# 負數索引超過範圍也會發生錯誤

# 'in'可以用在很多地方, 像是if判斷式
# 可以用來判斷某個元素是否在List當中
L = ["Apple", "Banana", "Cherry"]
if "Banana" in L:
    print("有香蕉!")
else:
    print("沒有香蕉!")

# in 在 for 迴圈中代表迴圈變數會依序取得右邊範圍當中的每一個元素
L = ["Apple", "Banana", "Cherry"]
for item in L:
    print("我喜歡吃", item)

# in 還可以用在字串當中, 檢查某個字串是否在字串當中
s = "Hello, World!"
if "World" in s:
    print("有World這個字串!")
