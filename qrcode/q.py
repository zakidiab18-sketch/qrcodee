import qrcode
from qrcode.constants import ERROR_CORRECT_H

# الرابط من GitHub Pages
url = "https://zakidiab18-sketch.github.io/mywep/"

# إعدادات QR
qr = qrcode.QRCode(
    version=1,  # حجم الكود، 1 = صغير
    error_correction=ERROR_CORRECT_H,  # تصحيح أخطاء عالي
    box_size=10,  # حجم كل مربع أسود/أبيض
    border=4  # سمك الإطار حول الكود
)

# إضافة الرابط للكيو آر
qr.add_data(url)
qr.make(fit=True)

# إنشاء الصورة
img = qr.make_image(fill_color="black", back_color="white")

# حفظ الصورة
img.save("qrcode.png")

# print("تم إنشاء الكيو آر: qr_index.png")
