quantity = int(input("จำนวนปืนที่รับมาขาย : "))
cost_price = int(input("ต้นทุนของปืนที่รับมาต่อกระบอก : "))
sell_price = int(input("ราคาที่จะนำไปขายต่อ : "))
team_members = int(input("จำนวนลูกน้องในทีมที่ไปทำงาน : "))

x = quantity * cost_price



s = sell_price * quantity

y = s - x

b = (y*20)/100

m = b / team_members

print("ต้นทุนทั้งหมด", x,"THB")
print("รายรับทั้งหมด",s,"THB")
print("กำไรสุทธิ", y,"THB")
print("จำนวนเงินที่หักไปให้บอส", b,"THB")
print("จำนวนเงินที่ลูกน้องแต่ละคนได้", m,"THB")