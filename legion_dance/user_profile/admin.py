from django.contrib import admin

import user_profile.models as profile_models

admin.site.register(profile_models.User)
admin.site.register(profile_models.Team)
