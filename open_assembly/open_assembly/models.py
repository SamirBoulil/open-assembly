from django.db import models

# Create your models here.

class Deputy(models.Model):
    """ Model linked to concrete data table
    """
    id = models.AutoField(primary_key=True)
    uid = models.TextField(unique=True)
    name = models.TextField()
    surname = models.TextField()
    slug = models.TextField()
    sex = models.TextField()
    mail = models.TextField()
    birth_date = models.TextField()
    birth_town = models.TextField()
    birth_department = models.TextField()
    birth_country = models.TextField()
    work_name = models.TextField()
    work_category = models.TextField()
    work_familly = models.TextField()

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
    id = models.AutoField(primary_key=True)
    uid = models.TextField(unique=True)
    start_date = models.TextField()
    seat_number = models.TextField()
    election_cause = models.TextField()
    legislature = models.TextField()
    deputy = models.ForeignKey(Deputy, related_name='mandates')
    circonscription = models.ForeignKey(Circonscription, related_name='mandates')

    def __str__(self):
        return "%s %s %s" % (self.seat_number, self.legislature, self.election_cause)

class Vote:
    """ A deputy votes on a Decree with a Mandate
    """
    id = models.AutoField(primary_key=True)
    session_ref = models.TextField()
    legislature = models.TextField()
    vote_date = models.DateField()
    number_people_voting = models.IntegerField()
    number_votes = models.IntegerField()
    number_votes_no = models.IntegerField()
    number_votes_yes = models.IntegerField()
    number_votes_not_voting = models.IntegerField()
    result = models.IntegerField()

class Decree:
    """ Decree information
    """
    id = models.AutoField(primary_key=True)
    title = models.TextField()
    proposed_by = models.TextField()



