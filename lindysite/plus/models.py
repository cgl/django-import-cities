from django.db import models
from location.models import City
from django.contrib.auth.models import User

DANCE_TYPE_CHOICES = (
            ('LH', 'Lindy Hop'),
            ('BL', 'Blues'),
            ('BB', 'Balboa'),
            ('SJ', 'Solo Jazz'),
            ('CS', 'Collegiate Shag'),
            ('WC', 'West Coast Swing'),
            ('BW', 'Boogie Woogie'),
    )

class BaseModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(editable=False, default=False, verbose_name='Deleted')
    class Meta:
        abstract = True

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    city = models.ForeignKey(City)
    image = models.ImageField(null=True, blank=True, verbose_name="person_image")
    slug = models.SlugField(unique=True)
    date_of_birth = models.DateField(null=True, blank=True)

    SEX_TYPE_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('U', 'Unspecified'),
    )
    sex = models.CharField(max_length=2,choices=SEX_TYPE_CHOICES,default="F")
    email = models.EmailField(max_length=30,unique=True)
    mobile_phone = models.CharField(max_length=30)
    user = models.ForeignKey(User)

    def __str__(self):
        return "%s %s" %(self.first_name,self.last_name)

    def fullname(self):
        return "%s %s" %(self.person.first_name,self.person.last_name)

class Teacher(models.Model):
    person = models.OneToOneField(Person,related_name="teacher_prsn")
    TEACHER_TYPE_CHOICES = (
        ('Loc', 'Local'),
        ('Int', 'International'),
    )

    type = models.CharField(max_length=3,choices=TEACHER_TYPE_CHOICES,default="Int")
    image = models.ImageField(null=True, blank=True, verbose_name="teacher_image")
    present_city = models.ForeignKey(City,related_name="teacher_present_city")

    first_speciality = models.CharField(max_length=2,choices=DANCE_TYPE_CHOICES,default="LH")
    second_speciality = models.CharField(max_length=2,choices=DANCE_TYPE_CHOICES, blank=True)
    third_speciality = models.CharField(max_length=2,choices=DANCE_TYPE_CHOICES, blank=True)
    ## The dance types that the teacher specializes
    short_description = models.TextField(max_length=600, null=True, blank=True)
    claimed = models.BooleanField(default=False)
    open_to_private = models.BooleanField(default=False)
    ## Does the teacher want to give private lessons
    require_private_confirmation = models.BooleanField(default=True)
    ## Does teacher want to approve and confirm each of the requests that arrive for her
    ## free private slots in the calendar.
    ## This may slow down the process and may cause an extra burden for the teacher.
    def fullname(self):
        return "%s %s" %(self.person.first_name,self.person.last_name)
    def name(self):
        return self.person.first_name
    def __str__(self):
        return "%s %s" %(self.person.first_name,self.person.last_name)
    youtube_video1 = models.CharField(max_length=11, null=True,blank=True)
    youtube_video2 = models.CharField(max_length=11, null=True,blank=True)
    likes = models.ManyToManyField(User,through="LikesTeacher", related_name="like_teacher")
    follows = models.ManyToManyField(User,through="FollowsTeacher", related_name="follow_teacher")


class Event(BaseModel):
    name = models.CharField(max_length=100,unique=True)
    image = models.ImageField(null=True, blank=True, verbose_name="event_image")
    slug = models.SlugField(unique=True)
    start_date = models.DateField()
    end_date = models.DateField()
    is_published = models.BooleanField(default=False)
    slogan = models.CharField(max_length=100,blank=True)
    short_description = models.TextField(max_length=600, null=True, blank=True)

    REGISTRATION_CHOICES = (
        ('Op', 'Open'),
        ('Cl', 'Closed'),
        ('Su', 'Suspended'),
        ('Ca', 'Cancelled'),
        ('So', 'Completely Sold Out'),
    )
    reg_status = models.CharField(max_length=2,choices=REGISTRATION_CHOICES,default="Cl")

    EVENT_TYPE_CHOICES = (
        ('Ws', 'Workshop'),
        ('Ex', 'Exchange'),
        ('Dc', 'Dance Camp'),
        ('Co', 'Concert'),
        ('We', 'Weekend'),
    )
    type = models.CharField(max_length=2,choices=EVENT_TYPE_CHOICES,default="Ws")
    city = models.ForeignKey(City)
    website = models.URLField(null=True,blank=True)
    fb_page = models.URLField(null=True,blank=True)
    fb_event = models.URLField(null=True,blank=True)
    fb_event_id = models.CharField(max_length=18,blank=True)
    #dance_type = models.ManyToManyField(DanceType,blank=True)

    teachers = models.ManyToManyField(Teacher,blank=True,through='TeachesInEvent')

    organizer1 = models.ForeignKey(Person, related_name="event_organizer1")
    organizer2 = models.ForeignKey(Person, related_name="event_organizer2",null=True, blank=True)
    organizer3 = models.ForeignKey(Person, related_name="event_organizer3",null=True, blank=True)
    company = models.CharField(max_length=100,blank=True)

    #bands = models.ManyToManyField(Band,blank=True, related_name="bands")
    #djs = models.ManyToManyField(Dj,blank=True,related_name="djs")
    #special_guests = models.ManyToManyField(SpecialGuest,blank=True,related_name="special_guests")
    #mc = models.ManyToManyField(Mc,blank=True,related_name="mc")
    claimed = models.BooleanField(default=False)
    SOURCE_OF_INFO = (
        ('LP', 'LindyPlus Crawler'),
        ('EO', 'Event Owner'),
        ('SE', 'Suggested Event'),
    )
    info_source = models.CharField(max_length=2,choices=SOURCE_OF_INFO,default="LP")
    likes = models.ManyToManyField(User,through="LikesEvent", related_name="like_event")
    follows = models.ManyToManyField(User,through="FollowsEvent", related_name="follow_event")


    def __str__(self):
        return self.name

    def past_event(self):
        return self.end_date <= timezone.now().date() - datetime.timedelta(days=1)
    past_event.admin_order_field = 'end_date'
    past_event.boolean = True
    past_event.short_description = 'coming event?'

    class Meta:
        ordering = ["-start_date"]

    def get_absolute_url(self):
        from django.core.urlresolvers import reverse
        return reverse('plus.views.core.event_details', args=[str(self.id)])

class LikesTeacher(models.Model):
    user = models.ForeignKey(User)
    teacher = models.ForeignKey(Teacher)
    create_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (("user", "teacher"),)

class FollowsTeacher(models.Model):
    user = models.ForeignKey(User)
    teacher = models.ForeignKey(Teacher)
    create_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (("user", "teacher"),)

class LikesEvent(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    create_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (("user", "event"),)

class FollowsEvent(models.Model):
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    create_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together = (("user", "event"),)

class DanceType(models.Model):
    image = models.ImageField(null=True, blank=True, verbose_name="dance_type_image")
    dancetype = models.CharField(max_length=30,unique=True)

    slug = models.SlugField()
    def __str__(self):
        return self.dancetype

class TeachesInEvent(models.Model):
    teacher = models.ForeignKey(Teacher)
    event = models.ForeignKey(Event)
    dance_type = models.ManyToManyField(DanceType,blank=True)
    def __str__(self):
        return "%s %s %s" %(self.teacher,self.event,self.dance_type)
