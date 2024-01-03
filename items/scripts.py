from items.models import Items
from items.searializers import BaseItemSerializer

def add_data_to_items(data):
    items = []
    for rec in data:
        serializer = BaseItemSerializer(data=rec)
        try:
            serializer.is_valid(raise_exception=True)
            items.append(Items(**rec))
        except:
            pass
    Items.objects.bulk_create(items)
