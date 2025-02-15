import numpy

#Sentetik Değerler
#   isim:                           Cumhuriyet          İstasyon           Pınar
#   Nüfus Yoğunluğu(kişi/km2):          300                 700             500
#   Mevcut Ulaşım Altyapısı(1-10):       3                   8               6
#   Maliyet Analizi(1-10):               7                   3               4
#   Çevresel Etki(1-10):                 6                   3               4
#   Sosyal Fayda(1-10):                  4                   9               7
#   Çevresel etki ve Maliyet analizleri negatif kriterler olduğundan dolayı ters şekilde puanlandı,

cumhuriyet = [300, 3, 7, 6, 4]
istasyon = [700, 8, 3, 3, 9]
pinar = [500, 6, 4, 4, 7]

mahalleler = numpy.array([cumhuriyet, istasyon, pinar])
names = ["Cumhuriyet Mahallesi", "İstasyon Mahallesi", "Pınar Mahallesi"]

#Kriterlerin önem dereceleri
kriter_onemi = numpy.array([5,7,7,4,6])

#Softmax: e^x / ∑ e^x
def softmax(x):
    exponentials = numpy.exp(x)
    return exponentials / numpy.sum(exponentials)

#Kriterlerin ağırlığı belirlenir
weights = softmax(kriter_onemi)

print("Kritiklerin Ağırlıkları:", weights)

#Normalleştirme işlemi
normalDegerler = mahalleler / mahalleler.max(axis=0)

#Normalletirilmiş değerler ile ağırlıkların matris çarpımı
scores = normalDegerler @ weights

#En yüksek skor
best = scores.argmax()

print(f"En iyi rota: {names[best]}")
print("Tüm rotalar:")
for i in range(len(mahalleler)):
    print(f"{names[i]} = {round(scores[i], 6)}")




