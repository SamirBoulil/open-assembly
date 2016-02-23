from django.db import models

class Group(models.Model):
    id = models.TextField(primary_key=True)
    name = models.TextField()


class Deputy(models.Model):
    """ Model linked to concrete data table
    """
    id = models.TextField(primary_key=True)
    name = models.TextField()
    surname = models.TextField()
    slug = models.TextField()
    sex = models.TextField()
    mail = models.TextField()
    birth_date = models.DateField()
    birth_town = models.TextField()
    birth_department = models.TextField(blank=True, null=True)
    birth_country = models.TextField(blank=True, null=True)
    work_name = models.TextField(blank=True, null=True)
    work_category = models.TextField(blank=True, null=True)
    work_familly = models.TextField(blank=True, null=True)
    group = models.ForeignKey(Group, related_name='deputies', blank=True, null=True)

    def __str__(self):
        return "%s %s" % (self.name, self.surname)


class Circonscription(models.Model):
    """ A mandate is practised on a circo / department
    """
    id = models.AutoField(primary_key=True)
    num_circo = models.TextField()
    num_department = models.TextField()
    department = models.TextField()
    region = models.TextField()

    def __str__(self):
        return "%s %s %s" % (""+self.num_circo, self.department, self.region)


class Mandate(models.Model):
    """ A deputy has a mandate.
    """
    id = models.TextField(primary_key=True)
    start_date = models.DateField()
    seat_number = models.TextField()
    election_cause = models.TextField()
    legislature = models.TextField()
    deputy = models.ForeignKey(Deputy, related_name='mandates')
    circonscription = models.ForeignKey(Circonscription, related_name='mandates')

    def __str__(self):
        return "%s %s %s" % (self.seat_number, self.legislature, self.election_cause)


class Poll(models.Model):
    """ Decree information
    """
    id = models.TextField(primary_key=True)
    title = models.TextField()
    asked_by = models.TextField()
    poll_date = models.DateField()
    session_ref = models.TextField()
    sceance_ref = models.TextField()
    is_accepted = models.BooleanField()
    legislature = models.TextField()
    number_people_voting = models.IntegerField()
    number_votes_made = models.IntegerField()
    number_votes_required = models.IntegerField()
    number_votes_no = models.IntegerField()
    number_votes_yes = models.IntegerField()
    number_votes_dk = models.IntegerField()
    number_votes_not_voting = models.IntegerField()


class Vote(models.Model):
    """ A deputy votes on a Decree with a Mandate
    """
    id = models.AutoField(primary_key=True)
    decision = models.IntegerField() #0:no 1:OK 2:Abs 3:Not voting
    poll = models.ForeignKey(Poll, related_name="votes")
    mandate = models.ForeignKey(Mandate, related_name="votes")
    deputy = models.ForeignKey(Deputy, related_name="votes")

