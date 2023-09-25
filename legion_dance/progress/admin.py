from django.contrib import admin

import progress.models as progress_models

admin.site.register(progress_models.Achievement)
admin.site.register(progress_models.UserAchievement)
