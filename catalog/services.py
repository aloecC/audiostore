from .models import Product, Category


class CatalogService:
    from .models import Product

    def get_products_by_category(category_id):
        """
        Возвращает список всех продуктов в указанной категории.
        :param category_id: ID категории, для которой нужно получить продукты.
        :return: QuerySet продуктов в указанной категории.
        """
        return Product.objects.filter(category_id=category_id)