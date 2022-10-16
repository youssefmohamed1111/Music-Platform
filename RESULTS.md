- create some artists:
  from artists.models import Artists
  a1 = Artists.objects.create(stageName ="Tyler",socialLinkField = "https://www.instagram.com/feliciathegoat/?igshid=YmMyMTA2M2Y%3D")
  a2 = Artists.objects.create(stageName ="Billie",socialLinkField = "https://instagram.com/billieeilish?igshid=YmMyMTA2M2Y=")
  a3 = Artists.objects.create(stageName ="Labrinth",socialLinkField = "https://www.instagram.com/labrinth/?igshid=YmMyMTA2M2Y%3D")

---

- list down all artists:
  Artists.objects.all()
  <QuerySet [<Artists: Artists object (1)>, <Artists: Artists object (2)>, <Artists: Artists object (3)>]>

---

- list down all artists sorted by name
  Artists.objects.all().order_by("stageName")
  <QuerySet [<Artists: Artists object (2)>, <Artists: Artists object (3)>, <Artists: Artists object (1)>]>

---

- list down all artists whose name starts with `a`
  Artists.objects.all().filter(stageName\_\_startswith='a')

---

- in 2 different ways, create some albums and assign them to any artists

---

- get the latest released album
  Albums.objects.all().order_by("releaseDateTime").reverse()[0]

---

- get all albums released before today
  from django.utils import timezone Album.objects.all().filter(release_datetime\_\_lt=timezone.now())

---

- get all albums released today or before but not after today
  Albums.objects.all().filter(release_datetime\_\_lte=timezone.now())

---

- count the total number of albums
  Albums.objects.count()

---

- in 2 different ways, for each artist, list down all of his/her albums

---

- list down all albums ordered by cost then by name (cost has the higher priority)
  Albums.objects.all().order_by("cost","Name")

---
