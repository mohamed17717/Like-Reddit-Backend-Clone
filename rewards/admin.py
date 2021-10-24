from django.contrib import admin

from .models import Reward
from .models import RewardTodoAction
from .models import UserAction
from .models import UserReward
from .models import UserTotalPoints
from .models import RewardPossibleFeature
from .models import RewardFeature


admin.site.register(Reward)
admin.site.register(RewardTodoAction)
admin.site.register(UserAction)
admin.site.register(UserReward)
admin.site.register(UserTotalPoints)
admin.site.register(RewardPossibleFeature)
admin.site.register(RewardFeature)

