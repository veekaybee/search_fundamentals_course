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
{'productId': ['0'], 'sku': ['9999185200050004'], 'name': ['Dell Inspiron I660S-2000BK Desktop & 20" LED Monitor Package'], 'type': ['Bundle'], 'startDate': ['2012-07-22'], 'active': ['true'], 'regularPrice': ['499.98'], 'salePrice': ['499.98'], 'artistName': [], 'onSale': ['false'], 'digital': ['false'], 'frequentlyPurchasedWith': [], 'accessories': [], 'relatedProducts': [], 'crossSell': [], 'salesRankShortTerm': [], 'salesRankMediumTerm': [], 'salesRankLongTerm': [], 'bestSellingRank': [], 'url': ['http://www.bestbuy.com/site/Dell+Inspiron+I660S-2000BK+Desktop+%26+20%22+LED+Monitor+Package/9999185200050004.p?id=pcmprd184700050004&skuId=9999185200050004&cmp=RMX'], 'categoryPath': ['Best Buy', 'Computers & Tablets', 'Desktop & All-in-One Computers', 'Desktop Packages'], 'categoryPathIds': ['cat00000', 'abcat0500000', 'abcat0501000', 'pcmcat212600050011'], 'categoryLeaf': ['pcmcat212600050011'], 'categoryPathCount': 4.0, 'customerReviewCount': [], 'customerReviewAverage': [], 'inStoreAvailability': ['true'], 'onlineAvailability': ['true'], 'releaseDate': [], 'shippingCost': [], 'shortDescription': [], 'shortDescriptionHtml': [], 'class': [], 'classId': [], 'subclass': [], 'subclassId': [], 'department': [], 'departmentId': [], 'bestBuyItemId': [], 'description': [], 'manufacturer': [], 'modelNumber': [], 'image': ['http://images.bestbuy.com/BestBuy_US/images/products/9999/pcmprd184700050004_sc.jpg'], 'condition': [], 'inStorePickup': [], 'homeDelivery': [], 'quantityLimit': [], 'color': [], 'depth': [], 'height': [], 'weight': [], 'shippingWeight': [], 'width': [], 'longDescription': ['Complete your tasks quickly with this compact desktop and monitor duo (I660S-2000BK, IN2030M).  Key features: Intel® Pentium® processor G630; 4GB DDR3 memory; 500GB hard drive; Windows 7 Home Premium; built-in wireless networking; 20" widescreen LED HD monitor included'], 'longDescriptionHtml': [], 'features': []},
{'productId': ['0'], 'sku': ['9999185200050006'], 'name': ['Gateway DX4870-UB20P Desktop & 21.5" LCD Monitor Package'], 'type': ['Bundle'], 'startDate': ['2012-07-22'], 'active': ['true'], 'regularPrice': ['549.98'], 'salePrice': ['549.98'], 'artistName': [], 'onSale': ['false'], 'digital': ['false'], 'frequentlyPurchasedWith': [], 'accessories': [], 'relatedProducts': [], 'crossSell': [], 'salesRankShortTerm': [], 'salesRankMediumTerm': [], 'salesRankLongTerm': [], 'bestSellingRank': [], 'url': ['http://www.bestbuy.com/site/Gateway+DX4870-UB20P+Desktop+%26+21.5%22+LCD+Monitor+Package/9999185200050006.p?id=pcmprd184700050006&skuId=9999185200050006&cmp=RMX'], 'categoryPath': ['Best Buy', 'Computers & Tablets', 'Desktop & All-in-One Computers', 'Desktop Packages'], 'categoryPathIds': ['cat00000', 'abcat0500000', 'abcat0501000', 'pcmcat212600050011'], 'categoryLeaf': ['pcmcat212600050011'], 'categoryPathCount': 4.0, 'customerReviewCount': [], 'customerReviewAverage': [], 'inStoreAvailability': ['true'], 'onlineAvailability': ['true'], 'releaseDate': [], 'shippingCost': [], 'shortDescription': [], 'shortDescriptionHtml': [], 'class': [], 'classId': [], 'subclass': [], 'subclassId': [], 'department': [], 'departmentId': [], 'bestBuyItemId': [], 'description': [], 'manufacturer': [], 'modelNumber': [], 'image': ['http://images.bestbuy.com/BestBuy_US/images/products/9999/pcmprd184700050006_sc.jpg'], 'condition': [], 'inStorePickup': [], 'homeDelivery': [], 'quantityLimit': [], 'color': [], 'depth': [], 'height': [], 'weight': [], 'shippingWeight': [], 'width': [], 'longDescription': ['Gear up for your digital photos, music and home movies with this wireless-enabled desktop and monitor matchup (DX4870-UB20P, FHX2201QV).  Key features: Intel® Core™ i3-2120 processor; 6GB DDR3 memory; 1TB hard drive; Windows 7 Home Premium; built-in wireless networking; 21.5" widescreen LCD monitor included'], 'longDescriptionHtml': [], 'features': []},
{'productId': ['0'], 'sku': ['9999185200050007'], 'name': ['Asus Essentio CM6730-06 Desktop & 20" LED Monitor Package'], 'type': ['Bundle'], 'startDate': ['2012-07-22'], 'active': ['true'], 'regularPrice': ['599.98'], 'salePrice': ['599.98'], 'artistName': [], 'onSale': ['false'], 'digital': ['false'], 'frequentlyPurchasedWith': [], 'accessories': [], 'relatedProducts': [], 'crossSell': [], 'salesRankShortTerm': [], 'salesRankMediumTerm': [], 'salesRankLongTerm': [], 'bestSellingRank': [], 'url': ['http://www.bestbuy.com/site/Asus+Essentio+CM6730-06+Desktop+%26+20%22+LED+Monitor+Package/9999185200050007.p?id=pcmprd184700050007&skuId=9999185200050007&cmp=RMX'], 'categoryPath': ['Best Buy', 'Computers & Tablets', 'Desktop & All-in-One Computers', 'Desktop Packages'], 'categoryPathIds': ['cat00000', 'abcat0500000', 'abcat0501000', 'pcmcat212600050011'], 'categoryLeaf': ['pcmcat212600050011'], 'categoryPathCount': 4.0, 'customerReviewCount': [], 'customerReviewAverage': [], 'inStoreAvailability': ['true'], 'onlineAvailability': ['true'], 'releaseDate': [], 'shippingCost': [], 'shortDescription': [], 'shortDescriptionHtml': [], 'class': [], 'classId': [], 'subclass': [], 'subclassId': [], 'department': [], 'departmentId': [], 'bestBuyItemId': [], 'description': [], 'manufacturer': [], 'modelNumber': [], 'image': ['http://images.bestbuy.com/BestBuy_US/images/products/9999/pcmprd184700050007_sc.jpg'], 'condition': [], 'inStorePickup': [], 'homeDelivery': [], 'quantityLimit': [], 'color': [], 'depth': [], 'height': [], 'weight': [], 'shippingWeight': [], 'width': [], 'longDescription': ['Easily transfer, edit, organize and share your digital photos and videos with this powerful desktop and monitor package (CM6730-06, VS208NR-B).  Key features: Intel® Core™ i5-2320 processor; 6GB DDR3 memory; 1TB hard drive; Windows 7 Home Premium; 20" widescreen LED monitor included'], 'longDescriptionHtml': [], 'features': [],
'productId': ['0'], 'sku': ['44444'], 'name': ['sample'], 'type': ['Bundle'], 'startDate': ['2011-08-05'], 'active': ['false'], 'regularPrice': ['172.98'], 'salePrice': ['172.98'], 'artistName': ['sample'], 'onSale': ['false'], 'digital': ['false'], 'frequentlyPurchasedWith': ['sample'], 'accessories': ['sample'], 'relatedProducts': ['sample'], 'crossSell': ['sample'], 'salesRankShortTerm': ['sample'], 'salesRankMediumTerm': [2], 'salesRankLongTerm': [1], 'bestSellingRank': [1], 'url': ['sample'], 'categoryPath': ['Best Buy', 'Car, Marine & GPS'], 'categoryPathIds': ['cat00000', 'abcat0300000'], 'categoryLeaf': ['abcat0300000'], 'categoryPathCount': 2.0, 'customerReviewCount': [1], 'customerReviewAverage': [1], 'inStoreAvailability': ['true'], 'onlineAvailability': ['true'], 'releaseDate': ['2020-01-01'], 'shippingCost': ['4.99'], 'shortDescription': ['sample'], 'shortDescriptionHtml': ['sample'], 'class': ['sample'], 'classId': [200], 'subclass': [2000], 'subclassId': [2000], 'department': ['sample'], 'departmentId': [200], 'bestBuyItemId': [200], 'description': ['sample'], 'manufacturer': ['sample'], 'modelNumber': ['D150'], 'image': ['sample'], 'condition': ['sample'], 'inStorePickup': ['sample'], 'homeDelivery': ['sample'], 'quantityLimit': ['sample'], 'color': ['sample'], 'depth': [200], 'height': [200], 'weight': [200], 'shippingWeight': [200], 'width': [200], 'longDescription': [200], 'longDescriptionHtml': ['sample'], 'features': ['sample']}
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

