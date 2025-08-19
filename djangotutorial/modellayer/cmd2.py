from modellayer.models import Blog, Entry, Author
import datetime
b = Blog(name="Beatles Blog", tagline="All the latest Beatles news.")
b.save()

entry = Entry.objects.get(pk=1)
cheese_blog = Blog.objects.get(name="Beatles Blog")
entry.blog = cheese_blog
entry.save()

joe = Author.objects.create(name="Joe")
entry.authors.add(joe)
john = Author.objects.create(name="John")
paul = Author.objects.create(name="Paul")
george = Author.objects.create(name="George")
ringo = Author.objects.create(name="Ringo")
entry.authors.add(john, paul, george, ringo)

Entry.objects.filter(headline__startswith="What").exclude(pub_date__gte=datetime.date.today()).filter(pub_date__gte=datetime.date(2005, 1, 30))


q1 = Entry.objects.filter(headline__startswith="What")
q2 = q1.exclude(pub_date__gte=datetime.date.today())
q3 = q1.filter(pub_date__gte=datetime.date.today())

q = Entry.objects.filter(headline__startswith="What")
q = q.filter(pub_date__lte=datetime.date.today())
q = q.exclude(body_text__icontains="food")
print(q)