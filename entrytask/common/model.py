from __future__ import unicode_literals

from django.db import models


class CategoryTab(models.Model):
    category_name = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    category_photo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_tab'


class CommentTab(models.Model):
    create_time = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('UserTab', models.DO_NOTHING)
    event = models.ForeignKey('EventTab', models.DO_NOTHING)
    content = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment_tab'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class EventTab(models.Model):
    create_by = models.ForeignKey('UserTab', models.DO_NOTHING, db_column='create_by')
    create_time = models.IntegerField(blank=True, null=True)
    event_time = models.IntegerField(blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=2048, blank=True, null=True)
    category = models.ForeignKey(CategoryTab, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_tab'


class EventTagTab(models.Model):
    event = models.ForeignKey(EventTab, models.DO_NOTHING)
    tag = models.ForeignKey('TagTab', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'event_tag_tab'


class LikeTab(models.Model):
    create_time = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('UserTab', models.DO_NOTHING)
    event = models.ForeignKey(EventTab, models.DO_NOTHING)
    type = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'like_tab'


class ParticipantTab(models.Model):
    user = models.ForeignKey('UserTab', models.DO_NOTHING)
    event = models.ForeignKey(EventTab, models.DO_NOTHING)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'participant_tab'


class PhotoTab(models.Model):
    photo_url = models.CharField(max_length=255, blank=True, null=True)
    photo_content = models.CharField(max_length=255, blank=True, null=True)
    creat_time = models.IntegerField(blank=True, null=True)
    event = models.ForeignKey(EventTab, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'photo_tab'


class TagTab(models.Model):
    tag_name = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tag_tab'


class UserTab(models.Model):
    user_name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.IntegerField(blank=True, null=True)
    full_name = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.IntegerField(blank=True, null=True)
    user_type = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    salt = models.CharField(max_length=255, blank=True, null=True)
    avatar = models.CharField(max_length=255, blank=True, null=True)
    create_by = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_tab'