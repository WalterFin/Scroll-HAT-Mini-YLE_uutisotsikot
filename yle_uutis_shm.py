import time

try:
    import feedparser
except:
    print("Asenna feederparser komennolla: sudo pip install feedparser")
    quit()
try:
    import scrollphathd
except:
    print("Asenna scrollphathd kirjasto komennolla: sudo apt-get install python3-scrollphathd")
    quit()


print("CTRL+C lopettaa ohjelman.")
while True:
    #RSS osoite
    print("Ladataan RSS-syötettä.")
    feed = feedparser.parse("https://feeds.yle.fi/uutiset/v1/majorHeadlines/YLE_UUTISET.rss")
    #asetetaan kirkkaus (0.1-1)
    kirkkaus = 0.2

    feed_entries = feed.entries
    otsikot = []

    for entry in feed.entries:
        article_title = entry.title
        otsikko = "{}".format(article_title)
        #otsikoiden lisääminen tauluun
        otsikot.append(otsikko)

    #otsikon tulostus taulusta scrollhatminillä
    for i in otsikot:
        scrollphathd.write_string(" " + i, brightness=kirkkaus)
        #lasketaan otsikon esitysaika (tekstin pituus x 0.6s)
        esitysaika = len(i) * 0.6
        #määritetään otsikon tulostuksen lopetusaika
        lopetusaika = time.time() + esitysaika
        while True:
            scrollphathd.show()
            scrollphathd.scroll()
            # odotetaan 0.08s
            time.sleep(0.08)
            #tekstin esittämisen lopettaminen ja näytön pyyhkiminen
            if lopetusaika <= time.time():
                scrollphathd.clear()
                time.sleep(2)
                break
