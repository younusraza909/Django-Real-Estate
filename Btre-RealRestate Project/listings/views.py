from django.shortcuts import render,get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from .models import Listing


def index(request):
    # objects.all to get all data
    # .order by to get data according to something
    # "-" used to get it descending order
    # filter(field_name) to get only data that pass through condition
    listings = Listing.objects.order_by("-list_date").filter(is_published=True)

    # pagintion to show specified number per page
    paginator = Paginator(listings, 6)
    page = request.GET.get("page")
    paged_listings = paginator.get_page(page)

    context = {
        # isntead of using listing we have to pass paged_listings
        "listings": paged_listings
    }

    return render(request, "listings/listings.html", context)


def listing(request, listing_id):
    #if it cant load that data it will show 404
    #pk primary key
    listing = get_object_or_404(Listing,pk=listing_id)
    

    context={
        "listing":listing
    }

    return render(request, "listings/listing.html",context)


def search(request):
    return render(request, "listings/search.html")
