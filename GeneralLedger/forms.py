

class Form(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'first_name', 'last_name', 'email', 'username', 'phone', 'national_id', 'password1', 'password2',)