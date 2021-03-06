# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin
from filer.fields.image import FilerImageField

from djangocms_social.models import likes
from djangocms_social import defaults


class Like(CMSPlugin):
    facebook = models.BooleanField(_('facebook'), default=False)
    google = models.BooleanField(_('google'), default=False)
    twitter = models.BooleanField(_('twitter'), default=False)
    pinterest = models.BooleanField(_('pinterest'), default=False)
    email = models.BooleanField(_('email'), default=False)

    # options
    title = models.CharField(_('title'), max_length=255, default=defaults.LIKE['title'], blank=True, null=True,
        help_text=_('Uses the title of the browser window if empty.'))
    description = models.CharField(_('description'), max_length=255, default=defaults.LIKE['description'],
        blank=True, null=True)
    image = FilerImageField(verbose_name=_('image'), blank=True, null=True,
        help_text=_('This setting can only be set once per page. If set twice, it will be overridden.'))

    def __init__(self, *args, **kwargs):
        super(Like, self).__init__(*args, **kwargs)
        self.options = likes.AVAILABLE

    def get_objects(self):
        objects = []
        for type, object in self.options.iteritems():
            if getattr(self, type, False):
                objects.append(getattr(likes, object)(**self.get_kwargs()))
        return objects

    def get_kwargs(self):
        kwargs = {
            'title': self.title,
            'description': self.description,
        }
        return kwargs


class Mail(CMSPlugin):
    subject = models.CharField(_('subject'), max_length=100)
    body = models.TextField(_('body'), default='', blank=True)
    append_url = models.BooleanField(_('append url'), default=True,
        help_text=_('Append the current web address at the end of the mail.'))


class Links(CMSPlugin):
    facebook = models.URLField(_('facebook'), null=True, blank=True)
#    googleplus = models.URLField(_('google plus'), null=True, blank=True)
    twitter = models.URLField(_('twitter'), null=True, blank=True)
    xing = models.URLField(_('xing'), null=True, blank=True)
    linkedin = models.URLField(_('linkedin'), null=True, blank=True)
#    youtube = models.URLField(_('youtube'), null=True, blank=True)
    rss = models.URLField(_('rss'), null=True, blank=True)

    links = [
        'facebook', 'twitter', 'xing', 'linkedin', 'rss',
    ]