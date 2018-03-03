from flickrapi import FlickrAPI
import urllib
import random
import yagmail

people = {'werner':'werner.hofmeester@gmail.com',
          'chef': 'david.m.berenstein@gmail.com',
          'gerrie': 'joostvanthiel@gmail.com',
          'rossi': 'ttjanssens@gmail.com',
          'rick':'rickvannobelen@gmail.com',
          'max':'maxkonings23@gmail.com',
          'arjen':'a.franken1710@gmail.com',
          'frank':'v.f.rutgers@gmail.com',
          'simon':'simon.riezebos@gmail.com',
          'luc':'lucjacobs341@gmail.com',
          'joost': 'joost.vrijhoef@gmail.com',
          'thomas': 't.h.v.haperen@gmail.com',
          'brouwer': 'j.h.j.brouwer87@gmail.com',
          'sander': 'a.t.goessens@gmail.com',
          'ralf': 'ralf.stamps@gmail.com',
          'job': 'jobvisserhcm@gmail.com',
          'timo': 'vandooremaal21@gmail.com'}

def send_mail(tag):
    try:
        recipient = people[tag]
    except:
        return None

    FLICKR_PUBLIC = '9c77a2340902c0b57cb88783a9624413'
    FLICKR_SECRET = 'b1dfea578f9da931'

    flickr = FlickrAPI(FLICKR_PUBLIC, FLICKR_SECRET, format='parsed-json')
    extras='url_o'

    sort_type = ['date-posted-asc', 'date-posted-desc', 'date-taken-asc', 'date-taken-desc', 'interestingness-desc', 'interestingness-asc', 'relevance']
    random.shuffle(sort_type)

    try:
        Fellow = flickr.photos.search(tags=tag, user_id='88703693@N00', extras=extras, sort=sort_type[0])
        photos = Fellow['photos']
        randomphoto = random.randint(1, int(photos['total'])-1)

        image = urllib.request.urlretrieve(photos['photo'][randomphoto]['url_o'], "throwback.jpg")
        body = 'Jupiter throwback voor ' + tag

        yag = yagmail.SMTP('abhinav.bhatnagar.91@gmail.com', 'hinderbot123')
        yag.send(to = recipient, subject = 'throwback', contents = [body, 'throwback.jpg'])

        return 'mail send'
    except:
        return None
