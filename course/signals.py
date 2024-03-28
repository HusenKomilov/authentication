from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.db.models import Avg

from course.models import FeedBack, Lesson

# from moviepy.editor import VideoFileClip


@receiver(post_save, sender=FeedBack)
def update_course_rating(sender, instance, **kwargs):
    avg_stars = FeedBack.objects.filter(course=instance.course).aggregate(Avg("stars"))
    instance.course.rating = avg_stars.get("stars__avg")
    instance.course.save()


# @receiver(pre_save, sender=Lesson)
# def update_lesson_duration(sender, instance, **kwargs):

#     clip = VideoFileClip(instance.video.path)
#     duration = clip.duration
#     instance.video_duration = int(duration)
#     return instance
