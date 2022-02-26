yazi = 'Kullanıcı Giriş Kısmına Hoşgeldiniz'
print(yazi.center(50,'*'))
kullanici_Adi = 'yunus'
sifre = '1234'

while True:
    kullanici_Ad = input('Kullanıcı adınızı giriniz: ')
    k_Sifre = input('Şifrenizi giriniz: ')
    if(kullanici_Adi == kullanici_Ad and sifre == k_Sifre):
        print(f'Hoşgeldiniz {kullanici_Ad}')
        break
    else:
        print('Kullanıcı adı veya şifre yanlış')