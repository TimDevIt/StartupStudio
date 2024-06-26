# Generated by Django 4.2 on 2024-04-18 11:10
from django.db import migrations


def add_guest_group(apps, schema_editor):
    groups = apps.get_model("auth", "Group")
    permissions = apps.get_model("auth", "Permission")
    guest_account = groups.objects.create(
        name="Гостевой аккаунт"
    )

    view_news_perm = permissions.objects.get(codename="view_newsarticle")
    view_projects_perm = permissions.objects.get(codename="view_project")
    view_project_detail_perm = permissions.objects.get(codename="can_view_project_details")
    guest_account.permissions.add(view_news_perm.id, view_projects_perm.id, view_project_detail_perm.id)

def add_authorized_user_group(apps, schema_editor):
    groups = apps.get_model("auth", "Group")
    permissions = apps.get_model("auth", "Permission")
    authorized_user = groups.objects.create(
        name="Авторизованный пользователь"
    )
    #Разрешения на работу с профилем
    profile_perm = permissions.objects.filter(name__contains="profile")
    #Разрешения на работу с новостями
    view_news_perm = permissions.objects.get(codename="view_newsarticle")
    # Разрешения на работу с проектами
    view_projects_perm = permissions.objects.get(codename="view_project")
    create_project_perm = permissions.objects.get(codename="can_create_projects")
    enter_project_perm = permissions.objects.get(codename="can_enter_projects")
    view_project_detail_perm = permissions.objects.get(codename="can_view_project_details")
    can_add_chat_mes_perm = permissions.objects.get(codename="add_projectchatmessage")
    can_view_chat_mes_perm = permissions.objects.get(codename="view_projectchatmessage")
    can_view_project_entry_perm = permissions.objects.get(codename="view_projectentry")
    can_change_project_entry_perm = permissions.objects.get(codename="change_projectentry")
    authorized_user.permissions.set(profile_perm)
    authorized_user.permissions.add(view_news_perm.id, view_projects_perm.id, create_project_perm.id, enter_project_perm.id,
                                    view_project_detail_perm.id, can_add_chat_mes_perm.id, can_view_chat_mes_perm.id,
                                    can_view_project_entry_perm.id, can_change_project_entry_perm.id)

def add_moderator_group(apps, schema_editor):
    groups = apps.get_model("auth", "Group")
    permissions = apps.get_model("auth", "Permission")
    moderator = groups.objects.create(
        name="Модератор"
    )
    #Разрешения на работу с новостями
    view_news_perm = permissions.objects.get(codename="view_newsarticle")
    add_news_perm = permissions.objects.get(codename="add_newsarticle")
    can_create_new_news_perm = permissions.objects.get(codename="create_new_news")
    # Разрешения на работу с проектами
    can_moderate_projects_perm = permissions.objects.get(codename="can_moderate_projects")

    moderator.permissions.add(view_news_perm.id, add_news_perm.id, can_create_new_news_perm.id,
                              can_moderate_projects_perm.id)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_alter_project_options_alter_project_pub_date_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('NewsFeed', '0027_alter_newsarticle_pub_date'),
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_guest_group, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(add_authorized_user_group, reverse_code=migrations.RunPython.noop),
        migrations.RunPython(add_moderator_group, reverse_code=migrations.RunPython.noop)
    ]
