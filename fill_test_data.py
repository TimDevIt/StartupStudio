import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StartupStudio.settings')
django.setup()

from core.models import Direction, Skill,EventType


if not EventType.objects.all():
    EventType.objects.create(event_type_name='ВКР')
    EventType.objects.create(event_type_name='Хакатон')
    EventType.objects.create(event_type_name='Конференция')
    EventType.objects.create(event_type_name='Курс')

if not Direction.objects.all():
    Direction.objects.create(direction_name='ИТ')
    Direction.objects.create(direction_name='Физика')
    Direction.objects.create(direction_name='Химия')

if not Skill.objects.all():
    it_direction = Direction.objects.get(direction_name='ИТ')
    Skill.objects.create(skill_name='Python', direction=it_direction)
    Skill.objects.create(skill_name='Java', direction=it_direction)
    Skill.objects.create(skill_name='C++', direction=it_direction)
    phys_direction  = Direction.objects.get(direction_name='Физика')
    Skill.objects.create(skill_name='Test1', direction=phys_direction)
    Skill.objects.create(skill_name='Test2', direction=phys_direction)
    Skill.objects.create(skill_name='Test3', direction=phys_direction)
print("Skills and Directions created")