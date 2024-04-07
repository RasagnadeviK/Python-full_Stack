from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from random import randint
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from random import randint
