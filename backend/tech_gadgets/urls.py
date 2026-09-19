from django.urls import path
from .views import  single_gadget_int_view, GadgetView, RedirectToGadgetView,start_page_view, start_manufacturer_view, start_manufacturer_Post_view



urlpatterns = [

    path('start/', start_page_view),
    path('', RedirectToGadgetView.as_view()),
    path('<int:gadget_id>', RedirectToGadgetView.as_view()),
    path("gadget/", GadgetView.as_view() ),
    path('gadget/<int:gadget_id>', single_gadget_int_view ),
    path('gadget/<slug:gadget_slug>', GadgetView.as_view(), name="gadget_slug_url"),
    path('manufacturer/<int:manufacturer_id>', start_manufacturer_view),
    path("manufacturer/send_manufacturer/", start_manufacturer_Post_view)
#

]