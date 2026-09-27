from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q, Avg
from .models import Property, PropertyType
from .forms import PropertyForm
from rentals.models import RentalRequest, Review, RequestStatus
from rentals.forms import RentalRequestForm, ReviewForm


def property_list(request):
    properties = Property.objects.select_related("owner").prefetch_related("images").all()

    q = request.GET.get("q", "").strip()
    property_type = request.GET.get("property_type", "").strip()
    min_price = request.GET.get("min_price", "").strip()
    max_price = request.GET.get("max_price", "").strip()

    if q:
        properties = properties.filter(
            Q(title__icontains=q) |
            Q(location__icontains=q) |
            Q(description__icontains=q)
        )
    if property_type:
        properties = properties.filter(property_type=property_type)
    if min_price:
        try:
            properties = properties.filter(monthly_rent__gte=float(min_price))
        except ValueError:
            pass
    if max_price:
        try:
            properties = properties.filter(monthly_rent__lte=float(max_price))
        except ValueError:
            pass

    return render(request, "properties/dashboard.html", {
        "properties": properties,
        "search_query": q,
        "selected_type": property_type,
        "min_price": min_price,
        "max_price": max_price,
        "property_types": PropertyType.choices,
    })


def property_detail(request, pk):
    property = get_object_or_404(
        Property.objects.select_related("owner").prefetch_related("images", "reviews__tenant"),
        pk=pk,
    )
    images = property.images.all()
    cover = images.first()

    reviews = property.reviews.all()
    avg_rating = reviews.aggregate(Avg("rating"))["rating__avg"]

    user_pending_request = False
    user_accepted_request = False
    user_has_reviewed = False
    request_form = None
    review_form = None

    if request.user.is_authenticated:
        user_pending_request = RentalRequest.objects.filter(
            property=property, tenant=request.user, status=RequestStatus.PENDING
        ).exists()
        user_accepted_request = RentalRequest.objects.filter(
            property=property, tenant=request.user, status=RequestStatus.ACCEPTED
        ).exists()
        user_has_reviewed = Review.objects.filter(
            property=property, tenant=request.user
        ).exists()

        request_form = RentalRequestForm(property_obj=property, user=request.user)
        review_form = ReviewForm(property_obj=property, user=request.user)

    return render(request, "properties/property_detail.html", {
        "property": property,
        "images": images,
        "cover": cover,
        "reviews": reviews,
        "avg_rating": round(avg_rating, 1) if avg_rating else None,
        "user_pending_request": user_pending_request,
        "user_accepted_request": user_accepted_request,
        "user_has_reviewed": user_has_reviewed,
        "request_form": request_form,
        "review_form": review_form,
    })


@login_required
def property_create_view(request):
    # Ensure owner role when creating property
    if not request.user.is_owner:
        request.user.role = 'OWNER'
        request.user.save(update_fields=['role'])

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            prop = form.save(owner=request.user)
            messages.success(request, f"Property '{prop.title}' has been successfully created!")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors in the property form.")
    else:
        form = PropertyForm()

    return render(request, "properties/property_form.html", {
        "form": form,
        "title": "Add New Property",
        "button_text": "Publish Listing",
    })


@login_required
def property_update_view(request, pk):
    property_obj = get_object_or_404(Property, pk=pk, owner=request.user)

    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property_obj)
        if form.is_valid():
            prop = form.save()
            messages.success(request, f"Property '{prop.title}' updated successfully!")
            return redirect('profile')
        else:
            messages.error(request, "Please correct the errors in the property form.")
    else:
        form = PropertyForm(instance=property_obj)

    return render(request, "properties/property_form.html", {
        "form": form,
        "property": property_obj,
        "title": f"Edit {property_obj.title}",
        "button_text": "Save Changes",
    })