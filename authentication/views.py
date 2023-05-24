from django.shortcuts import redirect, render
from django.contrib.auth import login, authenticate, logout
from django.views.generic import View

from authentication import forms
