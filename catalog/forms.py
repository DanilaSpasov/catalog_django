from django import forms

from catalog.models import Product

BANNED_WORDS = [
    "казино",
    "криптовалюта",
    "крипта",
    "биржа",
    "дешево",
    "дёшево",
    "бесплатно",
    "обман",
    "полиция",
    "радар",
]


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "image", "category", "price"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["title"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите название"}
        )

        self.fields["description"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите описание"}
        )

        self.fields["image"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Загрузите изображение"}
        )

        self.fields["category"].widget.attrs.update(
            {
                "class": "form-control",
            }
        )

        self.fields["price"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите цену"}
        )

    def clean(self):
        cleaned_data = super().clean()
        lower_title = cleaned_data.get("title", "").lower()
        lower_description = cleaned_data.get("description", "").lower()
        for word in BANNED_WORDS:
            if word in lower_title or word in lower_description:
                raise forms.ValidationError(
                    f"Запрещено использовать слово {word} в заголовке или описании."
                )
        return cleaned_data

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price is not None and price < 0:
            raise forms.ValidationError("Цена не может быть отрицательной.")
        return price


class ModeratorProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["publication_status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["publication_status"].widget.attrs.update(
            {"class": "form-check-input", "placeholder": "Опубликовано"}
        )
