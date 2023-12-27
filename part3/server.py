import rpyc
from rpyc.utils.server import ThreadedServer


@rpyc.service
class ComputationalServer(rpyc.Service):
    # addition
    @rpyc.exposed
    def find_sum(self, n1, n2):
        sum = n1 + n2
        return sum

    # sort
    @rpyc.exposed
    def sort_array(self, arr_str):
        arr = arr_str.split(" ")
        result = sorted(arr)
        return result


# Execution start
if __name__ == "__main__":
    server = ThreadedServer(ComputationalServer, port=34567)
    print("Server Started")
    server.start()
