from django.contrib import admin

import events.models as event_models

admin.site.register(event_models.Event)
admin.site.register(event_models.TeamEvent)
