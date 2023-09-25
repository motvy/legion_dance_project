from django.contrib import admin

import messenger.models as messenger_models

admin.site.register(messenger_models.Chat)
admin.site.register(messenger_models.Message)
