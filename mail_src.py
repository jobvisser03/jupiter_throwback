from flickrapi import FlickrAPI
import urllib
import random
import yagmail
import credentials

people = credentials.people
flickr = FlickrAPI(credentials.FLICKR_PUBLIC, credentials.FLICKR_SECRET, format='parsed-json')

def send_mail(tag):
    try:
        recipient = people[tag]
    except:
        return None

    extras='url_o'

    sort_type = ['date-posted-asc', 'date-posted-desc', 'date-taken-asc', 'date-taken-desc', 'interestingness-desc', 'interestingness-asc', 'relevance']
    random.shuffle(sort_type)

    try:
        Fellow = flickr.photos.search(tags=tag, user_id='88703693@N00', extras=extras, sort=sort_type[0])
        photos = Fellow['photos']
        randomphoto = random.randint(1, int(photos['total'])-1)

        image = urllib.request.urlretrieve(photos['photo'][randomphoto]['url_o'], "throwback.jpg")
        body = 'Jupiter throwback voor ' + tag

        yag = yagmail.SMTP(credentials.mail_address, credentials.mail_password)
        yag.send(to = recipient, subject = 'throwback', contents = [body, 'throwback.jpg'])

        return 'mail send'
    except:
        return None
