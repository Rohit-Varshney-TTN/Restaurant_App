from django.db .models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User , UserProfile

@receiver(post_save,sender=User)
def post_save_create_profile_receiver(sender, instance , created , **kwargs):
    print(created)
    if created :
        UserProfile.objects.create(user=instance)
        print('User Profile is created')
    else:
        try:
            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # create the user profile if not exists
            UserProfile.objects.create(user = instance)
            print('Profile was not exists , but I created One ')
        print('User is modified')

# post_save.connect(post_save_create_profile_receiver, sender=User)
@receiver(pre_save,sender=User)
def pre_save_profile_receiver(sender , instance , **kwargs):
    print(instance.username,'This user is being saved ')