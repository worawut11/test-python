grade = int(input("คะแนน: "))
if grade >= 80:
    print("เกรด A")
elif grade >= 70:
    print("เกรด B")
elif grade >= 60:
    print("เกรด C")
elif grade >= 50:
    print("เกรด D")
else:
    print("เกรด F")
print("จบการประเมินเกรด")
# คำสั่งนี้จะถูกเรียกใช้ทุกครั้งหลังจากประเมินเกรดเสร็จสิ้น
# ไม่ว่าจะได้เกรดอะไร