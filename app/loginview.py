#!/usr/bin/python3
from .loginmodel importLogin,User
from .rootview import getRoot
from .core.backend.soapbackend import JsonBackend
from .core.response import HttpResponse
from .core.Templates.template import SimpleTemplate,HtmlTemplate
from .templates.myTemplate import *

from . import settings
from .core.plugin.injected import Persistent
import json





