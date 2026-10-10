son = int(input("Juft son kiriting: "))

if son % 2 == 0:
    print("Rahmat!")
else:
    print("Bu son juft emas.")
yosh = int(input("yoshingizni kiriting :"))
if yosh < 4 or yosh > 60:
    print("Muzeyga kirish bepul")
elif yosh < 18:
    print("Chipta narxi: 10000 so'm")
else:
    print("Chipta narxi: 20000 so'm")

son1 = float(input("Birinchi sonni kiriting: "))
son2 = float(input("Ikkinchi sonni kiriting: "))

if son1 == son2:
    print(f"{son1} = {son2}")
elif son1 < son2:
    print(f"{son1} < {son2}")
else:
    print(f"{son1} > {son2}")

mahsulotlar = ["un", "qovun", "olma", "anor", "uzum"]
bor_mahsulotlar = []
mavjud_emas = []
for i in range(1, 6):
    mah = input(f"Savatga {i}-mahsulotni qo'shing: ").strip().lower()

    if mah in mahsulotlar:
        bor_mahsulotlar.append(mah)
    else:
        mavjud_emas.append(mah)
if not mavjud_emas:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
else:
    print("Do'konimizda quyidagi mahsulotlar yo'q:")
    for mah in mavjud_emas:
        print(mah)

foydalanuvchilar = ["anvar", "nodir", "olim", "sarvar", "dilshod"]
yangi_login = input("Yangi login tanlang: ").strip().lower()

if yangi_login in foydalanuvchilar:
    print("Login band, yangi login tanlang!")
else:
    print(f"Xush kelibsiz, {yangi_login.capitalize()}!")

son = int(input("Istalgan butun son kiriting: "))

for i in range(2, 11):
    if son % i == 0:
        print(f"{son} soni {i} ga qoldiqsiz bo'linadi")
