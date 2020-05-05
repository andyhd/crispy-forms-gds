from django import forms

from crispy_forms_gds.helper import FormHelper
from crispy_forms_gds.layout import HTML, Hidden, Layout, Submit


class SelectForm(forms.Form):

    sort_by = forms.ChoiceField(
        choices=(
            ("published", "Recently published"),
            ("updated", "Recently updated"),
            ("views", "Most views"),
            ("comments", "Most comments"),
        ),
        widget=forms.Select,
        label="Sort by",
    )

    def __init__(self, *args, **kwargs):
        super(SelectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout("sort_by", Submit("submit", "Submit"),)

    def get_choice(self, field):
        value = self.cleaned_data[field]
        return dict(self.fields[field].choices).get(value)

    def valid_layout(self):
        value = self.cleaned_data["sort_by"]
        self.helper.layout = Layout(
            Hidden("sort_by", value),
            HTML.h2("You answered..."),
            HTML.table(None, [("Sort by:", self.get_choice("sort_by"))]),
            Submit("continue", "Continue"),
        )
