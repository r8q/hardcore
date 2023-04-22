import telebot

# Botunuzun token'ını buraya girin
TOKEN = '5987082377:AAGYanzjQT7WRN8UAS7_-ZWoQFhUpBMvx8I'

# Telebot kütüphanesi ile bir bot nesnesi oluşturun
bot = telebot.TeleBot(TOKEN)

# Pozitif ve negatif kelimeler listelerini oluşturun
pozitif_kelimeler = ["harika", "güzel", "mükemmel", "iyi", "sevgi", "mutluluk", "başarılı", "gülümseme", "sevinç", "coşku", "şevkat", "iyimser", "olumlu", "ilham verici", "motivasyon", "enerjik", "heyecan verici", "umut", "rahatlık", "kendine güvenen", "şükran", "neşe", "tatmin", "güçlü", "sevgi dolu", "saygı", "hoş", "sadık", "samimi", "dürüst", "empati", "anlayışlı", "arkadaş canlısı", "sevecen", "şefkatli", "yararlı", "çözüm odaklı", "güvenilir", "şaşırtıcı", "inovatif", "akıllı", "yaratıcı", "eğlenceli", "dostane", "ilgi çekici", "zafer", "kaliteli", "dikkatli", "cesaret verici", "düşünceli", "huzur", "umut verici", "sıcakkanlı", "dostça", "hoşgörülü", "sabırlı", "paylaşımcı", "birleştirici", "güçlendirici", "gurur verici", "samimiyet", "bağışlama", "affetme", "özgüven", "iç huzur", "başarı", "saygın", "iyilik", "kendine saygı", "kararlılık", "kişisel gelişim", "öğrenme", "mükemmellik", "üretkenlik", "ilgi duyulan", "aydınlık", "iyimserlik", "hedef odaklı", "olumlu bakış açısı", "umutlu", "başarılı", "güzelim", "sevgiyle", "iyi niyetli", "hayranlık", "doğal", "içten", "minnettar", "verimli", "ilgili", "kaliteli zaman", "huzurlu", "ilham veren", "keyifli", "güzel bir gün", "güleryüzlü", "yetenekli", "akıllıca", "iyi hissetmek", "iyi davranış", "iyi niyet", "çözümleyici", "olumlu düşünmek", "olumlu duygular", "olumlu yönler", "olumlu sonuçlar", "olumlu etki", "mutlu son", "mutlu bir sonuç", "sevgi dolu bir kalp", "sevgi dolu bir yaklaşım", "sevgi dolu bir tavır", "içten bir yaklaşım", "içten bir tavır", "iyilik yapmak", "iyilikseverlik", "dürüstlük", "doğruluk"
"harika", "güzel", "mükemmel", "iyi", "sevgi", "mutluluk", "başarılı", "gülümseme", "sevinç", "coşku",
"şevkat", "iyimser", "olumlu", "ilham verici", "motivasyon", "enerjik", "heyecan verici", "umut", "rahatlık",
"kendine güvenen", "şükran", "neşe", "tatmin", "güçlü", "sevgi dolu", "saygı", "hoş", "sadık", "samimi",
"dürüst", "empati", "anlayışlı", "arkadaş canlısı", "sevecen", "şefkatli", "yararlı", "çözüm odaklı", "güvenilir",
"şaşırtıcı", "inovatif", "akıllı", "yaratıcı", "eğlenceli", "dostane", "ilgi çekici", "zafer", "kaliteli", "dikkatli",
"cesaret verici", "düşünceli", "huzur", "umut verici", "sıcakkanlı", "dostça", "hoşgörülü", "sabırlı", "paylaşımcı",
"birleştirici", "güçlendirici", "gurur verici", "samimiyet", "bağışlama", "affetme", "özgüven", "iç huzur", "başarı",
"saygın", "iyilik", "kendine saygı", "kararlılık", "kişisel gelişim", "öğrenme", "mükemmellik", "üretkenlik", "ilgi duyulan",
"aydınlık", "iyimserlik", "hedef odaklı", "olumlu bakış açısı", "umutlu", "başarılı", "güzelim", "sevgiyle", "iyi niyetli",
"hayranlık", "doğal", "içten", "minnettar", "verimli", "ilgili", "kaliteli zaman", "huzurlu", "ilham veren", "keyifli",
"güzel bir gün", "güleryüzlü", "yetenekli", "akıllıca", "iyi hissetmek", "iyi davranış", "iyi niyet", "çözümleyici", "olumlu düşünmek",
"olumlu duygular", "olumlu yönler", "olumlu sonuçlar", "olumlu etki", "mutlu son", "mutlu bir sonuç", "sevgi dolu bir kalp",
"sevgi dolu bir yaklaşım", "sevgi dolu bir tavır", "içten bir yaklaşım", "içten bir tavır", "iyilik yapmak", "iyilikseverlik",
"dürüstlük", "doğruluk"]
negatif_kelimeler = ["kötü","nefret","üzücü", "endişe verici", "karanlık", "hüzünlü", "sıkıcı", "bunaltıcı", "rahatsız edici", "gergin", "gerilimli",
"korkunç", "endişeli", "sıkıntılı", "yılgın", "karamsar", "umutsuz", "boşvermiş", "kızgın", "hırslı", "yıkıcı",
"zorlayıcı", "üzgün", "kaygılı", "endişeli", "kötümser", "acı", "huzursuz", "tehlikeli", "güvensiz", "gerilimli",
"sinirli", "yorgun", "kafası karışık", "şaşırmış", "heyecansız", "umutsuzca", "sevgisiz", "dikkatsiz", "ilgisiz",
"aptalca", "güçsüz", "başarısız", "yararsız", "güvensiz", "utanç verici", "utanç duyulan", "aşağılayıcı", "kırgın",
"kayıp", "yalnız", "yabancılaşmış", "umutsuz", "korkak", "tutsak", "dışlanmış", "hor görülmüş", "sıkıntı verici",
"boğucu", "talihsiz", "acınası", "belirsiz", "kötücül", "karanlık", "fırsatı kaçırmış", "mahvolmuş", "yıkılmış",
"kırılmış", "öfkeli", "yalnız", "soğuk", "iğrenç", "kötü niyetli", "yakıcı", "felaket", "hayal kırıklığı", "çaresiz",
"şok edici", "kayıp", "kaybetmek", "utanç verici", "utanmış", "alaycı", "mutsuz", "mecburiyet", "vazgeçmek",
"imkansız", "sorunlu", "kısır döngü", "sıkıntı", "kötüleşmek", "tehlikeli", "kötü bir şey", "itici", "kötü bir gün",
"negatif düşünmek", "negatif etki", "negatif hissetmek", "negatif sonuç", "negatif yön", "negatif duygu", "negatif tutum",
"negatif düşünce", "karamsarlık", "pesimizm", "karamsar bir bakış açısı", "mutsuz son", "üzüntü", "hoşnutsuzluk",
"şikayet", "üzücü haber", "negatif atmosfer", "tatsızlık", "hoşa gitmeyen", "moralli bozuk", "zor zamanlar", "sıkıntılı bir durum","kötü", "üzüntü", "acı", "keder", "stres", "sıkıntı", "endişe", "korku", "dehşet", "huzursuzluk",
"üzücü", "hüzünlü", "mahvolmuş", "kötüleşmiş", "çirkin", "rahatsız", "başarısız", "utanç", "suçlu",
"yalnız", "umutsuz", "depresif", "talihsiz", "karanlık", "kötümser", "düşmanca", "öfkeli", "hiddetli",
"agresif", "tehlikeli", "çirkin", "acımasız", "aşağılayıcı", "kıskanç", "aptalca", "yanıltıcı", "aldatıcı",
"sarsıntılı", "kötü niyetli", "şaşırtıcı", "işlevsiz", "sıkıcı", "utanç verici", "sahte", "sahtekar",
"zayıf", "düşük", "itici", "iğrenç", "kötü kokulu", "kaba", "gösterişli", "gereksiz", "güvensiz",
"şüpheci", "belirsiz", "endişeli", "isteksiz", "sıkıntılı", "stresli", "sıkıcı", "önemsiz", "sıkıcı",
"bıkkın", "aptalca", "anlamsız", "kayıp", "iç karartıcı", "soğuk", "umutsuzca", "unutulmuş", "vahşi",
"tekinsiz", "yalnızca", "ruhsuz", "çaresiz", "aşağılık", "başarısızlık", "ümitsiz", "karamsar", "boğucu",
"kısıtlayıcı", "sınırlayıcı", "dar", "sıkışık", "sıkı", "karanlık", "kirli", "bozuk", "tuhaf",
"anlaşılmaz", "kafa karıştırıcı", "yıkıcı", "zehirli", "acı verici", "kötü hissettiren", "ters",
"yalancı", "sahtekar", "yalnızca", "tatsız", "can sıkıcı", "boş", "anlamsız", "yavan", "sinir bozucu",
"belirsiz", "karamsarlık", "başarısızlık", "umutsuzluk", "halsizlik", "kaygı", "endişe", "gerginlik", "panik",
"intihar", "düşmanca", "suç", "terör", "cinayet", "ölüm", "kavga", "savaş", "acımasızlık", "sefalet",
"felaket", "katastrof", "çöküş", "bunalım", "baskı", "zorbalık", "tortura", "işkence"] 

# /start komutu geldiğinde çalışacak işlev
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Merhaba, ben bir Telegram botuyum. Nasıl yardımcı olabilirim?")

# /help komutu geldiğinde çalışacak işlev
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Size nasıl yardımcı olabilirim?")


# Mesaj alındığında çalışacak işlev
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Gelen mesajı küçük harflere çevirin
    text = message.text.lower()

    # Mesajın içerdiği pozitif ve negatif kelimeleri sayın
    pozitif_count = sum(text.count(kelime) for kelime in pozitif_kelimeler)
    negatif_count = sum(text.count(kelime) for kelime in negatif_kelimeler)

    # Pozitif kelime sayısı negatif kelime sayısından fazlaysa pozitif olarak kabul edin,
    # aksi halde negatif olarak kabul edin.
    if pozitif_count > negatif_count:
        bot.reply_to(message, "Bu mesaj pozitif bir duygu içeriyor.")
    elif negatif_count > pozitif_count:
        bot.reply_to(message, "Bu mesaj negatif bir duygu içeriyor.")
    else:
        bot.reply_to(message, "Bu mesaj nötr bir duygu içeriyor.")

# Botu çalıştırın
bot.polling()
