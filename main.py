from time import sleep

meme_dict = {
    "LOL,": "Komik bir şeye verilen cevap",
    "CRINGE,": "Garip ya da utandırıcı bir şey",
    "ROFL,": "Bir şakaya karşılık verilen gülme tepkisi",
    "SHEESH,": "Onaylamamak",
    "CREEPY,": "Korkunç",
    "AGGRO,": "Agresifleşmek/sinirlenmek"
}

print("Merhaba! Bu uygulama size bazı popüler kelimelerin anlamlarını sunar.")
sleep(1)
print("En fazla 5 kelime sorgulayabilirsiniz.")
sleep(1)
print("Lütfen tüm kelimeleri büyük harflerle yazın!")

for i in range(5):
    word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")
    
    if word in meme_dict.keys():
        print(word, meme_dict[word])
    else:
        print(word, 'kelimesi sözlüğümüzde bulunmuyor.')
        
print("Teşekkürler, tekrar görüşmek üzere!")
