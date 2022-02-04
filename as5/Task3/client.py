import grpc
import sys
from proto import restaurant_pb2
from proto import restaurant_pb2_grpc

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    '''with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='you'))
    print("Greeter client received: " + response.message)
    '''
    channel = grpc.insecure_channel('localhost:50051')
    stub = restaurant_pb2_grpc.RestaurantStub(channel)
    response = stub.DrinkOrder(restaurant_pb2.RestaurantRequest(orderID='1234',
                                                                items=[ "fizzy drinks", "water", "water" ]))
    print(response.status)

if __name__ == '__main__':
    run()
