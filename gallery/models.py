from django.db import models
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.images.edit_handlers import ImageChooserPanel

# Gallery index page, that links to GallerySubpages
class GalleryIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        context = super().get_context(request)
        gallery_subpages = self.get_children().live().order_by('-first_published_at')
        context['gallery_subpages'] = gallery_subpages
        return context


# GallerySubpage that contains images
class GallerySubpage(Page):
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)

    miniature = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        InlinePanel('gallery_images', label = "Images that will be displayed on this page"),
        ImageChooserPanel('miniature'),
    ]

class GalleryImage(Orderable):
    page = ParentalKey(GallerySubpage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )

    panels = [
        ImageChooserPanel('image'),
    ]
