from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from .constants import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE


class CustomPageNumberPagination(PageNumberPagination):
    page_size = DEFAULT_PAGE_SIZE
    page_size_query_param = 'page_size'
    max_page_size = MAX_PAGE_SIZE
    page_query_param = 'page'

    def get_page_size(self, request):
        try:
            page_size = int(request.query_params.get(self.page_size_query_param, self.page_size))
            if page_size > self.max_page_size:
                raise ValidationError(f"page_size cannot be more than {self.max_page_size}")
            return page_size
        except ValueError:
            raise ValidationError("Invalid page_size. It must be an integer.")

    def get_paginated_response(self, data):
        return Response({
            "results": data,
            "pages": {
                "total_count": self.page.paginator.count,
                "has_next": self.page.has_next(),
                "previous": self.get_previous_link(),
                "pageNumber": self.page.number,
                "page_size": self.get_page_size(self.request),
            }
        })
