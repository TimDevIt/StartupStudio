import os
import django


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'StartupStudio.settings')
django.setup()


from django.contrib.auth.models import Group, Permission

def add_guest_group():
    guest_account = Group.objects.create(name="Гостевой аккаунт")
    view_news_perm = Permission.objects.get(codename="view_newsarticle")
    view_projects_perm = Permission.objects.get(codename="view_project")
    view_project_detail_perm = Permission.objects.get(codename="can_view_project_details")
    guest_account.permissions.add(view_news_perm, view_projects_perm, view_project_detail_perm)

def add_authorized_user_group():
    authorized_user = Group.objects.create(name="Авторизованный пользователь")
    profile_perm = Permission.objects.filter(name__contains="profile")
    view_news_perm = Permission.objects.get(codename="view_newsarticle")
    view_projects_perm = Permission.objects.get(codename="view_project")
    create_project_perm = Permission.objects.get(codename="can_create_projects")
    enter_project_perm = Permission.objects.get(codename="can_enter_projects")
    view_project_detail_perm = Permission.objects.get(codename="can_view_project_details")
    can_add_chat_mes_perm = Permission.objects.get(codename="add_projectchatmessage")
    can_view_chat_mes_perm = Permission.objects.get(codename="view_projectchatmessage")
    can_view_project_entry_perm = Permission.objects.get(codename="view_projectentry")
    can_change_project_entry_perm = Permission.objects.get(codename="change_projectentry")
    authorized_user.permissions.set(profile_perm)
    authorized_user.permissions.add(view_news_perm, view_projects_perm, create_project_perm, enter_project_perm,
                                    view_project_detail_perm, can_add_chat_mes_perm, can_view_chat_mes_perm,
                                    can_view_project_entry_perm, can_change_project_entry_perm)

def add_moderator_group():
    moderator = Group.objects.create(name="Модератор")
    view_news_perm = Permission.objects.get(codename="view_newsarticle")
    add_news_perm = Permission.objects.get(codename="add_newsarticle")
    can_create_new_news_perm = Permission.objects.get(codename="create_new_news")
    can_moderate_projects_perm = Permission.objects.get(codename="can_moderate_projects")
    moderator.permissions.add(view_news_perm, add_news_perm, can_create_new_news_perm, can_moderate_projects_perm)


if __name__ == "__main__":
    add_guest_group()
    add_authorized_user_group()
    add_moderator_group()
    print("Groups created!")