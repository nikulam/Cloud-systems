import grpc
import sys
from proto import restaurant_pb2
from proto import restaurant_pb2_grpc
from concurrent import futures

RESTAURANT_ITEMS_FOOD = ["chips", "fish", "burger", "pizza", "pasta", "salad"]
RESTAURANT_ITEMS_DRINK = ["water", "fizzy drink", "juice", "smoothie", "coffee", "beer"]
RESTAURANT_ITEMS_DESSERT = ["ice cream", "chocolate cake", "cheese cake", "brownie", "pancakes", "waffles"]

class Restaurant(restaurant_pb2_grpc.RestaurantServicer):

    # Logic goes here

    def FoodOrder(self, request, context):
        ID = request.orderID
        inMenu = set(request.items).issubset(set(RESTAURANT_ITEMS_FOOD))
        if inMenu:
            return restaurant_pb2.RestaurantResponse(orderID=ID,
                                                    status=restaurant_pb2.RestaurantResponse.Status.ACCEPTED)
        else:
            return restaurant_pb2.RestaurantResponse(orderID=ID,
                                                    status=restaurant_pb2.RestaurantResponse.Status.REJECTED)

    def DrinkOrder(self, request, context):
        ID = request.orderID
        inMenu = set(request.items).issubset(set(RESTAURANT_ITEMS_DRINK))
        if inMenu:
            return restaurant_pb2.RestaurantResponse(orderID=ID,
                                                    status=restaurant_pb2.RestaurantResponse.Status.ACCEPTED)
        else:
            return restaurant_pb2.RestaurantResponse(orderID=ID,
                                                    status=restaurant_pb2.RestaurantResponse.Status.REJECTED)
    def DessertOrder(self, request, context):
        ID = request.orderID
        inMenu = set(request.items).issubset(set(RESTAURANT_ITEMS_DESSERT))
        if inMenu:
            return restaurant_pb2.RestaurantResponse(orderID=ID,
                                                    status=restaurant_pb2.RestaurantResponse.Status.ACCEPTED)
        else:
            return restaurant_pb2.RestaurantResponse(orderID=ID,
                                                    status=restaurant_pb2.RestaurantResponse.Status.REJECTED)


def serve():

    # Logic goes here
    # Remember to start the server on localhost and a port defined by the first command line argument
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    restaurant_pb2_grpc.add_RestaurantServicer_to_server(Restaurant(), server)
    server.add_insecure_port('localhost:' + sys.argv[1])
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()
