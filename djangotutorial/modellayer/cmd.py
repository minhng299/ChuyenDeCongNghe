from modellayer.models import Fruit, Group, Membership, Person
import datetime
p = Person(name="Fred Flintstone", shirt_size="L")
p.save()
p.shirt_size
p.get_shirt_size_display()

fruit = Fruit.objects.create(name="Apple")
fruit.name = "Pear"
fruit.save()
Fruit.objects.values_list("name", flat=True)


ringo = Person.objects.create(name="Ringo Starr")
paul = Person.objects.create(name="Paul McCartney")
beatles = Group.objects.create(name="The Beatles")
m1 = Membership(
     person=ringo,
     group=beatles,
     date_joined=datetime.date(1962, 8, 16),
     invite_reason="Needed a new drummer.",
 )
m1.save()
beatles.members.all()
ringo.group_set.all()
m2 = Membership.objects.create(
     person=paul,
     group=beatles,
     date_joined=datetime.date(1960, 8, 1),
     invite_reason="Wanted to form a band.",
 )
beatles.members.all()


Membership.objects.create(
person=ringo,
group=beatles,
date_joined=datetime.date(1968, 9, 4),
invite_reason="You've been gone for a month and we miss you.",
)
beatles.members.all()
beatles.members.remove(ringo)
beatles.members.all()

Group.objects.filter(members__name__startswith="Paul")

Person.objects.filter(group__name="The Beatles", membership__date_joined__gt=datetime.date(1961, 1, 1))

ringos_membership = Membership.objects.get(group=beatles, person=ringo)
ringos_membership.date_joined
datetime.date(1962, 8, 16)
ringos_membership.invite_reason 