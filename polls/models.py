import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

class grade(models.Model):

    year=models.CharField(_("년도"), max_length=255)
    semester=models.CharField(_("학기"), max_length=255)
    classify=models.CharField(_("이수구분"), max_length=255)
    codenum=models.CharField(_("학수번호"), max_length=255)
    namee=models.CharField(_("과목명"), max_length=255)
    credit=models.CharField(_("학점"), max_length=255)
