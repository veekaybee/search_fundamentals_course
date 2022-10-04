# Create an index with non-default settings.

import logging
from opensearchpy import OpenSearch

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
logging.basicConfig(format='%(levelname)s:%(message)s')

host = 'localhost'
port = 9200
auth = ('admin', 'admin')  # For testing only. Don't store credentials in code.

# Create the client with SSL/TLS enabled, but hostname and certificate verification disabled.
client = OpenSearch(
    hosts=[{'host': host, 'port': port}],
    http_compress=True,  # enables gzip compression for request bodies
    http_auth=auth,
    # client_cert = client_cert_path,
    # client_key = client_key_path,
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)

index_name = 'bbuy_products'
index_body = {
  'settings': {
    'index': {
      'query':{
          'default_field': "body"
      }
    }
  }
}

response = client.indices.create(index_name, body=index_body)
print('\nCreating index:')
print(response)

docs = [
    {'productId': ['98775'], 'sku': ['430420'], 'name': ['My Romance - CD'], 'type': ['Music'], 'startDate': ['1989-07-27'], 'active': ['false'], 'regularPrice': ['9.99'], 'salePrice': ['9.99'], 'artistName': ['Carly Simon'], 'onSale': ['false'], 'digital': ['false'], 'frequentlyPurchasedWith': [], 'accessories': [], 'relatedProducts': [], 'crossSell': [], 'salesRankShortTerm': [], 'salesRankMediumTerm': [], 'salesRankLongTerm': ['78104'], 'bestSellingRank': [], 'url': [], 'categoryPath': ['Best Buy', 'Movies & Music', 'Music', 'Pop'], 'categoryPathIds': ['cat00000', 'abcat0600000', 'cat02001', 'cat02009'], 'categoryLeaf': ['cat02009'], 'categoryPathCount': 4.0, 'customerReviewCount': [], 'customerReviewAverage': [], 'inStoreAvailability': ['false'], 'onlineAvailability': ['false'], 'releaseDate': ['1990-02-22'], 'shippingCost': [], 'shortDescription': [], 'shortDescriptionHtml': [], 'class': ['COMPACT DISC'], 'classId': ['77'], 'subclass': ['POP'], 'subclassId': ['100'], 'department': ['VIDEO/COMPACT DISC'], 'departmentId': ['8'], 'bestBuyItemId': ['306736'], 'description': [], 'manufacturer': ['Arista'], 'modelNumber': [], 'image': ['http://images.bestbuy.com/BestBuy_US/images/products/4304/430420.jpg'], 'condition': [], 'inStorePickup': ['false'], 'homeDelivery': ['false'], 'quantityLimit': ['3'], 'color': [], 'depth': [], 'height': [], 'weight': [], 'shippingWeight': [], 'width': [], 'longDescription': [], 'longDescriptionHtml': [], 'features': []},
    {'productId': ['291393'], 'sku': ['430395'], 'name': ['Earth, Sun, Moon - CD'], 'type': ['Music'], 'startDate': ['1990-07-27'], 'active': ['false'], 'regularPrice': ['12.99'], 'salePrice': ['12.99'], 'artistName': ['Love and Rockets'], 'onSale': ['false'], 'digital': ['false'], 'frequentlyPurchasedWith': [], 'accessories': [], 'relatedProducts': [], 'crossSell': [], 'salesRankShortTerm': [], 'salesRankMediumTerm': [], 'salesRankLongTerm': [], 'bestSellingRank': [], 'url': [], 'categoryPath': ['Gothic'], 'categoryPathIds': ['cat02671'], 'categoryLeaf': ['cat02671'], 'categoryPathCount': 1.0, 'customerReviewCount': [], 'customerReviewAverage': [], 'inStoreAvailability': ['false'], 'onlineAvailability': ['false'], 'releaseDate': ['1990-10-25'], 'shippingCost': [], 'shortDescription': [], 'shortDescriptionHtml': [], 'class': ['COMPACT DISC'], 'classId': ['77'], 'subclass': ['ALTERNATIVE'], 'subclassId': ['1038'], 'department': ['VIDEO/COMPACT DISC'], 'departmentId': ['8'], 'bestBuyItemId': ['44128'], 'description': [], 'manufacturer': ['Beggars Banquet/Big Time'], 'modelNumber': [], 'image': ['http://images.bestbuy.com/BestBuy_US/images/products/nonsku/default_music_l.jpg'], 'condition': [], 'inStorePickup': ['false'], 'homeDelivery': ['false'], 'quantityLimit': ['3'], 'color': [], 'depth': [], 'height': [], 'weight': [], 'shippingWeight': [], 'width': [], 'longDescription': [], 'longDescriptionHtml': [], 'features': []},
    {'productId': ['88396'], 'sku': ['430402'], 'name': ["That's What - CD"], 'type': ['Music'], 'startDate': ['1989-11-14'], 'active': ['false'], 'regularPrice': ['12.99'], 'salePrice': ['12.99'], 'artistName': ['Leo Kottke'], 'onSale': ['false'], 'digital': ['false'], 'frequentlyPurchasedWith': [], 'accessories': [], 'relatedProducts': [], 'crossSell': [], 'salesRankShortTerm': [], 'salesRankMediumTerm': [], 'salesRankLongTerm': [], 'bestSellingRank': [], 'url': [], 'categoryPath': ['Best Buy', 'Movies & Music', 'Music', 'Folk'], 'categoryPathIds': ['cat00000', 'abcat0600000', 'cat02001', 'cat02005'], 'categoryLeaf': ['cat02005'], 'categoryPathCount': 4.0, 'customerReviewCount': [], 'customerReviewAverage': [], 'inStoreAvailability': ['false'], 'onlineAvailability': ['false'], 'releaseDate': ['1990-06-12'], 'shippingCost': [], 'shortDescription': [], 'shortDescriptionHtml': [], 'class': ['COMPACT DISC'], 'classId': ['77'], 'subclass': ['FOLK'], 'subclassId': ['1017'], 'department': ['VIDEO/COMPACT DISC'], 'departmentId': ['8'], 'bestBuyItemId': ['382573'], 'description': [], 'manufacturer': ['Private Music'], 'modelNumber': [], 'image': ['http://images.bestbuy.com/BestBuy_US/images/products/4304/430402.jpg'], 'condition': [], 'inStorePickup': ['false'], 'homeDelivery': ['false'], 'quantityLimit': ['3'], 'color': [], 'depth': [], 'height': [], 'weight': [], 'shippingWeight': [], 'width': [], 'longDescription': [], 'longDescriptionHtml': [], 'features': []},
    {'productId': ['103941'], 'sku': ['430411'], 'name': ['Greatest Hits - CD'], 'type': ['Music'], 'startDate': ['1989-12-19'], 'active': ['true'], 'regularPrice': ['8.99'], 'salePrice': ['8.99'], 'artistName': ['Keith Whitley'], 'onSale': ['false'], 'digital': ['false'], 'frequentlyPurchasedWith': [], 'accessories': [], 'relatedProducts': [], 'crossSell': [], 'salesRankShortTerm': [], 'salesRankMediumTerm': [], 'salesRankLongTerm': ['242672'], 'bestSellingRank': [], 'url': ['http://www.bestbuy.com/site/Greatest+Hits+-+CD/430411.p?id=103941&skuId=430411&cmp=RMX'], 'categoryPath': ['Best Buy', 'Movies & Music', 'Music', 'Country'], 'categoryPathIds': ['cat00000', 'abcat0600000', 'cat02001', 'cat02003'], 'categoryLeaf': ['cat02003'], 'categoryPathCount': 4.0, 'customerReviewCount': [], 'customerReviewAverage': [], 'inStoreAvailability': ['false'], 'onlineAvailability': ['true'], 'releaseDate': ['1990-07-17'], 'shippingCost': ['0.00'], 'shortDescription': [], 'shortDescriptionHtml': [], 'class': ['COMPACT DISC'], 'classId': ['77'], 'subclass': ['COUNTRY'], 'subclassId': ['1005'], 'department': ['VIDEO/COMPACT DISC'], 'departmentId': ['8'], 'bestBuyItemId': ['360034'], 'description': [], 'manufacturer': ['RCA'], 'modelNumber': [], 'image': ['http://images.bestbuy.com/BestBuy_US/images/products/4304/430411.jpg'], 'condition': [], 'inStorePickup': ['true'], 'homeDelivery': ['false'], 'quantityLimit': ['3'], 'color': [], 'depth': [], 'height': [], 'weight': [], 'shippingWeight': [], 'width': [], 'longDescription': [], 'longDescriptionHtml': [], 'features': []}    
]

for doc in docs:
    doc_id = doc['productId']
    print("Indexing {}".format(doc_id))
    response = client.index(
        index=index_name,
        body=doc,
        id=doc_id,
        refresh=True
    )
    print('\n\tResponse:')
    print(response)

# Verify they are in:
print(client.cat.count(index_name, params={"v": "true"}))

