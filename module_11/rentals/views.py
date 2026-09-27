from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from properties.models import Property
from .models import RentalRequest, Review, RequestStatus
from .forms import RentalRequestForm, ReviewForm


@login_required
def create_rental_request(request, property_id):
    property_obj = get_object_or_404(Property, pk=property_id)

    if property_obj.owner == request.user:
        messages.error(request, "You cannot send a rental request for your own property.")
        return redirect("property_detail", pk=property_id)

    if request.method == "POST":
        form = RentalRequestForm(request.POST, property_obj=property_obj, user=request.user)
        if form.is_valid():
            req = form.save(commit=False)
            req.property = property_obj
            req.tenant = request.user
            req.status = RequestStatus.PENDING
            req.save()
            messages.success(request, "Your rental request has been sent successfully!")
            return redirect("tenant_dashboard")
        else:
            for error in form.non_field_errors():
                messages.error(request, error)
            return redirect("property_detail", pk=property_id)

    return redirect("property_detail", pk=property_id)


@login_required
def cancel_rental_request(request, pk):
    rental_req = get_object_or_404(RentalRequest, pk=pk, tenant=request.user)
    if rental_req.status == RequestStatus.PENDING:
        rental_req.status = RequestStatus.CANCELLED
        rental_req.save(update_fields=["status"])
        messages.success(request, "Rental request cancelled successfully.")
    else:
        messages.error(request, "Only pending requests can be cancelled.")
    return redirect("tenant_dashboard")


@login_required
def update_request_status(request, pk, action):
    rental_req = get_object_or_404(RentalRequest, pk=pk, property__owner=request.user)
    if action == "accept":
        rental_req.status = RequestStatus.ACCEPTED
        rental_req.save(update_fields=["status"])
        messages.success(request, f"Rental request from {rental_req.tenant.email} accepted.")
    elif action == "reject":
        rental_req.status = RequestStatus.REJECTED
        rental_req.save(update_fields=["status"])
        messages.info(request, f"Rental request from {rental_req.tenant.email} rejected.")
    else:
        messages.error(request, "Invalid action.")
    return redirect("owner_dashboard")


@login_required
def owner_dashboard(request):
    owner_properties = request.user.properties.prefetch_related("images").all()
    total_properties = owner_properties.count()
    available_properties = owner_properties.filter(availability_status=True).count()

    rental_requests = RentalRequest.objects.filter(
        property__owner=request.user
    ).select_related("property", "tenant").order_by("-created_at")

    total_requests = rental_requests.count()
    pending_requests = rental_requests.filter(status=RequestStatus.PENDING).count()
    accepted_requests = rental_requests.filter(status=RequestStatus.ACCEPTED).count()

    return render(request, "rentals/owner_dashboard.html", {
        "total_properties": total_properties,
        "available_properties": available_properties,
        "total_requests": total_requests,
        "pending_requests": pending_requests,
        "accepted_requests": accepted_requests,
        "rental_requests": rental_requests,
        "owner_properties": owner_properties,
    })


@login_required
def tenant_dashboard(request):
    tenant_requests = RentalRequest.objects.filter(
        tenant=request.user
    ).select_related("property", "property__owner").order_by("-created_at")

    total_requests = tenant_requests.count()
    pending_requests = tenant_requests.filter(status=RequestStatus.PENDING).count()
    accepted_requests = tenant_requests.filter(status=RequestStatus.ACCEPTED).count()
    rejected_requests = tenant_requests.filter(status=RequestStatus.REJECTED).count()

    # Pre-calculate which properties can be reviewed
    reviewed_property_ids = set(
        Review.objects.filter(tenant=request.user).values_list("property_id", flat=True)
    )

    return render(request, "rentals/tenant_dashboard.html", {
        "tenant_requests": tenant_requests,
        "total_requests": total_requests,
        "pending_requests": pending_requests,
        "accepted_requests": accepted_requests,
        "rejected_requests": rejected_requests,
        "reviewed_property_ids": reviewed_property_ids,
    })


@login_required
def create_review(request, property_id):
    property_obj = get_object_or_404(Property, pk=property_id)
    if request.method == "POST":
        form = ReviewForm(request.POST, property_obj=property_obj, user=request.user)
        if form.is_valid():
            rev = form.save(commit=False)
            rev.property = property_obj
            rev.tenant = request.user
            rev.save()
            messages.success(request, "Thank you! Your review has been published.")
        else:
            for error in form.non_field_errors():
                messages.error(request, error)
            for field, errors in form.errors.items():
                for err in errors:
                    messages.error(request, f"{field.title()}: {err}")
    return redirect("property_detail", pk=property_id)
