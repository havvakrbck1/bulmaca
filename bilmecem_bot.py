import telebot
import random

TOKEN = '' 
bot = telebot.TeleBot(TOKEN)

riddles = [
    {"soru": "Beni kırmadan, beni tutmak zordur. Beni kullanırken dikkatli olman gerekir, yoksa kaybolurum. Ben neyim?", "cevap": "dil"},
    {"soru": "Beni tutarsan, seni taşıyabilirim. Beni görmezsen, kaybolurum. Ben neyim?", "cevap": "gölge"},
    {"soru": "Bir odada duruyorum ama bir yerde varım. Suyu geçiremem, ama ışığı geçirebilirim. Ben neyim?", "cevap": "cam"},
    {"soru": "Her zaman ilerlerim ama asla geriye gitmem. Ben neyim?", "cevap": "zaman"},
    {"soru": "Bir şeyim ama aynı zamanda bir yerdeyim. Sadece bir yere giderim ve geri dönmem. Ben neyim?", "cevap": "okyanus"},
    {"soru": "Beni yiyebilirsin ama ben her zaman bir parça kalırım. Ben neyim?", "cevap": "pizza"},
    {"soru": "Bir odada hiç ışık yokken, bana bakamazsın ama seni görürüm. Ben neyim?", "cevap": "karanlık"},
    {"soru": "Küçük bir kutu içinde ben büyüyebilirim. Hiç bir zaman ben bir yere gitmem. Ben neyim?", "cevap": "seçenek"},
    {"soru": "Zamanla büyürüm, fakat hiçbir zaman yaşlanmam. Ben neyim?", "cevap": "yağmur"},
    {"soru": "Beni her zaman taşır, fakat durduğum zaman, senin içindeyim. Ben neyim?", "cevap": "yürek"},
    {"soru": "Beni asla öldüremezsin ama beni kapatınca, en derin sessizlik olur. Ben neyim?", "cevap": "göz"},
    {"soru": "Hiç canım yok ama dünyanın en önemli parçasıyım. Ben neyim?", "cevap": "havacılık"},
    {"soru": "Beni ters çevirirsen, başka bir şeyim. Ben neyim?", "cevap": "yol"},
    {"soru": "Birini alırım, ama bir daha asla almazsın. Ben neyim?", "cevap": "duvar"},
    {"soru": "Bir zamanlar dışarıda kalırdım ama sonra içeri gelirim. Ben neyim?", "cevap": "cam"},
    {"soru": "Beni kesemezsin ama sürekli büyürüm. Ben neyim?", "cevap": "yaprak"},
    {"soru": "Benim doğumum hep bende kalır. Ben neyim?", "cevap": "makine"},
    {"soru": "Yapmam gereken şeyin en iyi cevabını benden alırsın. Ben neyim?", "cevap": "hesap"},
    {"soru": "Hiç bir zaman kaybolmam ama asla bir şeyi de bulamam. Ben neyim?", "cevap": "televizyon"},
    {"soru": "Aklı birleştirerek hem doğru hem de yanlış bir çözüm bulursun. Ben neyim?", "cevap": "bulmaca"}
]

oyuncular = {}

@bot.message_handler(commands=['basla'])
def basla(message):
    user_id = message.from_user.id
    oyuncular[user_id] = {'puan': 0, 'soru_numarasi': 0}
    soru = riddles[0]['soru']
    bot.reply_to(message, f"Hadi başlayalım! Bulmacayı çöz: {soru}")

@bot.message_handler(func=lambda m: True)
def cevap_kontrol(message):
    user_id = message.from_user.id
    if user_id in oyuncular:
        cevap = message.text.lower().strip()
        soru_numarasi = oyuncular[user_id]['soru_numarasi']
        
        if cevap == riddles[soru_numarasi]['cevap']:
            oyuncular[user_id]['puan'] += 1
            oyuncular[user_id]['soru_numarasi'] += 1
            if oyuncular[user_id]['soru_numarasi'] < len(riddles):
                soru = riddles[oyuncular[user_id]['soru_numarasi']]['soru']
                bot.reply_to(message, f"Tebrikler! Puanın: {oyuncular[user_id]['puan']} \nBir sonraki bulmaca: {soru}")
            else:
                bot.reply_to(message, f"Harika! Tüm bulmacaları çözdün. Toplam puanın: {oyuncular[user_id]['puan']}")
                del oyuncular[user_id]
        else:
            bot.reply_to(message, "Yanlış cevap. Tekrar deneyin!")

bot.polling()
