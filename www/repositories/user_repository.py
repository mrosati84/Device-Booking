from www.models import User

class UserRepository():
    def get_by_pk(self, pk):
        return User.objects.get(pk=pk)

    def get_by_last_name(self, last_name):
        return User.objects.filter(last_name__contains=last_name).order_by('last_name')
