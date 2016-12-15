from django import forms
from userprofile.models import UserProfile


class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('gender', 'name', 'age', 'pic', 'follow_tags',
                  'college', 'mobile', 'bio', 'address')
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 2, 'cols': 15}
                                  ),
            'address': forms.Textarea(attrs={'rows': 2, 'cols': 15},)
        }

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': field
            })

    # code
