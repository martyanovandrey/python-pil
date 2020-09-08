from PIL import Image
import os
n = 0

''' уменьшить размер штампа
for r in os.listdir(path ='G:/test2'):
    img = Image.open('G:/test2/' + r)
    img_resized = img.resize((1457, 434))
    img_resized.save('G:/test2/' + r, dpi=(200,200))
'''


for r in os.listdir(path ='G:/test'):
    img = Image.open('G:/test/' + r)
    dpi = img.info['dpi']
    dpi_new = 200
    h, w = img.size
    h_cm = (h * 2.54 / dpi[0])
    h_new = round(h_cm / 2.54 * dpi_new)
    w_cm = (w * 2.54 / dpi[0])
    w_new = round(w_cm / 2.54 * dpi_new)
    img_resized = img.resize((h_new, w_new))
    img_resized.save('G:/test/' + r, dpi=(200, 200))
         
def mm_dpi(x, y):
    h, w = img.size
    h_wmark, w_wmark = watermark.size
    dpi = img.info['dpi']
    x_mm = (h * 2.54 / dpi[0]) * 10
    y_mm = (w * 2.54 / dpi[0]) * 10
    x_move = h - round((h / x_mm) * x) - h_wmark
    y_move = w - round((w / y_mm) * y) - w_wmark
    return (x_move, y_move)

for i, y in zip(os.listdir(path ='G:/test'), os.listdir(path ='G:/test2')):
    img = Image.open('G:/test/' + i)
    watermark = Image.open('G:/test2/' + y)
    n += 1
    img.paste(watermark, mm_dpi(6, 5))
    img.save("G:/test_result/img_ " + str(n) + ".jpg", dpi=img.info['dpi'])

print('Finish!')
