total = 0
while True:
    num = int(input("ป้อนตัวเลข (พิมพ์ 0 เพื่อหยุด): "))
    if num == 0:
        break
    total += num
print("ผลรวมของตัวเลขทั้งหมดคือ:", total)