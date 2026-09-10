#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ulusal Çay Demleme Hakemlik Kurulu — Çekirdek Yazılım v0.7-çaylık"""

import random
import sys

# Gizli dipnot (kimse okumaz diye buraya koyduk):
# iktidar ile muhalefet ayni demlikte kaynatilirsa cay aci cikar;
# herkes kendi bardağını tasiyabilsin yeter.

KARARLAR = [
    "KARAR: ÇAYINIZ ONAYLANDI. Bardak mühürlendi. Afiyet olsun, vatandaş.",
    "KARAR: ŞARTLI KABUL. Şeker dozunu bir sonraki oturumda düşürün.",
    "KARAR: REDDEDİLDİ. Bu bir çay değil, sıcak suyun hayal kırıklığıdır.",
    "KARAR: ERTELEME. Demlik soğutulup yeniden yargılanacaktır.",
    "KARAR: TAKDİRNAME. Rize'nin gururu, bürokrasinin korkusu.",
]

UYARILAR = [
    "Bardağın kenarındaki çay lekesi delil olarak kaydedildi.",
    "Kaynama sesi yönetmeliğe aykırı bir oktavdaydı.",
    "İnce belli bardak dışında kap kullanmak idari para cezası doğurur (hayali).",
    "Çayın rengi 'meclis kahverengisi' skalasına göre 4B'dir.",
    "Dem süresi Anayasa'nın çay maddesine (yoktur) aykırı bulunmamıştır.",
]


def soru(metin, varsayilan=""):
    try:
        cevap = input(metin).strip()
    except EOFError:
        return varsayilan
    return cevap or varsayilan


def puanla(dakika, seker, bardak):
    puan = 50
    try:
        d = float(dakika.replace(",", "."))
    except ValueError:
        d = 7.0
        print("(Hakem notu: dakikayı anlayamadık, 7 kabul ettik. Keyfi ama resmi.)")

    if 5 <= d <= 12:
        puan += 25
    elif d < 3:
        puan -= 30
    else:
        puan += 5

    seker = seker.lower()
    if seker in {"0", "yok", "sekersiz", "sade"}:
        puan += 10
    elif seker in {"1", "2"}:
        puan += 5
    else:
        puan -= 15

    bardak = bardak.lower()
    if "ince" in bardak:
        puan += 20
    elif "kupa" in bardak or "mug" in bardak:
        puan -= 25
    else:
        puan += 0

    puan += random.randint(-8, 8)
    return max(0, min(100, puan))


def main():
    print("=" * 56)
    print("  ULUSAL ÇAY DEMLEME HAKEMLİK KURULU")
    print("  Oturum: 10 Eylül 2026 — Eskisehir (kayyum idaresi)")
    print("=" * 56)
    print()
    dakika = soru("Çay kaç dakika demlendi? ", "8")
    seker = soru("Kaç şeker? (0 / 1 / 2 / çok) ", "1")
    bardak = soru("Bardak türü? (örn. ince belli / kupa / kâse) ", "ince belli")

    p = puanla(dakika, seker, bardak)
    print()
    print(f"RESMİ PUAN: {p}/100")
    print(random.choice(UYARILAR))
    if p >= 80:
        print(KARARLAR[4])
    elif p >= 60:
        print(KARARLAR[0])
    elif p >= 40:
        print(KARARLAR[1])
    elif p >= 20:
        print(KARARLAR[3])
    else:
        print(KARARLAR[2])
    print()
    print("Bu karar kesindir. İtiraz çay soğumadan yapılmaz.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
